import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Ищем по сайту https://hyperskill.org/courses элементы через Xpath

# Logo = (//div[@class = '!flex !items-center'])

# Catalog = (//div//a[contains(text(), 'Catalog')])

# Pricing = ((//div//a[contains(text(), 'Pricing')])[1])

# Python Developer card = ((//div[@class = 'card-body'])[1])



