from playwright.sync_api import Page

class ContactsPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator("#contentmain h1")

    def navigate(self):
        self.page.goto("https://www.nap.edu.au/contacts")
