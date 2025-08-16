from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.for_schools_link = page.get_by_role("link", name="For schools").first
        self.privacy_policy_link = page.locator("//div[@class='divcopyright']//a[normalize-space()='Privacy policy']")

    def navigate(self):
        self.page.goto("https://www.nap.edu.au/naplan/public-demonstration-site")

    def click_for_schools_link(self):
        self.for_schools_link.click()

    def get_privacy_policy_link_href(self):
        return self.privacy_policy_link.get_attribute("href")
