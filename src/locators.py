from selenium.webdriver.common.by import By


class MainPage:
    profile_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    login_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    current_list_item = (By.XPATH, ".//div[contains(@class, 'current')]/span")
    bread_list = (By.XPATH, ".//span[contains(text(), 'Булки')]")
    sauces_list = (By.XPATH, ".//span[contains(text(), 'Соусы')]")
    topping_menu = (By.XPATH, ".//span[contains(text(), 'Начинки')]")


class AuthLogin:
    email_input = (By.XPATH, ".//input[@name = 'name']")
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")
    login_button = (By.XPATH, "//button[text() = 'Войти']")


class AuthRegistre:
    name_field = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")
    email_field = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    password_field = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    register_button = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']")
    incorrect_password_error_message = (By.XPATH, ".//p[text() = 'Некорректный пароль']")


class LkProfile:
    logout_button = (By.XPATH, ".//button[text() = 'Выход']")
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")
    logo_element = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")
