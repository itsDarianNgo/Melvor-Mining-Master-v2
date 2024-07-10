# src/browser_management/login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def login(browser, username, password):
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for login to complete and dashboard to load
    time.sleep(5)
