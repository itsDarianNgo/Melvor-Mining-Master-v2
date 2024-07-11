# tests/test_equipment_management.py

import pytest
from selenium import webdriver
from src.browser_management.browser_init import setup_browser
from src.browser_management.navigate import navigate_to_homepage
from src.browser_management.login import login
from src.browser_management.character_select import select_character
from src.game_state_management.game_state import check_game_ready
from src.equipment_management.equipment_management import get_current_glove, equip_item
import config.settings as settings

@pytest.fixture(scope="module")
def browser():
    driver = setup_browser()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def setup_game(browser):
    navigate_to_homepage(browser, settings.GAME_URL)
    login(browser, settings.USERNAME, settings.PASSWORD)
    select_character(browser, settings.CHARACTER_NAME)
    if not check_game_ready(browser):
        pytest.fail("Game is not ready")

def test_get_current_glove(browser, setup_game):
    gloves_id = get_current_glove(browser)
    assert gloves_id is not None
    print("Current Gloves ID:", gloves_id)

def test_equip_item(browser, setup_game):
    item_name = "Gem_Gloves"  # Replace with actual item ID
    equip_item(browser, item_name)
