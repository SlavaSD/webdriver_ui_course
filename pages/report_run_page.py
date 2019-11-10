from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.params import DOMAIN
from pages.base_page import BasePage


class ReportRunPage(BasePage):

    def __init__(self, driver):
        super(ReportRunPage, self).__init__(driver)
        self.page_url = DOMAIN+'/symfony/web/index.php/core/displayPredefinedReport?reportId=492'



    def get_report_header(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.head h1'))).text

