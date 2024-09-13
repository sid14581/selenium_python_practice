import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
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
driver.get("https://rahulshettyacademy.com/angularpractice/")
print()
print(driver.title)
print(driver.current_url)
time.sleep(3)

driver.find_element(By.NAME,"name").send_keys("Sid")
driver.find_element(By.NAME,"email").send_keys("yoyo@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("yoyo@gmail123")
driver.find_element(By.ID,"exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR,"input#inlineRadio1").click()   # css id selector

#driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(3)

msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(msg)

assert "Success" in msg
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("siddhardh")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()


time.sleep(3)
driver.close()
