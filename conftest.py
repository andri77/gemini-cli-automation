import pytest
from py.xml import html
from pytest_html import extras
import os
import shutil
import datetime

# Global variable to store the screenshot directory
_screenshot_dir = None

def pytest_sessionstart(session):
    """
    Called after the Session object has been created and before performing collection and entering the run test loop.
    """
    global _screenshot_dir
    # Create a unique temporary directory for screenshots
    _screenshot_dir = os.path.join(session.config.rootdir, "screenshots", datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(_screenshot_dir, exist_ok=True)
    print(f"Screenshots will be saved to: {_screenshot_dir}")

def pytest_sessionfinish(session):
    """
    Called after whole test run finished, right before returning the exit status to the system.
    """
    global _screenshot_dir
    if _screenshot_dir and os.path.exists(_screenshot_dir):
        # Optionally, you might want to keep screenshots if tests failed
        # For now, we'll always clean up
        # shutil.rmtree(_screenshot_dir)
        print(f"Screenshots saved in: {_screenshot_dir}")


def pytest_collection_modifyitems(items):
    for item in items:
        if "API/tests/" in str(item.fspath):
            if "test_security.py" in str(item.fspath):
                item.add_marker(pytest.mark.security)
            else:
                item.add_marker(pytest.mark.api)
        elif "tests/" in str(item.fspath):
            item.add_marker(pytest.mark.ui)
        elif "perf/tests/" in str(item.fspath):
            item.add_marker(pytest.mark.performance)

def pytest_html_results_summary(prefix, summary, postfix):
    # This hook can be used to add custom content to the summary section of the HTML report.
    # We will use it later to inject our charts.
    pass

def pytest_html_results_table_header(cells):
    # This hook can be used to add custom columns to the results table header.
    cells.insert(1, html.th("Test Type"))

    # Find and swap 'Duration' and 'Links' headers
    duration_index = -1
    links_index = -1
    for i, cell in enumerate(cells):
        if hasattr(cell, 'text'):
            if cell.text == "Duration":
                duration_index = i
            elif cell.text == "Links":
                links_index = i

    if duration_index != -1 and links_index != -1:
        cells[duration_index], cells[links_index] = cells[links_index], cells[duration_index]

def pytest_html_results_table_row(report, cells):
    # This hook can be used to add custom data to the results table rows.
    test_type = "N/A"
    if hasattr(report, 'keywords'):
        if 'security' in report.keywords:
            test_type = "Security"
        elif 'api' in report.keywords:
            test_type = "API"
        elif 'ui' in report.keywords:
            test_type = "UI"
        elif 'performance' in report.keywords:
            test_type = "Performance"
    cells.insert(1, test_type)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots for UI tests after each test run.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and hasattr(item, 'callspec') and 'page' in item.funcargs:
        # Check if it's a UI test
        if 'ui' in item.keywords:
            page = item.funcargs['page']
            screenshot_name = f"{item.name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot_path = os.path.join(_screenshot_dir, screenshot_name)
            try:
                page.screenshot(path=screenshot_path)
                # Attach screenshot to the report
                html_path = os.path.relpath(screenshot_path, os.path.dirname(report.nodeid))
                if hasattr(report, 'extra'):
                    report.extra.append(extras.png(page.screenshot(path=screenshot_path), f"Screenshot: {screenshot_name}"))
                else:
                    report.extra = [extras.png(page.screenshot(path=screenshot_path), f"Screenshot: {screenshot_name}")]
            except Exception as e:
                print(f"Failed to take screenshot for {item.name}: {e}")
