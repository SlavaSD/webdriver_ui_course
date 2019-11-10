import unittest
from time import sleep

from selenium import webdriver




class verify_logo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/admin/Desktop/HRM_Summer2019/browser_drivers/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList")


    def tearDown(self):
        self.driver.quit()


    def test_something(self):
        driver = self.driver
        driver.find_element_by_xpath('//input[@ id="txtUsername"]').send_keys('admin')
        driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        sleep(2)

        logo_element = driver.find_element_by_css_selector('#branding > img')
        logo_size = logo_element.size


        self.assertEqual(56, logo_size.get('height'))
        # self.assertEqual(283, logo_size.get('width'))
        self.assertTrue(logo_size.get('width')==283)
        self.assertDictEqual({'width': 283, 'height': 56}, logo_size)

        window_size = driver.get_window_size()
        logo_locatin = logo_element.location

        top_right_logo_corner_x_location = logo_size.get('width') + logo_locatin.get('x')
        self.assertTrue(top_right_logo_corner_x_location < (window_size.get('width') / 2))



if __name__ == '__main__':
    unittest.main()
