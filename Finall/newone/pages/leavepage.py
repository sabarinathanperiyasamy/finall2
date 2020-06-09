from locators.locators import locator
from selenium.webdriver.support.ui import Select
import time


class Leavepage:

    def __init__(self, driver):
        self.driver = driver
        self.lve_link = locator.lve_link
        self.emp_name = locator.emp_name
        self.l_typ = locator.l_typ
        self.f_date = locator.f_date
        self.t_date = locator.t_date
        self.cmt = locator.cmt
        self.calender = locator.calender
        self.lbtn =locator.lbtn

    def lve_func(self, name, dde, fde, ct):
        self.driver.find_element_by_xpath(self.lve_link).click()
        self.driver.find_element_by_name(self.emp_name).click()
        self.driver.find_element_by_name(self.emp_name).send_keys(name)
        add = Select(self.driver.find_element_by_id(self.l_typ))
        add.select_by_index(1)
        self.driver.find_element_by_name(self.f_date).clear()
        self.driver.find_element_by_name(self.f_date).send_keys(fde)
        self.driver.find_element_by_name(self.t_date).clear()
        self.driver.find_element_by_name(self.t_date).send_keys(dde)
        self.driver.find_element_by_id(self.cmt).send_keys(ct)
        self.driver.find_element_by_xpath(self.calender).click()
        self.driver.find_element_by_id(self.lbtn).click()





