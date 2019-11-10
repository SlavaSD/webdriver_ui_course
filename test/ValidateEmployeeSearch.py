import unittest
from selenium import webdriver
from time import sleep


class ValidEmpSrch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver')
        self.driver.get('http://hrm-online.portnov.com/')

    def tearDown(drv):
        drv.driver.quit()

# 1) Go to hrm.seleniumminutes.com
# 2) Login: admin/Password
# 3) CLick the PIM tab in the top left corner
# 4) In the Employee Name field enter the name 'Smith'
# 5) Click the Search button
# 6) Check that the first row of the results table contains an employee with last name 'Smith'
# Hint: Don't forget to wait where appropriate!

    def test_something(drv):
        drv = drv.driver
        drv.find_element_by_id('txtUsername').send_keys('admin')
        drv.find_element_by_id('txtPassword').send_keys('password')
        drv.find_element_by_id('btnLogin').click()
        drv.find_element_by_id('menu_pim_viewPimModule').click()
        drv.find_element_by_id('empsearch_employee_name_empName').send_keys('Smith')
        drv.find_element_by_id('searchBtn').click()






        drv.assertEqual(True, False)




if __name__ == '__main__':
    unittest.main()
