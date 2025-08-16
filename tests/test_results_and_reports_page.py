from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.results_and_reports_page import ResultsAndReportsPage

def test_naplan_results_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_results_and_reports_link()

    results_and_reports_page = ResultsAndReportsPage(page)
    
    with page.context.expect_page() as new_page_info:
        results_and_reports_page.click_naplan_results_link()
    
    new_page = new_page_info.value
    expect(new_page).to_have_url("https://www.acara.edu.au/reporting/national-report-on-schooling-in-australia/naplan-national-results")
