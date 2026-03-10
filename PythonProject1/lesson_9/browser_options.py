import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager" #normal
# chrome_options.add_argument("--headless") # Безголовый режим
# chrome_options.add_argument("--incognito") # Режим Инкогнито
# chrome_options.add_argument("--ignore-certificate-errors") # Игнорирование ошибок сертификатов
chrome_options.add_argument("--window-size=700,700") # Изменение разрешения окна
# chrome_options.add_argument("--disable-cache") # Отключение кеша
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()

driver.get("https://whatismyipaddress.com/")

end_time = time.time()
result = end_time - start_time
print(result)
