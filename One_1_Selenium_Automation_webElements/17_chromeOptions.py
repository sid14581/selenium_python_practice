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
# driver.get_screenshot_as_file("s1.png")
# chrome_opt.add_argument("--ignore-certificate-errors")


browser = "edge"
driver = ""
if browser.lower() == "chrome".lower():
    chrome_opt = wd.ChromeOptions()
    chrome_opt.add_argument("--start-maximized")
    chrome_opt.add_argument("headless")
    chrome_opt.add_argument("--ignore-certificate-errors")
    url = Service(r"/webdrivers/chromedriver-win64/chromedriver.exe")
    driver = wd.Chrome(service=url,options=chrome_opt)
elif browser.lower() == "edge".lower():
    edge_opt = wd.EdgeOptions()
    edge_opt.add_argument("--start-maximized")
    edge_opt.add_argument("headless")
    edge_opt.add_argument("--ignore-certificate-errors")
    url = Service(r"/webdrivers/edgedriver_win64/msedgedriver.exe")
    driver = wd.Edge(service=url,options=edge_opt)
# elif browser.lower() == "firefox".lower():
#     url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\g eckodriver-v0.35.0-win-aarch64\geckodriver.exe")
#     driver = wd.Firefox(service=url)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
print()
print(driver.title)
print(driver.current_url)
print()


time.sleep(3)
driver.quit()
