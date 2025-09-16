import pytest
from py.xml import html
from pytest_html import extras
import os
import shutil
import datetime
import base64
from pytest import StashKey

_test_results_by_type_key = StashKey[dict]()

# Global variable to store the screenshot directory
_screenshot_dir = None