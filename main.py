from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

EMAIL = os.environ['lnd_email']
PASSWORD = os.environ['lnd_password']

chrome_driver_path = r'C:\Users\pluus\dev_stuff\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_PP=101832192&f_WT=1%2C2%2C3&keywords=python%20developer&sortBy=R')
log_button = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
log_button.click()

login = driver.find_element(By.XPATH, '//*[@id="username"]')
login.send_keys(EMAIL)
password_space = driver.find_element(By.XPATH, '//*[@id="password"]' )
password_space.send_keys(PASSWORD)
log_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
log_in.click()

offers = driver.find_elements(By.CLASS_NAME, "job-flavors__flavor")
for offer in offers:
    offer.click()
    time.sleep(5)
    button = driver.find_element(By.CLASS_NAME, 'jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary')
    button.click()
