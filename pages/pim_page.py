from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from fixtures.params import DOMAIN
from pages.base_page import BasePage

class PIMPage(BasePage):

    def __init__(self, driver):
        super(PIMPage, self).__init__(driver)
        self.page_url = DOMAIN+'/symfony/web/index.php/pim/viewEmployeeList'

    def goto_reports(self):
        #self.wait.until(expected_conditions.presence_of_element_located((By.ID, "menu_pim_viewPimModule"))).click()
        #driver.find_element_by_id("menu_pim_viewPimModule").click()
        #self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'menu_core_viewDefinedPredefinedReports'))).click()
        self.driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()
