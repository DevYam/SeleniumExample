from selenium import webdriver
import time

email = 'admin@ncertguruji.com'
pwd = 'admin'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.ncertguruji.com/downloads/login.php')

user = driver.find_element_by_name('username')
user.send_keys(email)

password = driver.find_element_by_name('password')
password.send_keys(pwd)

time.sleep(5)
button = driver.find_element_by_xpath('/html/body/form/div[3]/button')
button.click()

time.sleep(10)





