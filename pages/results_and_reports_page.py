from playwright.sync_api import Page

class ResultsAndReportsPage:

    def __init__(self, page: Page):
        self.page = page
        self.naplan_results_link = page.get_by_role("link", name="NAPLAN national results").first

    def click_naplan_results_link(self):
        self.naplan_results_link.click()
