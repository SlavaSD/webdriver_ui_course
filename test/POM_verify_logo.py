import unittest
from time import sleep
from fixtures.base import AdminLoginTestCase


class MyTestCase(AdminLoginTestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()


    def tearDown(self):
        super(MyTestCase, self).tearDown()

    def test_logo_size_and_location(self):
        driver = self.driver

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
