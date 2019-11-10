import unittest
from random import randint
from time import sleep
import faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.select import Select
from steps.common import get_welcome_message, login


class AddEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")


    def tearDown(self):
        self.driver.quit()

    # Login
    def test_something(self):
        empId = randint(100000,999999)
        user = "User"+str(empId)
        user_exp_pass = "Passw0rd"
        expected_job_title = "QA Manager"
        expected_employment_status = "Full Time"
        data = faker.Faker()
        expected_first_name = data.first_name()
        expected_last_name = data.last_name()
        self.wait = WebDriverWait(self.driver, 2)
        driver = self.driver
        login(driver)
        welcome_text = get_welcome_message(driver)
        self.assertEqual("Welcome Admin", welcome_text)
        sleep(2)



    # Click the Add button
        #driver.find_element_by_id("btnAdd").click()
        #self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "btnAdd"))).click()
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, "btnAdd"))).click()
        # todo SS may need to come back later
        # Enter First Lastname
        driver.find_element_by_id("firstName").send_keys(expected_first_name)
        driver.find_element_by_id("lastName").send_keys(expected_last_name)
        # Enter and remember the empID
        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys(empId)
        driver.find_element_by_id("chkLogin").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "user_name"))).send_keys(user)
        driver.find_element_by_id("user_password").send_keys(user_exp_pass)
        driver.find_element_by_id("re_password").send_keys(user_exp_pass)
        # Save the Employee
        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_link_text("Job").click()
        # todo SS: may need sleep
        driver.find_element_by_id("btnSave").click()
        # todo SS: may need sleep
        Select(driver.find_element_by_id("job_job_title")).select_by_visible_text(expected_job_title)
        Select(driver.find_element_by_id("job_emp_status")).select_by_visible_text(expected_employment_status)
        driver.find_element_by_id('btnSave').click()

        # Go to PIM page
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_pim_viewEmployeeList").click()
        # todo may need to do something as well
        # Search by EmpID
        driver.find_element_by_id("empsearch_id").send_keys(empId)
        driver.find_element_by_id("searchBtn").click()

        # Logout

    # Expected: 1 record back
    #     lst = driver.find_elements_by_xpath("//td[3]/a")
    #     self.assertTrue(len(lst) == 1)
    #
    #
    # # Expected Correct Name and EmpID
    #     firstName = driver.find_element_by_xpath("//td[3]/a").text
    #     lastName = driver.find_element_by_xpath("//td[4]").text
    #     job_title = driver.find_element_by_xpath("//td[5]").text
    #     employment_status = driver.find_element_by_xpath("//td[6]").text
    #
    #     message = "Expected the table to contain first name '{0}' but instead the value was '{1}'"
    #     self.assertEqual(expected_first_name, firstName, message.format(expected_first_name, firstName))
    #     self.assertEqual(expected_last_name, lastName)
    #     self.assertEqual(expected_job_title, job_title)
    #     self.assertEqual(expected_employment_status, employment_status)
    #



if __name__ == '__main__':
    unittest.main()
