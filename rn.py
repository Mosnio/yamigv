from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import secrets
import random
import string
import os
import random
import time

from tbselenium.tbdriver import TorBrowserDriver
from os.path import dirname, join, realpath, getsize


r1 = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=random.randint(3,4)))

r2=''.join(random.choices(string.digits, k=random.randint(3,5)))

pas=r1+r2





N = 7
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=28))

res1=''.join(random.choices(string.digits, k=4))

res0=''.join(random.choices(string.ascii_uppercase, k=1))

nl = ( str(res1) + str(res))
fbl = random.sample(nl,k=32)
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
tr=(listToString(fbl))
trx=('T'+str(res0)+tr)




with TorBrowserDriver("/home/test/tor-browser_en-US") as driver:
	time.sleep(10)
	driver.get('https://app.spacemine.pro?referrer=657')
	time.sleep(15)
	driver.maximize_window()
	time.sleep(10)
	driver.find_element(By.XPATH, value= '//*[@id="wallet"]').send_keys(trx)
	time.sleep(10)
	driver.find_element(By.XPATH, value= '//*[@id="password"]').send_keys(pas)
	time.sleep(4)
	driver.find_element(By.XPATH, value= "//input[@value='Go']").click()
	time.sleep(25)
	print("ALL DONE SIR")
