import time

from selenium import webdriver
from trio import current_time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com/")

current_title = driver.title
print("Текущий заголовок:", current_title)

time.sleep(3)

driver.get("https://ya.ru/")

current_title = driver.title
print("Текущий заголовок:", current_title)

time.sleep(3)

driver.back()

url = driver.current_url
assert url == "https://vk.com/", "Ошибка в URL, открыта не та страница"

time.sleep(3)

driver.refresh()

time.sleep(3)

print("URL страницы:", url)

driver.forward()

url = driver.current_url
assert url == "https://ya.ru/", "Ошибка в URL, открыта не та страница"

time.sleep(3)

print("URL страницы:", url)