import sys
import time
import random
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
def filltext(input_name, A):
    for i in A:
        input_name.send_keys(i)
        time.sleep(random.uniform(0.09, 0.24))

def regins(token):
# infor
    inf = full_inf()

    options = Options()

    options.add_argument("-private-window")

    profile = webdriver.FirefoxProfile()

    profile.set_preference("permissions.default.image", 2)

    drivers = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options, firefox_profile=profile)

    drivers.set_window_size(590, 790)

    time.sleep(random.uniform(5, 10))

    drivers.get("https://www.instagram.com/")

    time.sleep(random.uniform(5, 10))
    try:
        wait(drivers, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span._7UhW9.xLCgt.qyrsm.gtFbE.se6yk"))).click()
    except NoSuchElementException:
        drivers.close()
        return

    time.sleep(random.uniform(2, 9))
    #phone from otp
    txt_phone = get_phone(token)
    if int(txt_phone[2]) == 1:
        print("erro !")
        drivers.delete_all_cookies()

        drivers.close()
    else:
        phone = drivers.find_element_by_name("emailOrPhone")
        filltext(phone, str("0"+str(txt_phone[0])))
        #filltext(phone,"0"+str(random.randint(300000000, 999999999)))
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
        print(inf[1]+"-"+inf[2])
        dangky = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
        #/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div[7]/div/button
        try:
            dangky[1].click()
        except NoSuchElementException:
            drivers.delete_all_cookies()
            drivers.close()
            return
        time.sleep(random.uniform(5, 9))
        try:
            select = drivers.find_elements_by_css_selector("select.h144Z")
        except NoSuchElementException:
            drivers.delete_all_cookies()
            drivers.close()
            return
        try:
            month = Select(select[0])
        except IndexError:
            requests.get('http://otpsim.com/api/sessions/cancel?session=' + txt_phone[1] + '&token=' + token)
            drivers.delete_all_cookies()
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
        #click tieptuc

        #driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button").click()
        tiep = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy._4pI4F.y3zKF")
        tiep[0].click()
        #confirmationCode - get_code
        time.sleep(random.uniform(39, 45))
        code = get_code(token, txt_phone[1])
        if int(code[0]) == 0:
            otp = drivers.find_element_by_name("confirmationCode")
            filltext(otp, str(code[1]))
            ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
            ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
            ketqua.close()
            time.sleep(random.uniform(10, 15))
            #//*[@id="react-root"]/section/main/div/div/div[1]/div/div/div/form/div[2]/button
            acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
            acceptxt.click()
            #-> regthanhcong
            #accept turn on notification
            time.sleep(random.uniform(13, 15))
            try:
                #drivers.find_element_by_css_selector("button.aOOlW.HoLwm").click()
                #time.sleep(random.uniform(3, 5))
                b = random.randint(10, 12)
                a = random.sample(range(1, 30), b)
                a = sorted(a)
                time.sleep(random.uniform(5, 8))
                d = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                for i in range(b):
                    try:
                        if int(i) > 5:
                            d[int(a[int(i)] - 3)].location_once_scrolled_into_view
                        # ActionChains(driver).move_to_element(d[int(a[i])]).perform()
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
            newc = drivers.find_elements_by_css_selector("button.sqdOP.yWX7d.y3zKF")
            newc[1].click()
            time.sleep(random.randint(50, 55))
            code = get_code(token, txt_phone[1])
            if int(code[0]) == 0:
                otp = drivers.find_element_by_name("confirmationCode")
                filltext(otp, str(code[1]))
                acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                acceptxt.click()
                ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
                ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
                ketqua.close()
                time.sleep(random.uniform(13, 15))
                try:
                    #drivers.find_element_by_css_selector("button.aOOlW.HoLwm").click()
                    #time.sleep(random.uniform(5, 10))
                    b = random.randint(10, 12)
                    a = random.sample(range(1, 30), b)
                    a = sorted(a)
                    time.sleep(random.uniform(5, 8))
                    d = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                    for i in range(b):
                        try:
                            if int(i) > 5:
                                d[int(a[int(i)] - 3)].location_once_scrolled_into_view
                            # ActionChains(driver).move_to_element(d[int(a[i])]).perform()
                            time.sleep(random.uniform(2, 3.5))
                            d[int(a[i])].click()
                            time.sleep(random.randint(3, 5))
                        except IndexError:
                            drivers.delete_all_cookies()
                            drivers.close()
                            return
                    drivers.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                    time.sleep(random.uniform(1, 3))
                    ecc = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                    time.sleep(random.uniform(3, 5))
                    ecc[-1].click()
                    time.sleep(random.uniform(3, 5))
                    drivers.delete_all_cookies()
                    drivers.close()
                except NoSuchElementException:
                    time.sleep((random.uniform(5, 10)))
                    drivers.delete_all_cookies()
                    drivers.close()
                    return

            else:
                requests.get('http://otpsim.com/api/sessions/cancel?session=' + txt_phone[1] + '&token=' +token)
                txt_phone = get_phone(token)
                if int(txt_phone[2]) == 1:
                    print("erro !")
                    drivers.delete_all_cookies()
                    drivers.close()
                    newp = drivers.find_elements_by_css_selector("button.sqdOP.yWX7d.y3zKF")
                    newp[0].click()
                    time.sleep(random.randint(5, 9))
                    newphone = drivers.find_element_by_name("newPhoneNumber")
                    filltext(newphone, "0" + str(txt_phone[0]))
                    time.sleep(random.randint(2, 5))
                    acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                    acceptxt.click()
                    time.sleep(random.randint(5, 8))
                    # otp = driver.find_element_by_name("confirmationCode")
                    time.sleep(random.randint(39, 45))
                    code = get_code(token, txt_phone[1])
                else:

                    if int(code[0]) == 0:
                        otp = drivers.find_element_by_name("confirmationCode")
                        filltext(otp, str(code[1]))
                        time.sleep((random.randint(3, 7)))
                        ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
                        ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
                        ketqua.close()
                        time.sleep(random.uniform(10, 15))
                        acceptxt = drivers.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                        acceptxt.click()
                        time.sleep(random.uniform(13, 15))
                        try:
                            #drivers.find_element_by_css_selector("button.aOOlW.HoLwm").click()
                            #time.sleep(random.uniform(5, 10))
                            b = random.randint(10, 12)
                            a = random.sample(range(1, 30), b)
                            a = sorted(a)
                            time.sleep(random.uniform(5, 8))
                            d = drivers.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                            # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                            for i in range(b):
                                try:
                                    if int(i) > 5:
                                        d[int(a[int(i)] - 3)].location_once_scrolled_into_view
                                    # ActionChains(driver).move_to_element(d[int(a[i])]).perform()
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
                            time.sleep(random.uniform(5, 9))
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
                        requests.get('http://otpsim.com/api/sessions/cancel?session=' + txt_phone[1] + '&token=' + token)
                        drivers.delete_all_cookies()
                        drivers.close()
                        return

def regforend(token):
    money = check_cost(token)
    while (money >= 700):
        money = check_cost(token)
        print(money)
        regins(token)
        time.sleep(3)
        reconnect()
        time.sleep(random.randint(20, 39))

regforend("765df13e89ff7e141cb0191bc05a2001")