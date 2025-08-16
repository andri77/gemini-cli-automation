from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.for_schools_link = page.get_by_role("link", name="For schools").first
        self.privacy_policy_link = page.locator("//div[@class='divcopyright']//a[normalize-space()='Privacy policy']")
        self.results_and_reports_link = page.get_by_role("link", name="Results and reports").first
        self.nap_logo = page.locator("a[href='/home'] img[title='NAP']")
        self.myschool_logo = page.locator("a[href='https://www.myschool.edu.au/'] img[title='MySchool']")
        self.australian_curriculum_logo = page.locator("a[href='http://www.australiancurriculum.edu.au/'] img[title='Australian Curriculum']")
        self.acara_logo = page.locator("a[href='http://www.acara.edu.au/'] img[title='Acara']")
        self.home_link = page.get_by_role("link", name="Home").first
        self.about_link = page.get_by_role("link", name="About").first
        self.naplan_link = page.get_by_role("link", name="NAPLAN").first
        self.nap_sample_assessments_link = page.get_by_role("link", name="NAP sample assessments").first
        self.opt_in_link = page.get_by_role("link", name="NAP Opt-in").first
        self.resources_link = page.get_by_role("link", name="Resources").first
        self.contacts_link = page.get_by_role("link", name="Contacts").first

    def navigate(self):
        self.page.goto("https://www.nap.edu.au/naplan/public-demonstration-site")

    def click_for_schools_link(self):
        self.for_schools_link.click()

    def get_privacy_policy_link_href(self):
        return self.privacy_policy_link.get_attribute("href")

    def click_results_and_reports_link(self):
        self.results_and_reports_link.click()
