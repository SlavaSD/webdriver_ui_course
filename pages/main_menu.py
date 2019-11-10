from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT


class MainMenu(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)
        self.action = ActionChains(self.driver)

    def select_localization(self):
        driver = self.driver

        admin_menu = driver.find_element_by_id('menu_admin_viewAdminModule')
        # We can call self.action one line at a time.
        self.action.move_to_element(admin_menu)
        # OR we can use a variable and we can chain multiple commands.
        self.action.move_to_element(
            driver.find_element_by_id('menu_admin_UserManagement')
        ).move_to_element(
            driver.find_element_by_id('menu_admin_Configuration')
        ).click(driver.find_element_by_id('menu_admin_localization')
        ).perform()

    def select_my_info(self):
        self.driver.find_element_by_id('menu_pim_viewMyDetails').click()

