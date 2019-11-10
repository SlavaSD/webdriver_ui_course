from fixtures.params import DOMAIN
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = DOMAIN +"/symfony/web/index.php/auth/login"

    def login(self, username='admin', password='password'):
        driver = self.driver

        if driver.current_url.find('seleniumminutes') >= 0 and username == 'admin':
            password = password.title()
        driver.find_element_by_id("txtUsername").send_keys(username)
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnLogin").click()