import sys
import re
import time
import random
import string
import os
import selenium.common.exceptions

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
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import autoit
from get_info import status
def filltext(input_name, A):
    for i in A:
        input_name.send_keys(i)
        time.sleep(random.uniform(0.09, 0.24))

def upload(user, pas):
    option = Options()
    option.add_argument("-private-window")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1")
    driver = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', firefox_profile=profile, options=option)
    driver.set_window_size(590, 790)
    driver.get("https://www.instagram.com/")
    time.sleep(random.uniform(4, 6))
    a = driver.find_elements_by_css_selector("button.sqdOP.yWX7d.y3zKF")
    time.sleep(random.uniform(0.5, 2))
    a[0].click()
    time.sleep(random.uniform(4, 6))
    #Vu.NgocLam_14405|NgocLamEBY%*K
    username = driver.find_element_by_name("username")
    filltext(username, str(user))
    time.sleep(random.uniform(0.5, 2))
    password = driver.find_element_by_name("password")
    filltext(password, str(pas))
    #-> dang nhap
    a = driver.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF ")
    time.sleep(random.uniform(0.5, 1))
    a[-1].click()
    time.sleep(random.uniform(4, 6))
    checkpoint = driver.current_url
    checkpoint = str(checkpoint)
    checkpoint = checkpoint.find("challenge")
    if int(checkpoint) == -1:
        #-> tat thong bao
        try:
            driver.find_element_by_id("slfErrorAlert").text
            driver.delete_all_cookies()
            driver.close()
            return 1
        except NoSuchElementException:
            pass
        time.sleep(random.uniform(4, 6))
        a = wait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.sqdOP.yWX7d.y3zKF"))).click()
        #a = driver.find_element_by_css_selector("button.sqdOP.yWX7d.y3zKF")
        #time.sleep(random.uniform(0.5, 2))
        #a.click()
        time.sleep(random.uniform(4, 6))
        driver.get("https://www.instagram.com/"+str(user)+"/")
        time.sleep(random.uniform(4, 6))
        try:
            driver.find_element_by_css_selector("img.be6sR").click()
        except NoSuchElementException:
            driver.get("https://www.instagram.com/" + str(user) + "/")
            time.sleep(random.uniform(4, 6))
            driver.find_element_by_css_selector("img.be6sR").click()
        time.sleep(random.uniform(4, 6))
        autoit.win_wait_active("Tải lên một tập tin", 5)
        autoit.control_send("Tải lên một tập tin", "Edit1", "E:\.Autoreg\Avata"+"\\"+str(random.choice(os.listdir(r'E:\.Autoreg\Avata'))))
        autoit.win_wait_active("Tải lên một tập tin", 5)
        autoit.control_click("Tải lên một tập tin", "Button1")
        time.sleep(random.uniform(3, 5))
        driver.find_element_by_css_selector("button.UP43G").click()
        time.sleep(random.uniform(10, 12))
        driver.find_element_by_css_selector("button.aOOlW.bIiDR").click()
        time.sleep(random.uniform(10, 12))
        for i in range(2):
            wait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.q02Nz._0TPg"))).click()
            autoit.win_wait_active("Tải lên một tập tin", 5)
            autoit.control_send("Tải lên một tập tin", "Edit1", r"E:\.Autoreg\status"+"\\"+str(random.choice(os.listdir(r'E:\.Autoreg\status'))))
            autoit.win_wait_active("Tải lên một tập tin", 5)
            autoit.control_click("Tải lên một tập tin", "Button1")
            time.sleep(random.uniform(3, 5))
            driver.find_element_by_css_selector("button.UP43G").click()
            time.sleep(random.uniform(3, 5))
            stt = status()
            driver.find_element_by_css_selector("textarea._472V_").send_keys(str(stt))
            time.sleep(random.uniform(3, 5))
            driver.find_element_by_css_selector("button.UP43G").click()
            time.sleep(random.uniform(8, 10))
        time.sleep(random.randint(3, 5))
        driver.get("https://www.instagram.com/" + str(user) + "/")
        follow = driver.find_elements_by_css_selector("span.g47SY.lOXF2")
        if int(follow[-1].text) < 10:
            time.sleep(random.uniform(2, 5))
            driver.find_element_by_css_selector("button.wpO6b").click()
            time.sleep(random.uniform(4, 6))
            b = random.randint(10, 12)
            a = random.sample(range(1, 22), b)
            a = sorted(a)
            time.sleep(random.uniform(5, 8))
            d = driver.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            for t in range(b):
                if int(a[t]) > 6:
                    #driver.execute_script("arguments[0].scrollIntoView();", d[int(a[t])+3])
                    d[int(a[t])-3].location_once_scrolled_into_view
                    time.sleep(random.uniform(2, 3))
                time.sleep(random.uniform(2.5, 3))
                d[int(a[t])].click()
                time.sleep(random.uniform(1, 2))
            print("follow 10 : done !")
        else:
            print("follow >=  10 : true !")
        driver.get("https://www.instagram.com/" + str(user) + "/")
        time.sleep(random.uniform(4, 6))
        insstatus = driver.find_elements_by_css_selector("span.g47SY.lOXF2")
        if int(insstatus[0].text) < 3:
            print("erro upstatus, re_up !")
            time.sleep(random.uniform(4, 6))
            driver.refresh()
            time.sleep(random.uniform(4, 6))
            for i in range(int(3 - int(insstatus[0].text))):
                wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.q02Nz._0TPg"))).click()
                autoit.win_wait_active("Tải lên một tập tin", 5)
                autoit.control_send("Tải lên một tập tin", "Edit1", r"E:\.Autoreg\status\\" + str(random.choice(os.listdir(r'E:\.Autoreg\status'))))
                autoit.win_wait_active("Tải lên một tập tin", 5)
                autoit.control_click("Tải lên một tập tin", "Button1")
                time.sleep(random.uniform(3, 5))
                driver.find_element_by_css_selector("button.UP43G").click()
                time.sleep(random.uniform(3, 5))
                driver.find_element_by_css_selector("button.UP43G").click()
                time.sleep(random.uniform(8, 10))
        else:
            print("ALL _ DONE !")
        driver.delete_all_cookies()
        driver.close()
        return 10
        #10 = all done
    else:
        driver.delete_all_cookies()
        driver.close()
        return 1
        # 1 = checkpoint

def do_ins():
    a = open(r"E:\.Autoreg\ketqua\ketqua.txt", encoding="utf8")
    for i in a:
        use = i.split("|")
        a = upload(use[0], use[1])
        if int(a == 1):
            file_done = open(r"E:\.Autoreg\ketqua\ketqua_upload.txt", 'a', encoding="utf8")
            i = re.sub(r'reg thanh cong', 'checkpoint', i)
            file_done.write(i)
            file_done.close()
        if int(a == 10):
            file_done = open(r"E:\.Autoreg\ketqua\ketqua_upload.txt", 'a', encoding="utf8")
            i = re.sub(r'reg thanh cong', 'all done', i)
            file_done.write(i)
            file_done.close()
        time.sleep(3)
        reconnect()
        time.sleep(random.randint(2, 5))
    a.close()

do_ins()