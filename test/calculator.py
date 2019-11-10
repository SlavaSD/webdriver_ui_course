import random
import unittest
from time import sleep

from selenium import webdriver

class Calculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://www.math.com/students/calculators/source/basic.htm")

    def tearDown(self):
        self.driver.quit()


    def test_add_numbers(self):
        driver = self.driver
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        operator = random.choice(['+', ' -', 'x', ' /'])
        driver.find_element_by_css_selector('input[value="  {0}  "]'.format(num1)).click()
        sleep(0.5)
        driver.find_element_by_css_selector('input[value="  {0}  "]'.format(operator)).click()
        driver.find_element_by_css_selector('input[value="  {0}  "]'.format(num2)).click()
        sleep(0.5)
        driver.find_element_by_name('DoIt').click()
        sleep(0.5)
        result = driver.find_element_by_name('Input').get_attribute('value')

        if operator == '+':
            expected_result = num1 + num2
        elif operator == ' -':
            expected_result = num1 - num2
        elif operator == 'x':
            expected_result = num1 * num2
        else:
            if num2 is 0 and operator is " /":
                expected_result = "inf"
            else:
                expected_result = num1 / float(num2)



        self.assertEqual(expected_result, float(result))


if __name__ == '__main__':
    unittest.main()
