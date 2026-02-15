from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver


def test_valid_login():
    driver = setup_driver()

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    assert "Logged In Successfully" in driver.page_source
    driver.quit()


def test_invalid_login():
    driver = setup_driver()

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPass")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    assert "Your password is invalid!" in driver.page_source
    driver.quit()


def test_empty_login():
    driver = setup_driver()

    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    assert "Your username is invalid!" in driver.page_source
    driver.quit()
