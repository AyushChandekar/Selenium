from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# scrapping data from flipkart into html for range of pages
driver = webdriver.Chrome()
query = "asus"
file = 0
for i in range (1,5):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")

    elems = driver.find_elements(By.CLASS_NAME,"jIjQ8S")
    print(f"{len(elems)} items found")

    for elem in elems:
        print(elem.text)
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w",encoding ='utf-8') as f:
            f.write(d)
            file += 1   
    # print(elem.get_attribute("innerHTML"))



time.sleep(2)
driver.close()