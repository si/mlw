from playwright.sync_api import sync_playwright
import time

def run_cuj(page):
    # Test an episode with both title and intro defined
    page.goto("http://localhost:4000/dan-blundell/")
    page.wait_for_timeout(500)

    og_title = page.locator('meta[property="og:title"]').get_attribute("content")
    og_desc = page.locator('meta[property="og:description"]').get_attribute("content")

    print(f"dan-blundell og:title: {og_title}")
    print(f"dan-blundell og:description: {og_desc}")

    assert og_title == "Make Life Work with Dan Blundell"

    # Let's test Ian Lurie which does have an intro
    page.goto("http://localhost:4000/ian-lurie/")
    page.wait_for_timeout(500)

    og_title_ian = page.locator('meta[property="og:title"]').get_attribute("content")
    og_desc_ian = page.locator('meta[property="og:description"]').get_attribute("content")

    print(f"ian-lurie og:title: {og_title_ian}")
    print(f"ian-lurie og:description: {og_desc_ian}")

    assert og_title_ian == "From CEO to individual contributor with Ian Lurie"
    assert "The one when Si talks to Ian" in og_desc_ian

    # Test the fallback on a tag page
    page.goto("http://localhost:4000/tag/fundraising/")
    page.wait_for_timeout(500)

    og_title_fallback = page.locator('meta[property="og:title"]').get_attribute("content")
    og_desc_fallback = page.locator('meta[property="og:description"]').get_attribute("content")

    print(f"fallback og:title: {og_title_fallback}")
    print(f"fallback og:description: {og_desc_fallback}")

    assert og_title_fallback == "fundraising | Make Life Work Podcast"
    assert og_desc_fallback == "Talking to people around tech about how they balance work life balance with any side projects"

    page.screenshot(path="verification_metadata.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
