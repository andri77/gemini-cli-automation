import pytest
from applitools.playwright import Eyes, Target

class VisualBasePage:
    def __init__(self, page):
        self.page = page
        self.eyes = Eyes()
        self.eyes.api_key = "JzSuDNJApxPUitP3I4LBL7dPDcVmQ9w8peoE2PAEt108Q110"

    def open(self, app_name, test_name):
        self.eyes.open(self.page, app_name, test_name)

    def check(self, name, target):
        self.eyes.check(name, target)

    def close(self):
        self.eyes.close(False)