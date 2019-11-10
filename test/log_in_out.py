import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from steps.common import login, get_welcome_message, logout


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.driver = webdriver.Chrome(executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")
        driver = self.driver
        login(driver)
        get_welcome_message(driver)
        self.assertEqual("Welcome Admin", get_welcome_message(driver))
        logout(driver)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
