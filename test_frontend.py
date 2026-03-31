from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Load an episode page that has an image
    page.goto("http://localhost:4000/dan-blundell/")
    page.wait_for_timeout(500)

    # We want to check the og:image meta tag in the head.
    # Since it's a meta tag, we can extract its content via JS evaluation or use a selector.
    og_image = page.locator('meta[property="og:image"]').get_attribute("content")
    print(f"dan-blundell og:image: {og_image}")
    assert og_image == "/images/uploads/S01/Dan-Blundell.png"

    # Load a tag page which should use the fallback image
    page.goto("http://localhost:4000/tag/fundraising/")
    page.wait_for_timeout(500)

    og_image_fallback = page.locator('meta[property="og:image"]').get_attribute("content")
    print(f"tag page og:image: {og_image_fallback}")
    assert og_image_fallback == "/images/design/make-life-work-square.png"

    page.screenshot(path="verification.png")

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
