#!/usr/bin/env python3
"""
LocalMonero Knowledge Base Scraper

Scrapes all articles from localmonero.co/nojs/knowledge in all available languages
and converts them to Hugo-compatible markdown files.
"""

import asyncio
import os
import re
import json
import httpx
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin
from pathlib import Path

# Configuration
BASE_URL = "https://localmonero.co"
KNOWLEDGE_URL = f"{BASE_URL}/nojs/knowledge"
REQUEST_DELAY = 0.3  # Delay between requests
TIMEOUT = 30

# All supported languages
LANGUAGES = [
    "en", "ko",
    # "ar", "bg", "cs", "da", "de", "el", "es", "fi", "fr",
    # "ha", "hi", "hu", "id", "it", "ja", "lt", "lv", "nb",
    # "nl", "pl", "pt-br", "ro", "ru", "sk", "sl", "so", "sv", "sw",
    # "tl", "tr", "ur", "zh-cn", "zh-tw"
]

# Language display names for Hugo config
LANGUAGE_NAMES = {
    "en": "English", "ar": "العربية", "bg": "Български", "cs": "Čeština",
    "da": "Dansk", "de": "Deutsch", "el": "Ελληνικά", "es": "Español",
    "fi": "Suomi", "fr": "Français", "ha": "Hausa", "hi": "हिन्दी",
    "hu": "Magyar", "id": "Bahasa Indonesia", "it": "Italiano", "ja": "日本語",
    "ko": "한국어", "lt": "Lietuvių", "lv": "Latviešu", "nb": "Norsk Bokmål",
    "nl": "Nederlands", "pl": "Polski", "pt-br": "Português (Brasil)",
    "ro": "Română", "ru": "Русский", "sk": "Slovenčina", "sl": "Slovenščina",
    "so": "Soomaali", "sv": "Svenska", "sw": "Kiswahili", "tl": "Tagalog",
    "tr": "Türkçe", "ur": "اردو", "zh-cn": "简体中文", "zh-tw": "繁體中文"
}

# RTL languages
RTL_LANGUAGES = ["ar", "ur"]

# Output directories
OUTPUT_DIR = Path(__file__).parent.parent / "hugo-site"
CONTENT_DIR = OUTPUT_DIR / "content" / "knowledge"
IMAGES_DIR = OUTPUT_DIR / "static" / "images"


