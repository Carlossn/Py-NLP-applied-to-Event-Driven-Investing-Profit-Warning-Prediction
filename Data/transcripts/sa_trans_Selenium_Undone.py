# coding: utf-8
# IMPORTANTL the line above avoids having a "Python SyntaxError: Non-ASCII character ‘xe2′ in file..." when executing selenium
# The documentatio of selenium is here: http://selenium-python.readthedocs.io/index.html

################################################# LIVE EXAMPLE: ############################################################### 

# Check wwww.python.org and search "Django" term in the search bar using selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # keys class provide keys in the keyboard like RETURN, F1, ALT etc.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome('C:\Users\Carlo\Desktop\chromedriver.exe') 
driver.get('http://seekingalpha.com/') # driver.get() method will navigate to the URL given and will wait until the page is fully loaded before returning control to your test or sc# ript. 

elem = driver.find_element_by_xpath('//[@id="hd-auto"]') # right click "inspect", click into wwww.python.org search bar and you will find "name = q" in its html code.
elem.clear() # clear any previous text
elem.send_keys("COL") # type Ticker 
elem.send_keys(Keys.RETURN) # equivalent to write click "Go" in the website search bar  

