from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "drone"
driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

elems = driver.find_elements(By.CLASS_NAME,"jIjQ8S")
print(f"{len(elems)} items found")

for elem in elems:
    print(elem.text)
# print(elem.get_attribute("innerHTML"))




time.sleep(2)
driver.close()