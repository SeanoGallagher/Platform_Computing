from selenium import webdriver

import time

def findKeyword(driver, keyword)->bool:
    return keyword.lower() in driver.page_source.lower()

driver = webdriver.Chrome()
driver.maximize_window()

rewardTime = 10
keyword = "Gallagher"

# Website with keyword
driver.get("http://localhost:3000/")
totalRewardTime = 0
if findKeyword(driver, keyword):
    totalRewardTime += rewardTime
    time.sleep(rewardTime)
print("Page 1: " + str(totalRewardTime))


driver.get("http://localhost:3000/blank")
totalRewardTime = 0
if findKeyword(driver, keyword):
    totalRewardTime += rewardTime
    time.sleep(rewardTime)
print("Page 2: " + str(totalRewardTime))

driver.quit()
