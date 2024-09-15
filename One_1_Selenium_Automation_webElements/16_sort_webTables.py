import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.firefox.service import Service
# driver = wd.Chrome()
# driver = wd.Edge()
# driver = wd.Firefox()

browser = "chrome"
driver = ""
if browser.lower() == "chrome".lower():
    url = Service(r"/webdrivers/chromedriver-win64/chromedriver.exe")
    driver = wd.Chrome(service=url)
elif browser.lower() == "edge".lower():
    url = Service(r"/webdrivers/edgedriver_win64/msedgedriver.exe")
    driver = wd.Edge(service=url)
# elif browser.lower() == "firefox".lower():
#     url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")
#     driver = wd.Firefox(service=url)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
print()
print(driver.title)
print(driver.current_url)
print()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='Top Deals']")))
driver.find_element(By.XPATH, "//*[text()='Top Deals']").click()

no_of_windows = driver.window_handles
driver.switch_to.window(no_of_windows[1])

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//tr//th//span[text()='Veg/fruit name']")))
list_of_items = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")

unsorted_items = []
for item in list_of_items:
    unsorted_items.append(item.text)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//tr//th//span[text()='Veg/fruit name']/following-sibling::*")))
driver.find_element(By.XPATH, "//tr//th//span[text()='Veg/fruit name']/following-sibling::*").click()
sorted_list_of_items = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")

sorted_items = []
for item in sorted_list_of_items:
    sorted_items.append(item.text)

print(sorted(unsorted_items))
print(sorted_items)
assert sorted_list_of_items != unsorted_items

time.sleep(3)
driver.quit()
