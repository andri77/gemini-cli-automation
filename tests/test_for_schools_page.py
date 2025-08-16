from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.for_schools_page import ForSchoolsPage

def test_national_protocols_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_for_schools_link()

    for_schools_page = ForSchoolsPage(page)
    for_schools_page.click_national_protocols_link()

    expect(page).to_have_url("https://www.nap.edu.au/naplan/for-schools/national-protocols-for-test-administration")
