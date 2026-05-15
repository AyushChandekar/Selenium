from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "ipad"
driver.get(f"https://www.amazon.com/s?k={query}&crid=177R4MXG1YZPQ&sprefix=ip%2Caps%2C341&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME,"sg-col-inner")
print(elem.text)
print(elem.get_attribute("innerHTML"))




time.sleep(5)
driver.close()