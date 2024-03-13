from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")
driver.maximize_window()

alertCount = 0
totalAlertTime = 0

start_time = time.time()
presence_time = 0
print(presence_time)
while presence_time < 30:
    current_time = time.time()
    presence_time = current_time - start_time

    print(f"Presence time: {presence_time} seconds")

    time.sleep(0.5)

    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/button')
    button.click()

    WebDriverWait(driver, 30).until(EC.alert_is_present())

    alertStartTime = time.time()

    WebDriverWait(driver, 30).until_not(EC.alert_is_present())

    alertTimer = time.time() - alertStartTime
    totalAlertTime += alertTimer

    alertCount+=1

    print(f"Time to Close Alert: {alertTimer} seconds")
    print(f"Alerts closed: {alertCount} alerts\n\n")

    
averageAlertTime = totalAlertTime / alertCount
print(f"Average Time to Close Alert: {averageAlertTime} seconds")
print(f"Total Alerts Closed: {alertCount}")

    


driver.quit()
