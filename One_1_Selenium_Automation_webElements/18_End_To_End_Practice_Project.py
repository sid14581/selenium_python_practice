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
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
print()
print(driver.title)
print(driver.current_url)
print()

phones = ["iphone X", "Samsung Note 8", "Blackberry"]
driver.find_element(By.XPATH, "//*[text()='Shop']").click()
wait = WebDriverWait(driver, 10)

for phone in phones:
    yo1 = "//*[text()='" + str(phone) + "']"
    yo2 = yo1 + "/ancestor::div[@class='card h-100']//button"

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, yo1)))
    driver.find_element(By.XPATH, yo2).click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Checkout')]")))
driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()

driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()

country = "india".capitalize()
driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys(country)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='" + country + "']")))
driver.find_element(By.XPATH, "//a[text()='" + country + "']").click()

driver.find_element(By.XPATH,"//input[@value='Purchase']").click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//strong")))
status_msg = driver.find_element(By.XPATH, "//strong/parent::*").text

print(status_msg.replace("×","").strip())

assert  "Success" in status_msg

time.sleep(3)
driver.quit()
