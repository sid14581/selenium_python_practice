import time
from selenium import webdriver as wd
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(3)
print()
print(driver.title)
print(driver.current_url)
print()

driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1")))

sentence = driver.find_element(By.XPATH,"//p[contains(text(),'email')]").text
username = sentence.split(" ")[4]
print(username)
driver.close()
driver.switch_to.window(window_handles[0])

driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys("yoyo")

driver.find_element(By.XPATH,"//*[@value='user']").click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"button[id='okayBtn']")))
driver.find_element(By.CSS_SELECTOR,"button[id='okayBtn']").click()

driver.find_element(By.ID,"terms").click()
driver.find_element(By.NAME,"signin").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//form//*[contains(text(),'Incorrect')]")))
msg = driver.find_element(By.XPATH,"//form//*[contains(text(),'Incorrect')]/parent::*").text

assert "Incorrect" in msg

time.sleep(3)
driver.quit()
