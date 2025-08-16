from playwright.sync_api import Page, expect
from pages.contacts_page import ContactsPage
from pages.home_page import HomePage

def test_contacts_page_content(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.contacts_link.click()

    contacts_page = ContactsPage(page)
    expect(contacts_page.page_title).to_have_text("Contacts")
    # Add more assertions for key elements on the page
