from playwright.sync_api import sync_playwright

from browser import create_browser


TEST_URL = "https://www.topcv.vn/viec-lam/data-engineer-middle-senior/2114998.html?ta_source=JobSearchList_LinkDetail&u_sr_id=oWjxn5H0Nt19uDBhfTPYpnamoDlq59YeSBekykzE_1778255368"


with sync_playwright() as p:

    browser, page = create_browser(p)

    page.goto(TEST_URL)

    page.wait_for_timeout(8000)

    body_text = page.locator("body").inner_text()

    print(body_text[:3000])

    browser.close()