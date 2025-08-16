from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.results_and_reports_page import ResultsAndReportsPage

def test_naplan_results_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_results_and_reports_link()

    results_and_reports_page = ResultsAndReportsPage(page)
    results_and_reports_page.click_naplan_results_link()

    expect(results_and_reports_page.naplan_results_link).to_be_visible()
