import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

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
driver.get("https://rahulshettyacademy.com/client")
print()
print(driver.title)
print(driver.current_url)
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(2)

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2)>input").send_keys("Siddu716$")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Siddu716$")
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(3)
driver.close()
