import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

first_name = driver.find_element("xpath", "//input[@id='userName']")
email = driver.find_element("xpath", "//input[@id='userEmail']")
address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
permanentAddress = driver.find_element("xpath", "//textarea[@id='permanentAddress']")

first_name.clear()
email.clear()
address.clear()
permanentAddress.clear()

time.sleep(3)

#проверяем поля пустые
assert first_name.get_attribute("value") == ""
assert email.get_attribute("value") == ""
assert address.get_attribute("value") == ""
assert permanentAddress.get_attribute("value") == ""

time.sleep(3)

first_name.send_keys("Alexey")
email.send_keys("scadasADE@gmail.com")
address.send_keys("fejfef, sefsf")
permanentAddress.send_keys("dsdqwfdqwdqdd1")

time.sleep(3)

assert "Alexey" in first_name.get_attribute("value")
assert "scadasADE@gmail.com" in email.get_attribute("value")
assert "fejfef, sefsf" in address.get_attribute("value")
assert "dsdqwfdqwdqdd1" in permanentAddress.get_attribute("value")

time.sleep(3)