def setup_html2text():
    """Configure html2text converter."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = True
    return h


def is_error_page(html: str) -> bool:
    """Check if the response is an error page."""
    error_indicators = [
        "429 Too Many Requests",
        "Rate limit exceeded",
        "Access denied",
        "403 Forbidden",
        "502 Bad Gateway",
        "503 Service Unavailable",
    ]
    for indicator in error_indicators:
        if indicator in html:
            return True
    return False


async def fetch_page(client: httpx.AsyncClient, url: str, lang: str = None) -> str | None:
    """Fetch a page with retry logic."""
    max_retries = 5
    base_delay = 2

    # Build params and headers for language
    params = {"language": lang} if lang and lang != "en" else None
    headers = {"Accept-Language": lang} if lang else {"Accept-Language": "en"}

    for attempt in range(max_retries):
        try:
            await asyncio.sleep(REQUEST_DELAY)
            # Clear cookies to prevent language caching
            client.cookies.clear()
            # Build request to see actual URL
            request = client.build_request("GET", url, params=params, headers=headers)
            response = await client.send(request, follow_redirects=True)
            response.raise_for_status()

            html = response.text

            if is_error_page(html):
                delay = base_delay * (2 ** attempt)
                print(f"    Rate limited, waiting {delay}s...")
                await asyncio.sleep(delay)
                continue

            return html

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                delay = base_delay * (2 ** attempt)
                print(f"    429 error, waiting {delay}s...")
                await asyncio.sleep(delay)
            else:
                print(f"    HTTP error: {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(base_delay)
        except httpx.HTTPError as e:
            print(f"    Network error: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(base_delay)

    return None


async def get_article_slugs(client: httpx.AsyncClient) -> list[str]:
    """Get all article slugs from the main knowledge page."""
    print("Fetching article list...")
    html = await fetch_page(client, KNOWLEDGE_URL)
    if not html:
        raise Exception("Failed to fetch main knowledge page")

    soup = BeautifulSoup(html, "html.parser")
    slugs = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        match = re.match(r"/nojs/knowledge/([a-z0-9-]+)$", href)
        if match:
            slug = match.group(1)
            if slug not in slugs:
                slugs.append(slug)

    print(f"Found {len(slugs)} articles")
    return slugs


def extract_article_content(html: str, slug: str, lang: str) -> dict | None:
    """Extract article content from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    title_elem = soup.find("h1")
    if not title_elem:
        return None

    title = title_elem.get_text(strip=True)

    if "Too Many Requests" in title or "Error" in title:
        return None

    # Find the main content paper div
    content_div = None
    for paper in soup.find_all("div", class_=lambda x: x and "MuiPaper" in x):
        if paper.find("img") or paper.find("p"):
            text = paper.get_text()
            if "winding down" not in text.lower() and len(text) > 200:
                content_div = paper
                break

    if not content_div:
        for div in soup.find_all("div"):
            paragraphs = div.find_all("p")
            if len(paragraphs) > 3:
                content_div = div
                break

    # Extract image
    image_url = None
    image_credit = None
    if content_div:
        img = content_div.find("img")
        if img and img.get("src"):
            src = img["src"]
            if "/knowledge/" in src:
                image_url = src
                credit_span = content_div.find("span", class_=lambda x: x and "caption" in str(x).lower())
                if credit_span:
                    credit_link = credit_span.find("a")
                    if credit_link:
                        image_credit = {
                            "text": credit_link.get_text(strip=True),
                            "url": credit_link.get("href", "")
                        }

    # Extract date
    date = None
    time_elem = soup.find("time")
    if time_elem:
        date = time_elem.get("datetime", time_elem.get_text(strip=True))

    # Extract body content
    body_html = ""
    if content_div:
        content_copy = BeautifulSoup(str(content_div), "html.parser")

        for elem in content_copy.find_all(["img", "span"], recursive=True):
            if elem.name == "img" or (elem.get("class") and "caption" in str(elem.get("class"))):
                elem.decompose()

        content_elements = content_copy.find_all(["p", "h2", "h3", "ul", "ol", "blockquote", "pre"])

        for elem in content_elements:
            if elem.find("a", href=lambda x: x and "/knowledge/" in x):
                parent_ul = elem.find_parent("ul")
                if parent_ul:
                    continue
            body_html += str(elem)

    return {
        "title": title,
        "slug": slug,
        "lang": lang,
        "date": date,
        "image": image_url,
        "image_credit": image_credit,
        "body_html": body_html
    }


async def download_image(client: httpx.AsyncClient, image_url: str, downloaded: set) -> str | None:
    """Download an image and return the local filename."""
    if not image_url:
        return None

    filename = os.path.basename(image_url)

    if filename in downloaded:
        return filename

    local_path = IMAGES_DIR / filename
    if local_path.exists():
        downloaded.add(filename)
        return filename

    full_url = urljoin(BASE_URL, image_url) if image_url.startswith("/") else image_url

    for attempt in range(3):
        try:
            await asyncio.sleep(REQUEST_DELAY)
            response = await client.get(full_url, timeout=TIMEOUT)
            response.raise_for_status()
            local_path.write_bytes(response.content)
            downloaded.add(filename)
            print(f"    Downloaded: {filename}")
            return filename
        except Exception as e:
            if attempt < 2:
                await asyncio.sleep(2 ** attempt)
            else:
                print(f"    Failed to download {filename}: {e}")
    return None


def html_to_markdown(html_content: str) -> str:
    """Convert HTML to Markdown."""
    if not html_content:
        return ""

    h = setup_html2text()
    markdown = h.handle(html_content)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    # Convert LocalMonero knowledge links to local links
    markdown = re.sub(r'\(/nojs/knowledge/([^)]+)\)', r'(/knowledge/\1/)', markdown)
    markdown = re.sub(r'\(https?://localmonero\.co/nojs/knowledge/([^)]+)\)', r'(/knowledge/\1/)', markdown)
    markdown = re.sub(r'\(https?://localmonero\.co/knowledge/([^)]+)\)', r'(/knowledge/\1/)', markdown)

    return markdown.strip()


