import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

wikipedia = driver.find_element("class name", "wikipedia-icon")

print("Иконка:", wikipedia)

time.sleep(3)

wikipediaid = driver.find_element("id", "Wikipedia1_wikipedia-search-input")

print("Айди поля Википедии:", wikipediaid)

time.sleep(3)

searchbutton = driver.find_element("class name", "wikipedia-search-button")

print("Кнопка поиска Википедии:", searchbutton)

time.sleep(3)

element = driver.find_element("tag name", "div")
print("Тэг: ", element)

time.sleep(3)