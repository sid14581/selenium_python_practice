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
    chrome_opt = wd.ChromeOptions()
    chrome_opt.add_argument("headless")
    #chrome_opt.add_argument("--ignore-certificate-errors")
    url = Service(r"/webdrivers/chromedriver-win64/chromedriver.exe")
    driver = wd.Chrome(service=url,options=chrome_opt)

elif browser.lower() == "edge".lower():
    edge_opt = wd.EdgeOptions()
    edge_opt.add_argument("headless")
    #edge_opt.add_argument("--ignore-certificate-errors")
    url = Service(r"/webdrivers/edgedriver_win64/msedgedriver.exe")
    driver = wd.Edge(service=url,options=edge_opt)

# elif browser.lower() == "firefox".lower():
#     url = Service(r"C:\Users\siddh\PycharmProjects\pythonProject\webdrivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")
#     driver = wd.Firefox(service=url)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(3)
print()
print(driver.title)
print(driver.current_url)
print()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#driver.get_screenshot_as_file("s1.png")
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
#driver.get_screenshot_as_file("s2.png")
driver.execute_script("document.getElementById('checkBoxOption3').click()")

time.sleep(3)
driver.quit()

