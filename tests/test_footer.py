from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_copyright_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    page.get_by_role("link", name="Copyright and terms of use").click()
    expect(page).to_have_url("https://www.nap.edu.au/copyright")

def test_accessibility_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    page.locator("//div[@class='divcopyright']//a[normalize-space()='Accessibility']").click()
    expect(page).to_have_url("https://www.nap.edu.au/accessibility")
