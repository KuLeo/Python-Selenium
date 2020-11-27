from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id(
    "productPrice" + str(i)) for i in range(1, -1, -1)
    ]

actcion = ActionChains(driver)
actcion.click(cookie)

for i in range(5000):
    actcion.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()
