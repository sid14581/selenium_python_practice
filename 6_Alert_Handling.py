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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print()
print(driver.title)
print(driver.current_url)
time.sleep(3)
print()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Sid")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alt = driver.switch_to.alert
alert_msg = alt.text
print(alert_msg)
assert "Sid" in alert_msg
alt.accept()
print()

time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Harsha")
driver.find_element(By.XPATH, "//input[@value='Confirm']").click()
time.sleep(2)
alt = driver.switch_to.alert
alter_msg = alt.text
print(alter_msg)
assert "Harsha" in alter_msg
alt.dismiss()

time.sleep(3)
driver.close()
