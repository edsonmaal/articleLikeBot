from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

for x in range(3):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.selenium.dev/documentation/")
    search = driver.find_element_by_link_text("WebDriver")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(search, 5, 5)
    action.click()
    action.perform()
    driver.quit()