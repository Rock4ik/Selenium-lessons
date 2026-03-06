import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print('Переходим на страницу...')

driver.get('http://the-internet.herokuapp.com/status_codes')

time.sleep(5)

links = driver.find_elements("xpath", '//li//a')

for i in range(len(links)):
    current_links = driver.find_elements("xpath", "//li/a")
    current_links[i].click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
