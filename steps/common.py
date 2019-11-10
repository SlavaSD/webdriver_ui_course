from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

    # login
def login(driver, username='admin', password='password'):
    if driver.current_url.find('seleniumminutes') >= 0 and username == 'admin':
        password = password.title()
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    # get welcome message
def get_welcome_message(driver):
    return WebDriverWait(driver, 25).until(
        expected_conditions.presence_of_element_located((By.ID, "welcome"))).text

    # logout
def logout(driver):
    driver.find_element_by_id("welcome").click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()


def is_element_present(driver, by, locator):
    try:
        driver.find_element(by, locator)
    except NoSuchElementException:
        return False
    return True