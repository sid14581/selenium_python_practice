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

browser = "chrome"
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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print()
print(driver.title)
print(driver.current_url)
time.sleep(3)

# STATIC DROPDOWN
dropdown = Select(driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency"))
dropdown.select_by_index(2)
time.sleep(3)
dropdown.select_by_value("INR")
time.sleep(3)
dropdown.select_by_visible_text("USD")
time.sleep(3)

# DYNAMIC DROPDOWN
driver.find_element(By.CSS_SELECTOR, "#select-class-example  input#autosuggest").send_keys("IND")
time.sleep(3)

# CSS SELECTOR
# countries1 = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item *[class='ui-corner-all']")
# for country in list(countries1):
#     print(country.text)
# print()

# XPATH
countries2 = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
for country in list(countries2):
    if country.text == "India".capitalize():
        country.click()
        break
time.sleep(2)

country = driver.find_element(By.XPATH,"//*[@id='autosuggest']").get_attribute("value")
print(country)

assert country == "India"

time.sleep(3)
driver.close()
