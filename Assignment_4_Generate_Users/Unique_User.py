from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import re
def keywordCounter(driver, keyword)->int:
    return len(re.findall(f'(?=({keyword.lower()}))', driver.page_source.lower()))


driver = webdriver.Chrome()
driver.maximize_window()

rewardTime = 1
keyword = "game"


# Website with keyword
driver.get("http://localhost:3000/")
totalRewardTime = keywordCounter(driver, keyword) * rewardTime
time.sleep(totalRewardTime)
print("Page 1: " + str(totalRewardTime) + " seconds")

driver.get("http://localhost:3000/blank")
totalRewardTime = keywordCounter(driver, keyword) * rewardTime
time.sleep(totalRewardTime)
print("Page 2: " + str(totalRewardTime) + " seconds")

driver.quit()
