from locators.locators import locator


class profile_search:

    def __init__(self, driver):
        self.driver = driver
        self.pim = locator.pim_path
        self.emp_id = locator.emp_id
        self.search = locator.search

    def prof_func(self, emp_id):
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_xpath(self.pim).click()
        self.driver.find_element_by_name(self.emp_id).clear()
        self.driver.find_element_by_name(self.emp_id).send_keys(emp_id)
        self.driver.find_element_by_id(self.search).click()


