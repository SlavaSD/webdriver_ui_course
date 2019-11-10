import unittest
from time import sleep

from fixtures.base import POMAdminLoginTestCase
from pages.main_menu import MainMenu
from pages.pim_page import PIMPage


class MenuTestCase(POMAdminLoginTestCase):
    def test_localization_menu(self):
        # pim_page = PIMPage(self.driver)
        # pim_page.main_menu.select_localization()

        main_main = MainMenu(self.driver)
        main_main.select_localization()
        # checking the Header
        self.assertEqual("Localization", self.driver.find_element_by_id("localizationHeading").text)

        # checking the URL
        self.assertTrue(self.driver.current_url.find("localization") > 0)


    def test_my_info_menu(self):
        driver = self.driver
        menu = MainMenu(driver)
        sleep(1)
        menu.select_my_info()
        # checking the Header
        # the correct way would be to create MyInfoPage instance and then call get_header() function
        self.assertEqual("Personal Details", self.driver.find_element_by_css_selector('.head h1').text)

        driver.set_window_size(200, 300)



        # This should result in a WebDriverException "unknown error ... element is not clickable"
        #driver.find_element_by_link_text('Job').click()

        # let's use execute_comamand to fake click it
        # driver.execute_script("document.querySelector('#sidenav > li:nth-child(6) > a').click()")
        driver.execute_script("arguments[0].click()", driver.find_element_by_link_text('Job'))
        self.assertEqual("Job", self.driver.find_element_by_css_selector('.head h1').text)




if __name__ == '__main__':
    unittest.main()
