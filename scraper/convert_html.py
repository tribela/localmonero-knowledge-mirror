#!/usr/bin/env python3
"""
Convert raw HTML files to Hugo-compatible Markdown.
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import html2text
from bs4 import BeautifulSoup

RAW_HTML_DIR = Path(__file__).parent.parent / "raw_html"
HUGO_CONTENT_DIR = Path(__file__).parent.parent / "hugo-site" / "content" / "knowledge"
HUGO_IMAGES_DIR = Path(__file__).parent.parent / "hugo-site" / "static" / "images"

# HTML to Markdown converter
h2t = html2text.HTML2Text()
h2t.ignore_links = False
h2t.ignore_images = True
h2t.ignore_emphasis = False
h2t.body_width = 0
h2t.unicode_snob = True


def extract_from_p_tags(content_div) -> str:
    """Extract body content from p tags (standard structure)."""
    content_copy = BeautifulSoup(str(content_div), "html.parser")
    
    # Remove image containers
    for img in content_copy.find_all("img"):
        parent = img.find_parent(["span", "div"])
        if parent:
            parent.decompose()
        else:
            img.decompose()

    # Remove caption spans
    for span in content_copy.find_all("span"):
        class_str = str(span.get("class", ""))
        if "caption" in class_str.lower() or "MuiTypography" in class_str:
            text = span.get_text()
            if "Illustration" in text or "CypherStack" in text:
                span.decompose()

    body_html = ""
    for elem in content_copy.find_all(["p", "h2", "h3", "h4", "ul", "ol", "blockquote", "pre"]):
        # Skip nested elements
        if elem.find_parent(["p", "h2", "h3", "h4", "blockquote", "pre"]):
            continue
        
        # Skip empty elements
        if not elem.get_text(strip=True):
            continue

        # Skip related articles section
        if elem.name == "ul":
            links = elem.find_all("a", href=lambda x: x and "/knowledge/" in str(x))
            if links and len(links) > 5:
                break
        
        body_html += str(elem)
    
    return body_html


def extract_from_div_children(content_div) -> str:
    """Extract body content from direct div children (translated articles structure)."""
    body_html = ""
    skip_next = False
    
    for child in content_div.children:
        if not hasattr(child, 'name') or not child.name:
            continue
        
        # Skip hr tags
        if child.name == "hr":
            continue
        
        # Skip image containers
        if child.find("img"):
            continue
        
        text = child.get_text(strip=True)
        
        # Skip empty elements
        if not text:
            continue
        
        # Skip caption/credit
        if "Illustration" in text or "CypherStack" in text:
            continue
        
        # Stop at "Further reading" / "더 보기" section
        if text.startswith("더 보기") or text.startswith("Further reading"):
            break
        
        # Check if this is a heading (short text, likely a section title)
        if len(text) < 50 and not child.find(["a"]):
            # Convert to h2
            body_html += f"<h2>{text}</h2>"
        else:
            # Regular paragraph - wrap in p tag if it's a div
            if child.name == "div":
                body_html += f"<p>{child.decode_contents()}</p>"
            else:
                body_html += str(child)
    
    return body_html


def extract_content(html: str, slug: str, lang: str) -> dict | None:
    """Extract article content from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Find title
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
                # Find image credit
                credit_link = content_div.find("a", href=lambda x: x and "cypherstack" in str(x).lower())
                if credit_link:
                    image_credit = {
                        "text": credit_link.get_text(strip=True),
                        "url": credit_link.get("href", "")
                    }

    # Extract date - prefer meta tag, fall back to time element
    date = None
    
    # First try meta tag (most reliable)
    meta_date = soup.find("meta", {"property": "article:published_time"})
    if meta_date and meta_date.get("content"):
        raw_date = meta_date.get("content")
        try:
            # ISO format: 2020-02-01T00:00:00.000Z
            parsed = datetime.strptime(raw_date[:19], "%Y-%m-%dT%H:%M:%S")
            date = parsed.strftime("%Y-%m-%d")
        except ValueError:
            pass
    
    # Fall back to time element
    if not date:
        time_elem = soup.find("time")
        if time_elem:
            raw_date = time_elem.get("datetime", time_elem.get_text(strip=True))
            if raw_date:
                # Handle format: "Sat Feb 01 2020 00:00:00 GMT+0000 (Coordinated Universal Time)"
                # or standard formats
                formats = [
                    "%Y-%m-%dT%H:%M:%S.%fZ",
                    "%Y-%m-%d",
                    "%a %b %d %Y",  # Sat Feb 01 2020
                    "%d %B %Y %H:%M %Z",
                    "%d %B %Y"
                ]
                for fmt in formats:
                    try:
                        # Take only the date part for complex formats
                        date_part = raw_date.split(" GMT")[0].strip() if " GMT" in raw_date else raw_date.strip()
                        parsed = datetime.strptime(date_part[:len(datetime.now().strftime(fmt))], fmt)
                        date = parsed.strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        continue
    
    if not date:
        date = "2024-01-01"

    # Extract body - get all content from the paper div
    body_html = ""
    if content_div:
        # Strategy: Check if content is in p tags or in direct div children
        p_tags = content_div.find_all("p")
        # Filter out p tags that are just links
        real_p_content = [p for p in p_tags if len(p.get_text(strip=True)) > 50 and "/knowledge/" not in str(p)]
        
        if len(real_p_content) >= 3:
            # Content is in p tags (standard structure)
            body_html = extract_from_p_tags(content_div)
        else:
            # Content is in div children (translated articles structure)
            body_html = extract_from_div_children(content_div)

    return {
        "title": title,
        "slug": slug,
        "lang": lang,
        "date": date or "2024-01-01",
        "image": image_url,
        "image_credit": image_credit,
        "body_html": body_html
    }


