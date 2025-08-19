from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.google.com")
        
        # Handle consent popup if it appears
        if page.locator("button:has-text('I agree')").is_visible():
            page.click("button:has-text('I agree')")
        
        # Fill search box
        page.wait_for_selector("textarea[name='q']")
        page.fill("textarea[name='q']", "AI Automation Testing")
        page.press("textarea[name='q']", "Enter")
        
        page.wait_for_timeout(2000)  # wait for results
        title = page.title()
        browser.close()
        
        assert "AI" in title
