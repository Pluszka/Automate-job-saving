from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r'C:\Users\pluus\dev_stuff\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_PP=101832192&f_WT=1%2C2%2C3&keywords=python%20developer&sortBy=R')
log_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
log_in.click()