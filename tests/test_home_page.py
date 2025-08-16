import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_for_schools_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_for_schools_link()
    expect(page).to_have_url("https://www.nap.edu.au/naplan/for-schools")

def test_privacy_policy_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    privacy_policy_link_href = home_page.get_privacy_policy_link_href()
    page.goto(privacy_policy_link_href)
    expect(page).to_have_url("https://www.acara.edu.au/contact-us/privacy")

def test_nap_logo_visibility_and_navigation(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(home_page.nap_logo).to_be_visible()
    home_page.nap_logo.click()
    expect(page).to_have_url("https://www.nap.edu.au/home")

def test_myschool_logo_visibility_and_navigation(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(home_page.myschool_logo).to_be_visible()
    # Since it opens in a new tab, we need to handle it
    with page.context.expect_page() as new_page_info:
        home_page.myschool_logo.click()
    new_page = new_page_info.value
    expect(new_page).to_have_url("https://www.myschool.edu.au/")

def test_australian_curriculum_logo_visibility_and_navigation(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(home_page.australian_curriculum_logo).to_be_visible()
    with page.context.expect_page() as new_page_info:
        home_page.australian_curriculum_logo.click()
    new_page = new_page_info.value
    expect(new_page).to_have_url("https://www.australiancurriculum.edu.au/")

def test_acara_logo_visibility_and_navigation(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(home_page.acara_logo).to_be_visible()
    with page.context.expect_page() as new_page_info:
        home_page.acara_logo.click()
    new_page = new_page_info.value
    expect(new_page).to_have_url("https://www.acara.edu.au/")