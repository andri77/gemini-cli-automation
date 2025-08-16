from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_for_schools_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_for_schools_link()
    expect(page).to_have_url("https://www.nap.edu.au/naplan/for-schools")

def test_privacy_policy_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    privacy_policy_link_href = home_page.get_privacy_policy_link_href()
    page.goto(privacy_policy_link_href)
    expect(page).to_have_url("https://www.acara.edu.au/contact-us/privacy")
