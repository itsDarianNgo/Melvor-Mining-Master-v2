# src/browser_management/character_select.py

from selenium.webdriver.common.by import By
import time


def select_character(browser, character_name):
    character_button = browser.find_element(By.XPATH, f"//button[contains(text(), '{character_name}')]")
    character_button.click()

    # Wait for character to load
    time.sleep(5)
