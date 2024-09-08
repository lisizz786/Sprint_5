import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.locators import MainPage, LkProfile, AuthLogin
from src.urls import Urls

class TestPersonalAccount:

    def test_navigation_to_personal_account(self, driver, get_login_driver):
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPage.profile_button))
        driver.find_element(*MainPage.profile_button).click()
        WebDriverWait(driver, 3).until(ec.url_to_be(Urls.profile_page_url))
        assert driver.current_url == Urls.profile_page_url


    def test_navigation_from_personal_account_to_constructor_success(self, driver, get_login_driver):
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(MainPage.profile_button))
        driver.find_element(*MainPage.profile_button).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LkProfile.constructor_button))
        driver.find_element(*LkProfile.constructor_button).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(MainPage.order_button))
        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.base_url and order_button.text == 'Оформить заказ'

    def test_click_through_to_the_constructor_logo_stellar_burgers_success(self, driver, get_login_driver):
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(MainPage.profile_button))
        driver.find_element(*MainPage.profile_button).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LkProfile.logo_element))
        driver.find_element(*LkProfile.logo_element).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(MainPage.profile_button))
        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.base_url and order_button.text == 'Оформить заказ'

    def test_logout_from_personal_account_success(self, driver, get_login_driver):
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(MainPage.profile_button))
        driver.find_element(*MainPage.profile_button).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LkProfile.logout_button))
        driver.find_element(*LkProfile.logout_button).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(AuthLogin.login_button))
        login_button = driver.find_element(*AuthLogin.login_button)
        assert driver.current_url == Urls.auth_page_url and login_button.text == 'Войти'
