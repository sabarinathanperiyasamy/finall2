from locators import locators


class profile_page:
    def __init__(self, driver):
        self.driver = driver

    def profile_func(self):
        self.driver.find_element_by_partial_link_text("0002").click()
        self.driver.find_element_by_xpath("//*[@id='empPic']").click()
        self.driver.find_element_by_xpath("//*[@id='photofile']").send_keys("D://test/testimage.jpg")
        self.driver.find_element_by_id("btnSave").click()
