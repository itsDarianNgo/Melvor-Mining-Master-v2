# main.py

from src.browser_management.browser_init import setup_browser
from src.browser_management.navigate import navigate_to_homepage
from src.browser_management.login import login
from src.browser_management.character_select import select_character
from src.game_state_management.game_state import check_game_ready
from src.mining_actions import mine_ore
from src.equipment_management import get_current_glove, equip_item
import config.settings as settings


def main():
    browser = setup_browser()
    try:
        navigate_to_homepage(browser, settings.GAME_URL)
        login(browser, settings.USERNAME, settings.PASSWORD)
        select_character(browser, settings.CHARACTER_NAME)

        # Check if the game is ready
        if check_game_ready(browser):
            print("Game is ready to proceed.")

            # Example usage of mining and equipment functions
            mine_ore(browser, "ore_local_id")  # Replace "ore_local_id" with the actual ID
            gloves_id = get_current_glove(browser)
            print("Current Gloves ID:", gloves_id)
            equip_item(browser, "item_local_id")  # Replace "item_local_id" with the actual ID
        else:
            print("Game is not ready. Exiting.")
            return
    finally:
        browser.quit()


if __name__ == "__main__":
    main()
