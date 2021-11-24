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
from selenium.common.exceptions import TimeoutException
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
    drivers = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options, firefox_profile=profile)
    driver_mail = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options, firefox_profile=profile)
    driver_mail.set_window_size(590, 790)
    drivers.set_window_size(590, 790)
    drivers.set_window_position(0, 0)
    driver_mail.set_window_position(590, 0)
    time.sleep(random.uniform(5, 10))
    drivers.get("https://facebook.com/")
    driver_mail.get("https://temp-mail.org/vi/")
    time.sleep(random.uniform(5, 10))
    try:
        wait(drivers, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy"))).click()
    except TimeoutException:
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        drivers.close()
        driver_mail.close()
        return
    wait(driver_mail, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.no-ajaxy.tm-btn.btn-gray.click-to-copy"))).click()
    time.sleep(random.uniform(2, 3))
    #ho
    ho = drivers.find_element_by_name("lastname")
    filltext(ho, inf[0])
    time.sleep(random.uniform(2, 5))
    #ten
    ten = drivers.find_element_by_name("firstname")
    filltext(ten, inf[1])
    time.sleep(random.uniform(2, 5))
    #mail
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    data = re.sub(r' ', '', data)
    win32clipboard.CloseClipboard()
    mail = drivers.find_element_by_name("reg_email__")
    filltext(mail, str(data))
    time.sleep(random.uniform(2, 5))
    #mail _ nhap lai
    re_mail = drivers.find_element_by_name("reg_email_confirmation__")
    filltext(re_mail, str(data))
    time.sleep(random.uniform(2, 5))
    # pass word
    password = drivers.find_element_by_name("reg_passwd__")
    filltext(password, inf[6])
    time.sleep(random.uniform(2, 3))
    #ngay sinh
    date = drivers.find_element_by_name("birthday_day")
    date = Select(date)
    date.select_by_value(str(inf[3]))
    time.sleep(random.uniform(0.5, 1.5))
    # thang sinh
    month = drivers.find_element_by_name("birthday_month")
    month = Select(month)
    month.select_by_value(str(inf[4]))
    time.sleep(random.uniform(0.5, 1.5))
    # nam sinh
    year = drivers.find_element_by_name("birthday_year")
    year = Select(year)
    year.select_by_value(str(inf[5]))
    time.sleep(random.uniform(0.5, 1.5))
    #sex
    sex = drivers.find_elements_by_name("sex")
    sex[int(inf[2])].click()
    time.sleep(random.uniform(2, 5))
    dangky = drivers.find_element_by_css_selector("button._6j.mvm._6wk._6wl._58mi._6o._6v")
    dangky.click()
    time.sleep(random.uniform(5, 7))
    tieptuc = drivers.find_element_by_css_selector("div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.bp9cbjyn.owycx6da.btwxx1t3.kt9q3ron.ak7q8e6j.isp2s0ed.ri5dt5u2.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.d1544ag0.tw6a2znq.s1i5eluu.tv7at329")
    tieptuc.click()
    print(str(data)+"|"+inf[6])
    # confirmationCode - get_code
    time.sleep(39)
    driver_mail.find_element_by_css_selector("div.bg-header.d-none.visable-xs-sm").location_once_scrolled_into_view
    time.sleep(2)
    try:
        code = driver_mail.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a/span[4]").text
    except NoSuchElementException:
        drivers.delete_all_cookies()
        driver_mail.delete_all_cookies()
        drivers.close()
        driver_mail.close()
        return
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
        otp = drivers.find_element_by_name("captcha_response")
        filltext(otp, code)
        driver_mail.delete_all_cookies()
        driver_mail.close()
        time.sleep(random.uniform(3, 5))
        acceptxt = drivers.find_element_by_css_selector("input.bj.v.bk.bl.bm")
        acceptxt.click()
        time.sleep(random.uniform(13, 15))
        checkpoint = drivers.current_url
        checkpoint = str(checkpoint)
        checkpoint = checkpoint.find("challenge")
        if int(checkpoint) == -1:
            ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
            ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
            ketqua.close()
            time.sleep(random.uniform(3, 5))
            try:
                b = random.randint(10, 12)
                a = random.sample(range(1, 30), b)
                a = sorted(a)
                time.sleep(random.uniform(5, 8))
                d = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                for i in range(b):
                    try:
                        if int(i) > 5:
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
        else:
            drivers.delete_all_cookies()
            drivers.close()
            return
def reg_ins_100():
    for i in range(10):
        reg_mail()
        time.sleep(5)
        dcom.reconnect()
        time.sleep(2)
reg_ins_100()