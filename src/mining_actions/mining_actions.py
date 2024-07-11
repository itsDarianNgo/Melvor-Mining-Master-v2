# src/mining_actions.py

import json
from selenium.common.exceptions import StaleElementReferenceException
import time
import textwrap


def retry(func, retries=3, delay=1):
    for i in range(retries):
        try:
            return func()
        except StaleElementReferenceException:
            if i < retries - 1:
                time.sleep(delay)
            else:
                raise


def mine_ore(driver, ore_name):
    """
    Initiate mining of a specified ore and verify mining has started.
    Args:
        driver: The Selenium WebDriver instance.
        ore_name: The local ID of the ore to be mined.
    """
    script = textwrap.dedent("""
        function startMiningSpecifiedRock(rock) {
            if (typeof game !== 'undefined' && game.mining) {
                if (rock) {
                    game.mining.onRockClick(rock);
                    console.log('Mining initiated for rock:', rock._localID);
                    return rock.currentHP;
                } else {
                    console.log('No rock object provided.');
                    return null;
                }
            } else {
                console.log('Game or mining object is not available');
                return null;
            }
        }

        function selectRockByProperty(property, value) {
            if (typeof game !== 'undefined' && game.mining) {
                const rocks = game.mining.actionQueryCache;
                for (let [rock, rockDetails] of rocks) {
                    if (rock && rock[property] === value) {
                        return rock;
                    }
                }
            }
            return null;
        }

        function mineRockByProperty(property, value) {
            const selectedRock = selectRockByProperty(property, value);
            if (selectedRock) {
                return startMiningSpecifiedRock(selectedRock);
            } else {
                console.log(`No available rock found with ${property}: ${value}`);
                return null;
            }
        }

        return mineRockByProperty('_localID', arguments[0]);
    """)
    initial_hp = retry(lambda: driver.execute_script(script, ore_name))
    if initial_hp is not None:
        time.sleep(2)  # Wait for some time to see the mining effect
        current_hp = driver.execute_script("return game.mining.selectedRock.currentHP")
        if current_hp < initial_hp:
            print(f"Mining started successfully. Initial HP: {initial_hp}, Current HP: {current_hp}")
        else:
            raise AssertionError("Mining did not start as expected.")
    else:
        raise AssertionError("Failed to select and mine the specified rock.")
