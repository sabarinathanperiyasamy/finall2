import pytest

from newone.pages.homepage import Homepage
from newone.pages.leavepage import Leavepage
from newone.pages.loginpage import Loginpage
from newone.pages.profile_page import profile_page
from newone.pages.profile_search import profile_search
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        driver.implicitly_wait(500)
        log = Loginpage(driver)
        log.username(utils.USERNAME)
        log.password(utils.PASSWORD)
        log.submit()

    def test_leave(self):
        driver = self.driver
        lve = Leavepage(driver)
        lve.lve_func(utils.name, utils.dde, utils.fde, utils.ct)

    def test_profile(self):
        driver = self.driver
        profile = profile_search(driver)
        profile.prof_func(utils.emp_id)

    def test_profile(self):
        driver = self.driver
        prof = profile_page(driver)
        prof.profile_func()

    def test_logout(self):
        driver = self.driver
        home = Homepage(driver)
        home.welcome()
        home.logout()
