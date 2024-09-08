import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import MainPage, AuthLogin, AuthRegistre
from src.data import User
from src.urls import Urls


class TestLogin:

    def test_button_log_personal_account_success(self, open_base_url, driver):

        driver.find_element(*MainPage.profile_button).click()
        driver.find_element(*AuthLogin.email_input).send_keys(User.email)
        driver.find_element(*AuthLogin.password_input).send_keys(User.password)
        driver.find_element(*AuthLogin.login_button).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.order_button))

        assert driver.find_element(*MainPage.order_button).is_displayed()

    def test_button_log_login_in_to_account_success(self, open_base_url, driver):

        driver.find_element(*MainPage.login_button).click()
        driver.find_element(*AuthLogin.email_input).send_keys(User.email)
        driver.find_element(*AuthLogin.password_input).send_keys(User.password)
        driver.find_element(*AuthLogin.login_button).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.order_button))

        assert driver.find_element(*MainPage.order_button).is_displayed()

    def test_log_using_registration_form_success(self, open_reg_page, driver):

        driver.find_element(*AuthRegistre.login_account_button).click()
        driver.find_element(*AuthLogin.email_input).send_keys(User.email)
        driver.find_element(*AuthLogin.password_input).send_keys(User.password)
        driver.find_element(*AuthLogin.login_button).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.order_button))

        assert driver.find_element(*MainPage.order_button).is_displayed()

    def test_log_recover_form_success(self, driver):

        driver.get(Urls.forgot_page_url)
        driver.find_element(*AuthRegistre.login_account_button).click()
        driver.find_element(*AuthLogin.email_input).send_keys(User.email)
        driver.find_element(*AuthLogin.password_input).send_keys(User.password)
        driver.find_element(*AuthLogin.login_button).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.order_button))

        assert driver.find_element(*MainPage.order_button).is_displayed()


