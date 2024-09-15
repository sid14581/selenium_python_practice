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
    url = Service(r"/webdrivers/chromedriver-win64/chromedriver.exe")
    driver = wd.Chrome(service=url)
elif browser.lower() == "edge".lower():
    url = Service(r"/webdrivers/edgedriver_win64/msedgedriver.exe")
    driver = wd.Edge(service=url)
# elif browser.lower() == "firefox".lower():
#     url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")
#     driver = wd.Firefox(service=url)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print()
print(driver.title)
print(driver.current_url)
time.sleep(3)

# CHECKBOX
driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").click()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and @value]")

for checkbox in checkboxes:
    if checkbox.get_attribute("value").lower() == "Option2".lower():
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(3)

# RADIO-BUTTON
radio_buttons = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")

for radio_button in radio_buttons:
    if radio_button.get_attribute("value").lower() == "Radio1".lower():
        radio_button.click()
        assert radio_button.is_selected()
        break


time.sleep(3)
assert driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(2)
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID,"displayed-text").is_displayed()


time.sleep(3)
driver.close()
