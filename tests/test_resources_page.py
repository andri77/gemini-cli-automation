from playwright.sync_api import Page, expect
from pages.resources_page import ResourcesPage
from pages.home_page import HomePage

def test_resources_page_content(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.resources_link.click()

    resources_page = ResourcesPage(page)
    expect(resources_page.page_title).to_have_text("Resources")
    # Add more assertions for key elements on the page
