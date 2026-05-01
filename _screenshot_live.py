import os
import glob
from playwright.sync_api import sync_playwright

BASE_URL = "https://halfmoon.advancedmarketing.co"
BASE_DIR = r"C:\Users\HP\halfmoon-rebuilt"
OUTPUT_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_pages():
    html_files = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
    pages = []
    for f in sorted(html_files):
        if os.path.basename(f).startswith("_"):
            continue
        rel = os.path.relpath(f, BASE_DIR).replace("\\", "/")
        url = f"{BASE_URL}/{rel}"
        name = rel.replace("/", "_").replace(".html", "")
        pages.append((url, name))
    return pages

def main():
    pages = get_pages()
    print(f"Found {len(pages)} pages to screenshot from live site")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1440, "height": 900})

        for url, name in pages:
            try:
                page = context.new_page()
                print(f"Screenshot: {name}")
                page.goto(url, wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(1500)

                # Full page
                path = os.path.join(OUTPUT_DIR, f"{name}_full.png")
                page.screenshot(path=path, full_page=True)

                # Above fold
                path2 = os.path.join(OUTPUT_DIR, f"{name}_abovefold.png")
                page.screenshot(path=path2, full_page=False)

                page.close()
            except Exception as e:
                print(f"  ERROR on {name}: {e}")

        browser.close()

    print(f"\nDone! Screenshots saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
