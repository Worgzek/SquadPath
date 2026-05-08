from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

from browser import create_browser

URL = "https://www.topcv.vn/tim-viec-lam-data-engineer-cr257cb261cl285?category_family=r257~b261l285"


with sync_playwright() as p:

    browser, page = create_browser(p)

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

    print(job_data[:1])

    browser.close()