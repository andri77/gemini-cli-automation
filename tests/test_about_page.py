from playwright.sync_api import Page, expect
from pages.about_page import AboutPage
from pages.home_page import HomePage

def test_about_page_content(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.about_link.click()

    about_page = AboutPage(page)
    expect(about_page.page_title).to_have_text("About")
    # Add more assertions for key elements on the page
