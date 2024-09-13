import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

# from selenium.webdriver.firefox.service import Service

# driver = wd.Chrome()
# driver = wd.Edge()
# driver = wd.Firefox()

browser = "edge"
driver = ""
if browser.lower() == "chrome".lower():
    url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\chromedriver-win64\chromedriver.exe")
    driver = wd.Chrome(service=url)
elif browser.lower() == "edge".lower():
    url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\edgedriver_win64\msedgedriver.exe")
    driver = wd.Edge(service=url)
# elif browser.lower() == "firefox".lower():
#     url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")
#     driver = wd.Firefox(service=url)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print()
print(driver.title)
print(driver.current_url)
time.sleep(3)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("melon")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(driver.find_elements(By.XPATH, "//div[@class='product']"))
print(count)
assert count > 0

for result in results:
    result.find_element(By.CSS_SELECTOR,"button[type='button']").click()
    time.sleep(1)

time.sleep(3)

driver.find_element(By.XPATH, "//input[@type='search']").clear()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("berry")
time.sleep(4)
results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(driver.find_elements(By.XPATH, "//div[@class='product']"))
print(count)
assert count > 0

for result in results:
    result.find_element(By.CSS_SELECTOR,"button[type='button']").click()
    time.sleep(1)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(text(),'CHECKOUT')]").click()


time.sleep(3)
driver.close()
