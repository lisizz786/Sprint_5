import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import MainPage, AuthLogin
from src.data import User
from src.urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def open_base_url(driver):
    driver.get(Urls.base_url)


@pytest.fixture
def open_reg_page(driver):
    driver.get(Urls.reg_page_url)


@pytest.fixture
def get_login_driver(driver):
    driver.get(Urls.base_url)
    driver.find_element(*MainPage.profile_button).click()
    driver.find_element(*AuthLogin.email_input).send_keys(User.email)
    driver.find_element(*AuthLogin.password_input).send_keys(User.password)
    driver.find_element(*AuthLogin.login_button).click()
