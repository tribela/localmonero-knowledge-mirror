#!/usr/bin/env python3
"""
Scrape LocalMonero knowledge articles and save raw HTML.
"""

import asyncio
import os
import re
from pathlib import Path

import httpx

BASE_URL = "https://localmonero.co"
KNOWLEDGE_URL = f"{BASE_URL}/nojs/knowledge"
OUTPUT_DIR = Path(__file__).parent.parent / "raw_html"
TIMEOUT = httpx.Timeout(30.0)
REQUEST_DELAY = 0.5
MAX_CONCURRENT = 2

LANGUAGES = [
    "en", "ko",
    "ar", "bg", "cs", "da", "de", "el", "es", "fi", "fr", "ha", "hi", "hu", "id", "it",
    "ja", "lt", "lv", "nb", "nl", "pl", "pt-br", "ro", "ru", "sk", "sl", "so", "sv",
    "sw", "tl", "tr", "ur", "zh-cn", "zh-tw"
]


def is_error_page(html: str) -> bool:
    """Check if the response is an error page."""
    error_indicators = [
        "429 Too Many Requests",
        "Too Many Requests",
        "Rate limit exceeded",
        "Please try again later",
        "<title>Error</title>",
    ]
    return any(indicator in html for indicator in error_indicators)


async def fetch_page(client: httpx.AsyncClient, url: str, lang: str = None) -> str | None:
    """Fetch a page with retry logic."""
    max_retries = 5
    base_delay = 2

    params = {"language": lang} if lang and lang != "en" else None
    headers = {"Accept-Language": lang} if lang else {"Accept-Language": "en"}

    for attempt in range(max_retries):
        try:
            client.cookies = httpx.Cookies()
            await asyncio.sleep(REQUEST_DELAY)
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

    slugs = []
    for match in re.finditer(r'/nojs/knowledge/([a-z0-9-]+)"', html):
        slug = match.group(1)
        if slug not in slugs:
            slugs.append(slug)

    print(f"Found {len(slugs)} articles")
    return slugs


async def scrape_article(client: httpx.AsyncClient, slug: str, lang: str, semaphore: asyncio.Semaphore) -> bool:
    """Scrape a single article and save raw HTML."""
    async with semaphore:
        output_file = OUTPUT_DIR / lang / f"{slug}.html"

        if output_file.exists():
            return True

        url = f"{KNOWLEDGE_URL}/{slug}"
        html = await fetch_page(client, url, lang)

        if not html:
            print(f"    Failed: {slug} ({lang})")
            return False

        if is_error_page(html):
            print(f"    Error page: {slug} ({lang})")
            return False

        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(html, encoding="utf-8")
        print(f"    Saved: {slug}.{lang}.html")
        return True


async def main():
    """Main scraping function."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with httpx.AsyncClient(timeout=TIMEOUT, http2=False) as client:
        slugs = await get_article_slugs(client)

        total = len(slugs) * len(LANGUAGES)
        print(f"\nScraping {len(slugs)} articles x {len(LANGUAGES)} languages = {total} pages")

        semaphore = asyncio.Semaphore(MAX_CONCURRENT)

        for i, slug in enumerate(slugs, 1):
            print(f"\n[{i}/{len(slugs)}] {slug}")

            tasks = [
                scrape_article(client, slug, lang, semaphore)
                for lang in LANGUAGES
            ]
            await asyncio.gather(*tasks)

    print("\n✓ Scraping complete!")
    print(f"  Raw HTML saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
