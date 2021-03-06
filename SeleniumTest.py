from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get("https://www.books.com.tw/")
print(driver.title)

search = driver.find_element_by_name("key")
search.send_keys("aimer")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchlist"))
        )

    searchlist = main.find_elements_by_tag_name("a")
    for item in searchlist:
        if "aimer" in str(item.text).lower():
            print(item.text)
            link = driver.find_element_by_link_text(item.text)
            link.click()
    time.sleep(5)

finally:
    driver.quit()
