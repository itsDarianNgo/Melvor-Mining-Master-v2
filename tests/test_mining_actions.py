# tests/test_mining_actions.py

import unittest
from selenium import webdriver
from src.browser_management.browser_init import setup_browser
from src.browser_management.navigate import navigate_to_homepage
from src.browser_management.login import login
from src.browser_management.character_select import select_character
from src.game_state_management.game_state import check_game_ready
from src.mining_actions.mining_actions import mine_ore
import config.settings as settings


class TestMiningActions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = setup_browser()
        navigate_to_homepage(cls.browser, settings.GAME_URL)
        login(cls.browser, settings.USERNAME, settings.PASSWORD)
        select_character(cls.browser, settings.CHARACTER_NAME)
        if not check_game_ready(cls.browser):
            raise Exception("Game is not ready")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_mine_ore(self):
        ore_name = "Copper_Ore"  # Replace with actual ore ID
        mine_ore(self.browser, ore_name)


if __name__ == "__main__":
    unittest.main()
