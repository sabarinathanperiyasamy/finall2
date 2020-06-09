import selenium.webdriver.support.ui
from selenium.webdriver.support.ui import WebDriverWait

from locators.locators import locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.wel_var = locator.wel_var
        self.logout_1 = locator.logout_1
        self.wait = WebDriverWait(driver, 30)

    def welcome(self):
        self.driver.element = self.wait.until(EC.element_to_be_clickable((By.ID, self.wel_var)))
        self.driver.element.click()

    def logout(self):
        self.driver.element1 = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.logout_1)))
        self.driver.element1.click()
