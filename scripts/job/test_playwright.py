from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup

URL = "https://www.topcv.vn/tim-viec-lam-data-engineer-cr257cb261cl285?category_family=r257~b261l285"

with sync_playwright() as p:

    # =========================
    # START BROWSER
    # =========================

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    stealth = Stealth()

    stealth.apply_stealth_sync(page)

    # =========================
    # STEP 1: SCRAPE LISTING PAGE
    # =========================

    print("Opening listing page...")

    page.goto(URL)

    page.wait_for_timeout(8000)

    html = page.content()

    soup = BeautifulSoup(html, "html.parser")

    h3_tags = soup.find_all("h3")

    job_data = []

    for tag in h3_tags:

        a_tag = tag.find("a")

        if a_tag:

            title = a_tag.get_text(strip=True)

            url = a_tag.get("href")

            job_data.append({
                "title": title,
                "url": url
            })

    print("\n=== JOBS FOUND ===\n")

    for job in job_data[:5]:
        print(job)

    # =========================
    # STEP 2: OPEN DETAIL PAGE
    # =========================

    test_url = job_data[0]["url"]

    print("\nOpening detail page...\n")
    print(test_url)

    page.goto(test_url)

    page.wait_for_timeout(8000)

    # =========================
    # DEBUG TEXT CONTENT
    # =========================

    body_text = page.locator("body").inner_text()

    print("\n=== PAGE TEXT ===\n")

    print(body_text[:5000])

    # =========================
    # GET HTML AFTER FULL RENDER
    # =========================

    detail_html = page.content()

    detail_soup = BeautifulSoup(detail_html, "html.parser")

    # save prettified html
    with open("detail.html", "w", encoding="utf-8") as f:
        f.write(detail_soup.prettify())

    print("\n=== PAGE TITLE ===\n")

    print(detail_soup.title.text)

    input("\nPress Enter to close browser...")

    browser.close()