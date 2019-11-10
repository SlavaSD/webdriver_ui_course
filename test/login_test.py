import unittest
from selenium import webdriver
from steps.common import login, get_welcome_message


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.driver = webdriver.Chrome(executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")
        driver = self.driver
        login(driver)
    # Epxected value vs. Actual value
        self.assertEqual("Welcome Admin", get_welcome_message(driver))

    def tearDown(self):
        self.driver.quit()

    # def test_invalid_login(self):
    #     driver = self.driver
    #     driver.find_element_by_id("txtUsername").send_keys("admin")
    #     driver.find_element_by_id("txtPassword").send_keys("Password")
    #     driver.find_element_by_id("btnLogin").click()
    #     warning_text = driver.find_element_by_id("spanMessage").text
    #
    #     sleep(2)
    #     # Epxected value vs. Actual value
    #     self.assertEqual(warning_text, "Invalid credentials")


    # def test_invalid_login(self):
    #     driver = self.driver
    #     driver.find_element_by_id("txtUsername").send_keys("admin")
    #     driver.find_element_by_id("txtPassword").send_keys("Password")
    #     driver.find_element_by_id("btnLogin").click()
    #     welcome_text = driver.find_element_by_id("spanMessage").text
    #     self.assertEqual(welcome_text, "Invalid credentials")




    # def test_invalid_login(self):
    #     driver = self.driver
    #     driver.find_element_by_id("txtUsername").send_keys("admin")
    #     driver.find_element_by_id("txtPassword").send_keys("")
    #     driver.find_element_by_id("btnLogin").click()
    #
    #     welcome_text = driver.find_element_by_id("spanMessage").text
    #     sleep(5)
    #     self.assertEqual("Password cannot be empty", welcome_text)




if __name__ == '__main__':
    unittest.main()
