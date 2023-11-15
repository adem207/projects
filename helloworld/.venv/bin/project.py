'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/skpatro/sel/chromedriver')
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://grasset.omnivox.ca/")
assert "QAVBOX" in driver.title
driver.find_element_by_name(By.LINK_TEXT, "SignUp Form").click()
driver.save_screenshot("/Users/skpatro/sel/test.png")
time.sleep(3)
driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
