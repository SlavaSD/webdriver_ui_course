import unittest
from random import randint

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import login, is_element_present


class ReportTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")

    def tearDown(self):
        driver = self.driver
        if self.report_name:
            driver.find_element_by_id("menu_pim_viewPimModule").click()
            driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()

            driver.find_element_by_id("search_search").send_keys(self.report_name)
            driver.find_element_by_class_name("searchBtn").click()

            driver.find_element_by_xpath("//td[text()= " + str('"' + self.report_name + '"') + "]/../td[1]").click()
            driver.find_element_by_id("btnDelete").click()

            self.wait.until(EC.visibility_of_element_located((By.ID, "dialogDeleteBtn"))).click()

        self.driver.quit()

    def test_create_and_remove_report(self):
        driver = self.driver
        report_name = ("rep" + str(randint(1, 3)))
        self.wait = WebDriverWait(driver, 2)
        login(driver)
        # click on the report tab
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()
        # click on the Add button
        driver.find_element_by_css_selector('input[value="Add"]').click()
        # enter unique Report name
        self.wait.until(
            EC.presence_of_element_located((By.ID, "report_report_name"))).send_keys(report_name)
        # select Criteria = Job Title
        Select(driver.find_element_by_id("report_criteria_list")).select_by_visible_text("Job Title")
        driver.find_element_by_id("btnAddConstraint").click()
        # select display field group = Personal
        Select(driver.find_element_by_id("report_display_groups")).select_by_visible_text("Personal")
        driver.find_element_by_id("btnAddDisplayGroup").click()
        # make sure to check the checkbox and save
        self.wait.until(EC.visibility_of_element_located((By.ID, 'display_group_1'))).click()
        driver.find_element_by_id("btnSave").click()
        # verify that report was created
        self.assertTrue(is_element_present(driver, By.XPATH, "//td[text()='{0}']/../td[3]/a".format(report_name)))
        # report was created
        self.report_name = report_name
        # run the report
        driver.find_element_by_xpath("//td[text()='{0}']/../td[3]/a".format(report_name)).click()
        # verify the report
        report_header = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.head h1'))).text
        self.assertEqual('Report Name : {0}'.format(report_name), report_header)
        # actual_result = driver.find_element_by_xpath('//*[@id="search-results"]/div[1]/h1').text
        # search_result = driver.find_element_by_xpath("//*[contains(text(),'Report Name :\"unique_report_name\"')]")
        # driver.find_element_by_xpath("//h1[text()='{0}']".format(expected_report)).is_displayed()
        # driver.find_element_by_xpath("//h1[contains(text(), 'Report Name : " + report_name + "')]").is_displayed()
        # message = "Expected the table to contain report na
        # self.assertEqual(expected_first_name, firstName, m
        # self.assertEqual(expected_report, actual_result)


if __name__ == '__main__':
    unittest.main()
