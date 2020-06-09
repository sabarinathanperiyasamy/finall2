from locators.locators import locator


class Loginpage:

    def __init__(self, driver):
        self.driver = driver

        self.username_locators = locator.username_locators
        self.password_locators = locator.password_locators
        self.submit_locators = locator.submit_locators

    def username(self, user_name):
        self.driver.find_element_by_id(self.username_locators).clear()
        self.driver.find_element_by_id(self.username_locators).send_keys(user_name)

    def password(self, pass_word):
        self.driver.find_element_by_id(self.password_locators).clear()
        self.driver.find_element_by_id(self.password_locators).send_keys(pass_word)

    def submit(self):
        self.driver.find_element_by_name("Submit").click()
