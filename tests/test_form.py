import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/login"

@allure.title("Тест авторизации")
@allure.description("Авторизация с валидными данными на сайте "
                    "https://the-internet.herokuapp.com/login")
def test_successful_login(driver):
    """Успешная авторизация"""
    with allure.step("Открыть страницу авторизации"):
        driver.get(BASE_URL)

    with allure.step("Дождаться элементов формы и найти поля и кнопку"):
        wait = WebDriverWait(driver, 20)

        username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    with allure.step("Ввести логин и пароль, нажать кнопку входа"):
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_btn.click()

    with allure.step("Дождаться сообщения об успехе и проверить текст"):
        wait = WebDriverWait(driver, 10)
        flash_msg = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#flash-messages .success"))
        )
        assert "You logged into a secure area!" in flash_msg.text

@allure.title("Тест неудачной авторизации")
@allure.description("Авторизация с невалидными данными на сайте "
                    "https://the-internet.herokuapp.com/login")
def test_unsuccessful_login(driver):
    """Неудачная авторизация (неверный логин)"""
    with allure.step("Открыть страницу авторизации"):
        driver.get(BASE_URL)

    with allure.step("Дождаться элементов формы и найти поля и кнопку"):
        wait = WebDriverWait(driver, 20)
        username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    with allure.step("Ввести неверные данные и нажать кнопку входа"):
        username.send_keys("wrong-user")
        password.send_keys("SuperSecretPassword!")
        login_btn.click()
    with allure.step("Дождаться сообщения об ошибке и проверить текст"):
        wait = WebDriverWait(driver, 10)
        flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash-messages")))

        assert "username is invalid" in flash_msg.text