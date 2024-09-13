import time

from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser = "edge"
driver = ""

if browser.lower() == "chrome".lower():
    url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\chromedriver-win64\chromedriver.exe")
    driver = wd.Chrome(service=url)
elif browser.lower() == "edge".lower():
    url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\edgedriver_win64\msedgedriver.exe")
    driver = wd.Edge(service=url)

driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

expected_list = ["capsicum", "apple", "grapes"]
extracted_list = []

driver.find_element(By.XPATH, "//*[@type='search']").send_keys("ap")
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='product']")))

products = driver.find_elements(By.XPATH, "//div[@class='product']//h4")

for product in products:
    item = product.text.split(" ")[0]
    extracted_list.append(item.lower())

print(expected_list)
print(extracted_list)

time.sleep(5)
driver.quit()
