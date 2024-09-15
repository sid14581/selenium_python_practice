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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
print()
print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("melon")

results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(driver.find_elements(By.XPATH, "//div[@class='product']"))
print("melon items-->", count)
assert count > 0

for result in results:
    result.find_element(By.CSS_SELECTOR, "button[type='button']").click()

driver.find_element(By.XPATH, "//input[@type='search']").clear()

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("berry")
results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(driver.find_elements(By.XPATH, "//div[@class='product']"))
print("berry items-->", count)
assert count > 0

for result in results:
    result.find_element(By.CSS_SELECTOR, "button[type='button']").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//*[contains(text(),'CHECKOUT')]").click()

wait = WebDriverWait(driver,7)
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoBtn")))

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"promoInfo"))) # value shoulld be passed as a tuple
code_msg = driver.find_element(By.CLASS_NAME, "promoInfo").text
print();
print(code_msg)
print();
#############################################################################################################
#############################################################################################################

# TOTAL_AMOUNT
list_of_amts = driver.find_elements(By.CSS_SELECTOR,"tbody td:nth-child(5) .amount")
total_sum = 0
for amt in list_of_amts:
    total_sum += int(amt.text)

total_amt = int(driver.find_element(By.CLASS_NAME,"totAmt").text)
print("total_sum",total_sum) ; print("total_amt",total_amt)
assert total_amt == total_sum

#############################################################################################################
#############################################################################################################

# DISCOUNT_AMOUNT

discount_per = driver.find_element(By.XPATH,"//span[@class='discountPerc']").text
discount = int(discount_per.split("%")[0])
print("discount percentage",discount)

discount_amt = total_sum - (total_sum * (discount/100))
total_discount_amt = float(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)
print("discount amount",discount_amt) ; print("total discount amount",total_discount_amt)
assert discount_amt == total_discount_amt

assert total_amt > total_discount_amt
time.sleep(3)
driver.quit()
