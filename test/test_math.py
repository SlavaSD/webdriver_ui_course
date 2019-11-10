import unittest
from random import randint
from selenium import webdriver



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://www.math.com/students/calculators/source/basic.htm")

    def tearDown(self):
        self.driver.quit()


    def test_something(self):
        driver = self.driver
        button_locator = '[value="  {0}  "]'
        num1 = randint(0, 9)
        num2 = randint(0, 9)
        driver.find_element_by_css_selector(button_locator.format(num1)).click()
        driver.find_element_by_css_selector('input[name="plus"]').click()
        driver.find_element_by_css_selector(button_locator.format(num2)).click()
        driver.find_element_by_css_selector('input[name="DoIt"]').click()
        result_of_calculation = driver.find_element_by_name('Input').get_attribute('value')

        messege = "Result should be '{0}' but instead we've got '{1}'"
        self.assertEqual(str(num1+num2), result_of_calculation, messege.format(str(num1+num2), result_of_calculation))
        print (messege.format(str(num1+num2), result_of_calculation))


if __name__ == '__main__':
    unittest.main()
