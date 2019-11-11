import unittest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ValidEmpSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver')
        self.driver.get('http://hrm-online.portnov.com/')

    def tearDown(self):
        self.driver.quit()

# 1) Go to hrm.seleniumminutes.com
# 2) Login: admin/Password
# 3) CLick the PIM tab in the top left corner
# 4) In the Employee Name field enter the name 'Smith'
# 5) Click the Search button
# 6) Check that the first row of the results table contains an employee with last name 'Smith'
# Hint: Don't forget to wait where appropriate!

    def test_something(self):
        driver = self.driver
        self.wait = WebDriverWait(self.driver, 2)
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()
        #driver.find_element_by_id('menu_pim_viewPimModule').click()
        sleep(0.5)
        driver.find_element_by_id('empsearch_employee_name_empName').send_keys('Smith')
        #self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'empsearch_employee_name_empName'))).send_keys('Smith')
        #self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'searchBtn'))).click()
        driver.find_element_by_id('searchBtn').click()
        result = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//tbody/tr/td[4]'))).text

        self.assertEqual("Smith", result)




if __name__ == '__main__':
    unittest.main()
