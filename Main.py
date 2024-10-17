from doctest import debug

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://tinder.com/"
email = "<YOUR_EMAIL>"
password = "<YOUR_PASSWORD>"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(2)

dec = driver.find_element(By.CSS_SELECTOR, '#t-342688478 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\$c-ds-background-primary\).C\(\$c-ds-text-secondary\) > div > div > div.D\(f\)--ml > div:nth-child(2) > button')
dec.click()

time.sleep(2)
c
b1 = driver.find_element(By.CSS_SELECTOR, '#t-342688478 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > div > main > div > div.Expand > div > div.Expand.Pos\(r\) > div > div > button.c1p6lbu0.W\(80\%\).My\(20px\).Mx\(a\)')
b1.click()


b2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#t-2071069554 > div > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > button"))
    )
b2.click()

# time.sleep(2)
#
# b2 = driver.find_element(By.CSS_SELECTOR, '#t-2071069554 > div > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > button')
# b2.click()

time.sleep(2)

b3 = driver.find_element(By.CSS_SELECTOR, '#t-2071069554 > div > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div.H\(100\%\).D\(f\).Fxd\(c\) > div.Mt\(a\) > span > div:nth-child(2) > button')
b3.click()

time.sleep(2)

main_window = driver.current_window_handle

for handle in driver.window_handles:
    if handle != main_window:
        facebook_window = handle
        break

driver.switch_to.window(facebook_window)

email_input = driver.find_element(By.CSS_SELECTOR, "#email")
email_input.send_keys(email)

pass_input = driver.find_element(By.CSS_SELECTOR, "#pass")
pass_input.send_keys(password)

b4 = driver.find_element(By.CSS_SELECTOR, "#loginbutton")
b4.click()


continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Continue as Adi']"))
    )
continue_button.click()

driver.switch_to.window(main_window)

time.sleep(2)

allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Allow']"))
    )
allow_button.click()

time.sleep(2)

miss = driver.find_element(By.CSS_SELECTOR, '#t-2071069554 > div > div > div > div > div.Bgc\(\$c-ds-background-primary\).Py\(24px\).Px\(36px\) > button.c1p6lbu0.W\(100\%\).Mt\(8px\)')
miss.click()

for i in range(100):
    time.sleep(2)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Lts\\(\\$ls-s\\).Cur\\(p\\).Bdrs\\(50%\\)"))
    )
    button.click()

driver.quit()