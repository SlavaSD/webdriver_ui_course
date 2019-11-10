import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.login_page import LoginPage


class HomeWork(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")
        self.login_page = LoginPage(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        driver = self.driver
        self.login_page.login()
        driver.find_element_by_class_name("firstLevelMenu").click()
        driver.find_element_by_id("menu_admin_Configuration").click()
        driver.find_element_by_id("menu_admin_localization").click()
        driver.find_element_by_id("btnSave").click()
        Select(driver.find_element_by_id("localization_dafault_language")).select_by_visible_text("Chinese - China")
        driver.find_element_by_id("btnSave").click()
        header1 = driver.find_element_by_id("localizationHeading").text

        self.assertFalse(header1 == "Localization")
        driver.find_element_by_id("btnSave").click()
        Select(driver.find_element_by_id("localization_dafault_language")).select_by_visible_text("US English")
        driver.find_element_by_id("btnSave").click()
        header2 = driver.find_element_by_id("localizationHeading").text
        self.assertEqual("Localization", header2)



if __name__ == '__main__':
    unittest.main()
