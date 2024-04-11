from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def countElem(driver, tag)->int:
    return len(driver.find_elements(By.TAG_NAME, tag))


driver = webdriver.Chrome()
driver.maximize_window()

rewardTime = 10
tag = "img"

# Website with keyword
driver.get("http://localhost:3000/")
totalRewardTime = 0
elems = countElem(driver, tag)
totalRewardTime += rewardTime * elems
time.sleep(totalRewardTime)
print("Page 1: " + str(totalRewardTime) + " seconds")

driver.get("http://localhost:3000/blank")
totalRewardTime = 0
elems = countElem(driver, tag)
totalRewardTime += rewardTime * elems
time.sleep(totalRewardTime)
print("Page 2: " + str(totalRewardTime) + " seconds")

driver.quit()
