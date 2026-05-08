from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth


def create_browser(p):

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    stealth = Stealth()

    stealth.apply_stealth_sync(page)

    return browser, page