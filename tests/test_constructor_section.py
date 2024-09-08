from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import MainPage
from src.urls import Urls

class TestConstructorSection:

    def test_switch_to_bread_in_constructor_success(self, open_base_url, driver):

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.sauces_list))
        driver.find_element(*MainPage.sauces_list).click()
        driver.find_element(*MainPage.bread_list).click()

        assert driver.find_element(*MainPage.current_list_item).text == 'Булки'

    def test_switch_to_sauces_in_constructor_success(self, open_base_url, driver):

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.sauces_list))
        driver.find_element(*MainPage.sauces_list).click()

        assert driver.find_element(*MainPage.current_list_item).text == 'Соусы'

    def test_switch_to_topping_in_constructor_success(self, open_base_url, driver):

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPage.topping_menu))
        driver.find_element(*MainPage.topping_menu).click()

        assert driver.find_element(*MainPage.current_list_item).text == 'Начинки'
