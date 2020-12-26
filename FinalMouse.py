from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://aimgods.finalmouse.com/goldenKey")
assert "AimGods" in driver.title
elem = driver.find_element_by_id("username")
elem.clear()
elem.send_keys("UserNameGuy") # This is a placeholder for the username
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys("Password123!") # This is a placeholder for the password
elem.send_keys(Keys.RETURN)
time.sleep(2)
driver.get("https://aimgods.finalmouse.com/goldenKey")
time.sleep(2)
f = True
while f:
    try:
        elem = driver.find_element_by_class_name("RewardsSlider__ToggleButton-bckp7e-7")
        elem.click()
        time.sleep(14)
        try:
            elem = driver.find_element_by_class_name("WonReward__ClaimRewardButton-m8yu6l-12")
            elem.click()
        except:
            time.sleep(1)
    except:
        time.sleep(1)
