from playwright.sync_api import Page

class ForSchoolsPage:

    def __init__(self, page: Page):
        self.page = page
        self.national_protocols_link = page.get_by_role("link", name="National protocols for test administration").first

    def click_national_protocols_link(self):
        self.national_protocols_link.click()
