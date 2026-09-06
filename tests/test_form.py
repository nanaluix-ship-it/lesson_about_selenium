from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com/login"

def test_successful_login(driver):
    """Успешная авторизация"""
    driver.get(BASE_URL)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_btn.click()

    wait = WebDriverWait(driver, 10)
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash-messages")))

    assert "You logged into a secure area!" in flash_msg.text


def test_unsuccessful_login(driver):
    """Неудачная авторизация (неверный логин)"""
    driver.get(BASE_URL)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Вводим неверные данные
    username.send_keys("wrong-user")
    password.send_keys("SuperSecretPassword!")
    login_btn.click()

    wait = WebDriverWait(driver, 10)
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash-messages")))

    # 👇 ИСПРАВЛЕНИЕ ЗДЕСЬ 👇
    # Сайт пишет "invalid", а не "incorrect". Также там есть символ крестика и перенос строки.
    assert "username is invalid" in flash_msg.text