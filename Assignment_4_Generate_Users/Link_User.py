from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def countElem(driver, tag)->int:
    return len(driver.find_elements(By.TAG_NAME, tag))

def findKeyword(driver, keyword)->bool:
    return keyword.lower() in driver.page_source.lower()

driver = webdriver.Chrome()
driver.maximize_window()

rewardTime = 10
keyword = "Gallagher"
tag1 = "a"
tag2 = "img"

# Website with keyword
driver.get("http://localhost:3000/")
totalRewardTime = 0
totalRewardTime += rewardTime * countElem(driver, tag1)
totalRewardTime += rewardTime * countElem(driver, tag2)
if findKeyword(driver, keyword):
    totalRewardTime += 10
time.sleep(totalRewardTime)
print("Page 1: " + str(totalRewardTime) + " seconds")

driver.get("http://localhost:3000/blank")
totalRewardTime = 0
totalRewardTime += rewardTime * countElem(driver, tag1)
totalRewardTime += rewardTime * countElem(driver, tag2)
if findKeyword(driver, keyword):
    totalRewardTime += 10
time.sleep(totalRewardTime)
print("Page 1: " + str(totalRewardTime) + " seconds")

driver.quit()
