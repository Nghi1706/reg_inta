import sys
import time
import random
import re
import win32clipboard
import dcom
from get_pic import *
from selenium.common.exceptions import NoSuchElementException
from dcom import reconnect
from selenium.webdriver.common.action_chains import ActionChains
from get_info import full_inf
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
from selenium.common.exceptions import  TimeoutException
def filltext(input_name, A):
    for i in A:
        input_name.send_keys(i)
        time.sleep(random.uniform(0.09, 0.24))
def reg_mail():
    inf = full_inf()
    options = Options()
    options.add_argument("-private-window")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    drivers = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options, firefox_profile=profile)
    driver_mail = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options, firefox_profile=profile)
    driver_mail.set_window_size(590, 790)
    drivers.set_window_size(590, 790)
    drivers.set_window_position(0, 0)
    driver_mail.set_window_position(590, 0)
    time.sleep(random.uniform(5, 10))
    drivers.get("https://www.instagram.com/")
    driver_mail.get("https://temp-mail.org/vi/")
    time.sleep(random.uniform(5, 10))
    try:
        wait(drivers, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span._7UhW9.xLCgt.qyrsm.gtFbE.se6yk"))).click()
    except TimeoutException:
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        drivers.close()
        driver_mail.close()
        return
    wait(driver_mail, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.no-ajaxy.tm-btn.btn-gray.click-to-copy"))).click()
    time.sleep(random.uniform(2, 3))
    tempmail = drivers.find_element_by_name("emailOrPhone")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    filltext(tempmail, str(data))
    time.sleep(random.uniform(2, 5))
    full_name = drivers.find_element_by_name("fullName")
    filltext(full_name, inf[0])
    time.sleep(random.uniform(2, 5))
    username = drivers.find_element_by_name("username")
    filltext(username, inf[1])
    time.sleep(random.uniform(2, 5))
    password = drivers.find_element_by_name("password")
    filltext(password, inf[2])
    time.sleep(random.uniform(2, 5))
    print(inf[1] + "-" + inf[2])
    dangky = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
    try:
        dangky[1].click()
    except NoSuchElementException:
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        driver_mail.close()
        drivers.close()
        return
    time.sleep(random.uniform(5, 9))
    try:
        select = drivers.find_elements_by_css_selector("select.h144Z")
    except NoSuchElementException:
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        driver_mail.close()
        drivers.close()
        return
    try:
        month = Select(select[0])
    except IndexError:
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        driver_mail.close()
        drivers.close()
        return

    month.select_by_value(str(inf[4]))
    time.sleep(random.uniform(2, 5))
    date = Select(select[1])
    date.select_by_value(str(inf[3]))
    time.sleep(random.uniform(2, 5))
    year = Select(select[2])
    year.select_by_value(str(inf[5]))
    time.sleep(random.uniform(2, 9))
    tiep = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy._4pI4F.y3zKF")
    tiep[0].click()
    # confirmationCode - get_code
    driver_mail.find_element_by_css_selector("div.bg-header.d-none.visable-xs-sm").location_once_scrolled_into_view
    time.sleep(2)
    try:
        code = wait(driver_mail, 39).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a/span[4]"))).text
    except TimeoutException:
        time.sleep(random.uniform(1, 2))
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        driver_mail.close()
        drivers.close()
        return
        #code = driver_mail.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a/span[4]").text
    print(code)
    if code == "":
        time.sleep(random.uniform(1, 2))
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        driver_mail.close()
        drivers.close()
        return
    else:
        code = re.findall(r'\d+', code)
        code = list(map(int, code))
        code = str(code[0])
        if (len(code) == 6):
            pass
        if (len(code) == 5):
            code = "0"+str(code)
            code = str(code)
            pass
        otp = drivers.find_element_by_name("email_confirmation_code")
        time.sleep(random.uniform(2.5, 6.5))
        filltext(otp, code)
        driver_mail.delete_all_cookies()
        driver_mail.close()
        time.sleep(random.uniform(3, 5))
        acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy._4pI4F.y3zKF")
        acceptxt.click()
        time.sleep(random.uniform(13, 15))
        accounts = drivers.current_url
        accounts = str(accounts)
        accounts = accounts.find("accounts")
        if (accounts != -1):
            acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy._4pI4F.y3zKF")
            acceptxt.click()
            time.sleep(random.uniform(12, 15))
            accounts = drivers.current_url
            time.sleep(random.uniform(1, 2))
            accounts = str(accounts)
            accounts = accounts.find("accounts")
            time.sleep(random.uniform(1, 2))
        if (accounts != -1):
            acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy._4pI4F.y3zKF")
            acceptxt.click()
            time.sleep(random.uniform(12, 15))
            accounts = drivers.current_url
            time.sleep(random.uniform(1, 2))
            accounts = str(accounts)
            accounts = accounts.find("accounts")
            time.sleep(random.uniform(1, 2))
        if (accounts != -1):
            drivers.get("https://www.instagram.com/")
            time.sleep(random.uniform(2, 5))
            username = drivers.find_element_by_name("username")
            filltext(username, str(inf[1]))
            time.sleep(random.uniform(1, 2))
            password = drivers.find_element_by_name("password")
            filltext(password, str(inf[2]))
            time.sleep(random.uniform(1, 2))
            drivers.find_element_by_css_selector("button.Igw0E.IwRSH.eGOV_._4EzTm").click()
            time.sleep(random.uniform(2, 5))
        checkpoint = drivers.current_url
        checkpoint = str(checkpoint)
        checkpoint = checkpoint.find("challenge")
        accounts = drivers.current_url
        time.sleep(random.uniform(1, 2))
        accounts = str(accounts)
        accounts = accounts.find("accounts")
        if int(checkpoint) == -1:
            ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
            ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
            ketqua.close()
            time.sleep(random.uniform(3, 5))
            try:
                b = random.randint(2, 5)
                a = random.sample(range(1, 30), b)
                a = sorted(a)
                time.sleep(random.uniform(5, 8))
                d = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                for i in range(b):
                    try:
                        if int(a[i]) > 5:
                            d[int(a[int(i)] - 3)].location_once_scrolled_into_view
                        time.sleep(random.uniform(2, 3.5))
                        d[int(a[i])].click()
                        time.sleep(random.randint(1, 3))
                    except IndexError:
                        drivers.delete_all_cookies()
                        drivers.close()
                        return
                drivers.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                time.sleep(random.uniform(1, 3))
                ecc = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                time.sleep(random.uniform(3, 5))
                ecc[-1].click()
                time.sleep(random.uniform(5, 9))
                drivers.delete_all_cookies()
                drivers.close()
            except NoSuchElementException:
                time.sleep(random.uniform(10, 15))
                drivers.delete_all_cookies()
                drivers.close()
                return
        if (int(checkpoint) == -1 & accounts != -1):
            drivers.delete_all_cookies()
            drivers.close()
            return

        else:
            drivers.delete_all_cookies()
            drivers.close()
            return
def reg_ins_100():
    for i in range(120):
        reg_mail()
        print("......"+str(i)+".......")
        time.sleep(5)
        #dcom.reconnect()
        #time.sleep(2)
reg_ins_100()