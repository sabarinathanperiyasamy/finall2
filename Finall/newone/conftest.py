import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(executable_path="C://Users//Dell//PycharmProjects//Finall//tessst//chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
