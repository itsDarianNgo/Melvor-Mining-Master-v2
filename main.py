# main.py

from src.browser_management.browser_init import setup_browser
from src.browser_management.navigate import navigate_to_homepage
from src.browser_management.login import login
from src.browser_management.character_select import select_character
from src.game_state_management.game_state import check_game_ready
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
        else:
            print("Game is not ready. Exiting.")
            return
    finally:
        browser.quit()


if __name__ == "__main__":
    main()