def parse_date(date_str: str) -> str:
    """Convert date string to ISO format (YYYY-MM-DD)."""
    if not date_str:
        return "2024-01-01"

    import re
    from datetime import datetime

    # Try common formats
    formats = [
        "%d %B %Y %H:%M %Z",   # "01 March 2022 00:00 UTC"
        "%d %B %Y",            # "01 March 2022"
        "%B %d, %Y",           # "March 01, 2022"
        "%Y-%m-%d",            # "2022-03-01"
    ]

    # Clean the date string
    date_str = date_str.strip()

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue

    # Fallback: try to extract year-month-day with regex
    match = re.search(r'(\d{1,2})\s+(\w+)\s+(\d{4})', date_str)
    if match:
        day, month, year = match.groups()
        months = {
            'january': '01', 'february': '02', 'march': '03', 'april': '04',
            'may': '05', 'june': '06', 'july': '07', 'august': '08',
            'september': '09', 'october': '10', 'november': '11', 'december': '12'
        }
        month_num = months.get(month.lower(), '01')
        return f"{year}-{month_num}-{day.zfill(2)}"

    return "2024-01-01"


def create_hugo_markdown(article: dict, image_filename: str | None) -> str:
    """Create Hugo-compatible markdown file content."""
    front_matter = {
        "title": article["title"],
        "slug": article["slug"],
        "date": parse_date(article["date"]),
    }

    if image_filename:
        front_matter["image"] = f"/images/{image_filename}"

    if article.get("image_credit"):
        front_matter["image_credit"] = article["image_credit"]["text"]
        front_matter["image_credit_url"] = article["image_credit"]["url"]

    yaml_lines = ["---"]
    for key, value in front_matter.items():
        if isinstance(value, str):
            escaped = value.replace('"', '\\"')
            yaml_lines.append(f'{key}: "{escaped}"')
        else:
            yaml_lines.append(f"{key}: {value}")
    yaml_lines.append("---")
    yaml_lines.append("")

    body_md = html_to_markdown(article["body_html"])
    return "\n".join(yaml_lines) + body_md


async def main():
    """Main scraping function - sequential processing."""
    print("=" * 60)
    print("LocalMonero Knowledge Base Scraper")
    print("=" * 60)

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    downloaded_images: set = set()
    stats = {"scraped": 0, "failed": 0}

    base_headers = {"User-Agent": "Mozilla/5.0 (compatible; LocalMoneroKnowledgeMirror/1.0)"}

    # Disable HTTP/2 to avoid potential issues
    async with httpx.AsyncClient(headers=base_headers, follow_redirects=True, http2=False) as client:
        slugs = await get_article_slugs(client)

        total = len(slugs) * len(LANGUAGES)
        print(f"\nScraping {len(slugs)} articles × {len(LANGUAGES)} languages = {total} pages")
        print(f"Request delay: {REQUEST_DELAY}s")
        print("-" * 60)

        for i, slug in enumerate(slugs, 1):
            print(f"\n[{i}/{len(slugs)}] {slug}")

            for lang in LANGUAGES:
                url = f"{KNOWLEDGE_URL}/{slug}"
                # Debug: print URL being fetched
                full_url = f"{url}?language={lang}" if lang != "en" else url
                html = await fetch_page(client, url, lang)

                if not html:
                    stats["failed"] += 1
                    print(f"  ✗ [{lang}] fetch failed")
                    continue

                article = extract_article_content(html, slug, lang)
                if not article:
                    stats["failed"] += 1
                    print(f"  ✗ [{lang}] extraction failed")
                    continue

                # Download image (only once per article)
                image_filename = None
                if article["image"]:
                    image_filename = await download_image(client, article["image"], downloaded_images)

                # Create and save markdown
                markdown = create_hugo_markdown(article, image_filename)
                filename = f"{slug}.{lang}.md"
                filepath = CONTENT_DIR / filename
                filepath.write_text(markdown, encoding="utf-8")

                stats["scraped"] += 1
                print(f"  ✓ [{lang}] {article['title'][:40]}...")

    print("\n" + "=" * 60)
    print("Scraping Complete!")
    print("=" * 60)
    print(f"Total scraped: {stats['scraped']}")
    print(f"Failed: {stats['failed']}")
    print(f"Images downloaded: {len(downloaded_images)}")
    print(f"Output directory: {OUTPUT_DIR}")

    lang_config = {
        "languages": LANGUAGE_NAMES,
        "rtl": RTL_LANGUAGES
    }
    config_path = OUTPUT_DIR / "language_config.json"
    config_path.write_text(json.dumps(lang_config, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Language config saved to: {config_path}")


if __name__ == "__main__":
    asyncio.run(main())
