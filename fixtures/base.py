import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT, CHROME_EXECUTABLE_PATH, DOMAIN
from pages.login_page import LoginPage
from steps.common import login


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)

    def tearDown(self):
        self.driver.quit()


class AdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(AdminLoginTestCase, self).setUp()
        self.driver.get("http://hrm-online.portnov.com/")
        login(self.driver)

    def tearDown(self):
        super(AdminLoginTestCase, self).tearDown()


class POMAdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(POMAdminLoginTestCase, self).setUp()
        self.driver.get(DOMAIN)
        self.login = LoginPage(self.driver)
        self.login.login()

    def tearDown(self):
        super(POMAdminLoginTestCase, self).tearDown()


if __name__ == '__main__':
    unittest.main()



