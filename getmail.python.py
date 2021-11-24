import sys
import time
import random
import re
import pyperclip3
import dcom
from get_pic import *
from selenium.common.exceptions import NoSuchElementException
from dcom import reconnect
from selenium.webdriver.common.action_chains import ActionChains
from get_info import  get_inf_FB
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from http_request import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import win32clipboard
def filltext(input_name, A):
    for i in A:
        input_name.send_keys(i)
        time.sleep(random.uniform(0.09, 0.24))
def reg_mail():
    inf = get_inf_FB()
    options = Options()
    options.add_argument("-private-window")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    driver_mail = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options, firefox_profile=profile)
    driver_mail.set_window_size(590, 790)
    driver_mail.set_window_position(590, 0)
    time.sleep(random.uniform(5, 10))
    driver_mail.get("https://temp-mail.org/vi/")
    time.sleep(random.uniform(5, 10))
    wait(driver_mail, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.no-ajaxy.tm-btn.btn-gray.click-to-copy"))).click()
    time.sleep(random.uniform(2, 3))
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print (data)
def reg_ins_100():
    for i in range(10):
        reg_mail()
        time.sleep(5)
        dcom.reconnect()
        time.sleep(2)
reg_ins_100()