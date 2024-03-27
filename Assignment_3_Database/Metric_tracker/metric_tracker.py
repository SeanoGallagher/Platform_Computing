from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import mysql.connector

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")
driver.maximize_window()

alertCount = 0
totalAlertTime = 0

start_time = time.time()
presence_time = 0
print(presence_time)
time.sleep(0.5)

while presence_time <= 10:
    current_time = time.time()
    presence_time = current_time - start_time

    print(f"Presence time: {presence_time} seconds")

    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/button')
    button.click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alertStartTime = time.time()

    WebDriverWait(driver, 10).until_not(EC.alert_is_present())

    alertTimer = time.time() - alertStartTime
    totalAlertTime += alertTimer

    alertCount += 1

    print(f"Time to Close Alert: {alertTimer} seconds")
    print(f"Alerts closed: {alertCount} alerts\n\n")
    
averageAlertTime = totalAlertTime / alertCount
print(f"Average Time to Close Alert: {averageAlertTime} seconds")
print(f"Total Alerts Closed: {alertCount}")

mydb = mysql.connector.connect(
  host="localhost",
  user="Platform_Computing",
  password='Coyote',
  database="Platform_DB"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Metric_Tracker (Average_Alert_Time, Alert_Count) VALUES (%s, %s)"
val = (round(averageAlertTime, 2), alertCount)
mycursor.execute(sql, val)

mydb.commit()

driver.quit()
