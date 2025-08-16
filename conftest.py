import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    screenshot_option = item.config.getoption("--screenshot")

    if rep.when == "call" and rep.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            if screenshot_option == "on" or screenshot_option == "only-on-failure":
                page.screenshot(path=f"screenshots/{item.name}.png")
    elif rep.when == "call" and screenshot_option == "on":
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            page.screenshot(path=f"screenshots/{item.name}.png")
