import time

from selenium import webdriver
from trio import current_time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Шпаргалка по WebElement
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/gb/login")

time.sleep(5)

driver.find_element("id", "loginformsubmit").click()

time.sleep(3)