def html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown."""
    if not html:
        return ""
    md = h2t.handle(html)
    # Clean up extra whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def replace_internal_links(markdown: str) -> str:
    """Replace internal /nojs/knowledge/ links with /knowledge/."""
    return re.sub(r'/nojs/knowledge/([^/\s"\']+)(/?)(?=["\'\)]|\s|$)', r'/knowledge/\1/', markdown)


def create_hugo_markdown(article: dict, image_filename: str | None) -> str:
    """Create Hugo-compatible markdown file content."""
    front_matter = {
        "title": article["title"],
        "slug": article["slug"],
        "date": article["date"],
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
    body_md = replace_internal_links(body_md)
    return "\n".join(yaml_lines) + body_md


def convert_file(html_file: Path, lang: str, downloaded_images: set) -> bool:
    """Convert a single HTML file to Markdown."""
    slug = html_file.stem

    try:
        html = html_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"    Error reading {html_file}: {e}")
        return False

    article = extract_content(html, slug, lang)
    if not article:
        print(f"    Failed to extract: {slug}.{lang}")
        return False

    # Handle image
    image_filename = None
    if article.get("image"):
        image_filename = os.path.basename(article["image"])
        downloaded_images.add(image_filename)

    # Create markdown
    markdown = create_hugo_markdown(article, image_filename)

    # Save to Hugo content
    output_file = HUGO_CONTENT_DIR / f"{slug}.{lang}.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(markdown, encoding="utf-8")

    return True


def main():
    """Convert all HTML files to Markdown."""
    if not RAW_HTML_DIR.exists():
        print(f"Error: Raw HTML directory not found: {RAW_HTML_DIR}")
        print("Run scrape_html.py first to download the HTML files.")
        return

    HUGO_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    HUGO_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    downloaded_images = set()
    success_count = 0
    fail_count = 0

    # Get all language directories
    lang_dirs = [d for d in RAW_HTML_DIR.iterdir() if d.is_dir()]

    for lang_dir in sorted(lang_dirs):
        lang = lang_dir.name
        html_files = list(lang_dir.glob("*.html"))

        print(f"\n[{lang}] Converting {len(html_files)} files...")

        for html_file in html_files:
            if convert_file(html_file, lang, downloaded_images):
                success_count += 1
            else:
                fail_count += 1

    print(f"\n✓ Conversion complete!")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Output: {HUGO_CONTENT_DIR}")


if __name__ == "__main__":
    main()
