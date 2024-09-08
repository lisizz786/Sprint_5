import pytest
from src.data import TestUser
from src.locators import AuthRegistre
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.urls import Urls


@pytest.mark.registration
def test_successful_registration(driver, open_reg_page):

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthRegistre.name_field)).send_keys(
        TestUser.user_name)
    driver.find_element(*AuthRegistre.email_field).send_keys(TestUser.email)
    driver.find_element(*AuthRegistre.password_field).send_keys(TestUser.password)

    driver.find_element(*AuthRegistre.register_button).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(Urls.auth_page_url))
    assert driver.current_url == Urls.auth_page_url


def test_registration_with_invalid_password_error(driver, open_reg_page):

    driver.find_element(*AuthRegistre.name_field).send_keys(TestUser.user_name)
    driver.find_element(*AuthRegistre.email_field).send_keys(TestUser.email)
    driver.find_element(*AuthRegistre.password_field).send_keys('short')
    driver.find_element(*AuthRegistre.register_button).click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(AuthRegistre.incorrect_password_error_message)
    )

    error_message = driver.find_element(*AuthRegistre.incorrect_password_error_message).text

    assert error_message == 'Некорректный пароль', f"Expected 'Некорректный пароль', but got '{error_message}'"
    assert driver.current_url == Urls.reg_page_url, f"Expected URL '{Urls.reg_page_url}', but got '{driver.current_url}'"

