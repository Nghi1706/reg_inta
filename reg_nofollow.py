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

    driver = webdriver.Firefox(executable_path='E:\.Autoreg\driver\geckodriver.exe', options=options)

    driver.set_window_size(590, 790)

    time.sleep(random.uniform(5, 10))

    driver.get("https://www.instagram.com/")

    time.sleep(random.uniform(5, 10))
    wait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span._7UhW9.xLCgt.qyrsm.gtFbE.se6yk"))).click()
    time.sleep(random.uniform(2, 9))
    #phone from otp
    txt_phone = get_phone(token)
    if int(txt_phone[2]) == 1:
        print("erro !")
        driver.delete_all_cookies()
        driver.close()
    else:
        phone = driver.find_element_by_name("emailOrPhone")
        filltext(phone, str("0"+str(txt_phone[0])))
        #filltext(phone,"0"+str(random.randint(300000000, 999999999)))
        time.sleep(random.uniform(2, 9))
        full_name = driver.find_element_by_name("fullName")
        filltext(full_name, inf[0])
        time.sleep(random.uniform(2, 9))
        username = driver.find_element_by_name("username")
        filltext(username, inf[1])
        time.sleep(random.uniform(2, 9))
        password = driver.find_element_by_name("password")
        filltext(password, inf[2])
        time.sleep(random.uniform(2, 9))
        print(inf[1]+"-"+inf[2])
        dangky = driver.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
        #/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div[7]/div/button
        try:
            dangky[1].click()
        except NoSuchElementException:
            driver.delete_all_cookies()
            driver.close()

        # //*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[7]/div/button
        # //*[@id="react-root"]/div/div/section/main/div/div/div[1]/div/form/div[7]/div/button
        time.sleep(random.uniform(10, 15))

        #selection(inf[4], inf[3], inf[5])
        #time.sleep(random.randint(2, 5))
        try:
            select = driver.find_elements_by_css_selector("select.h144Z")
        except NoSuchElementException:
            driver.delete_all_cookies()
            driver.close()

        month = Select(select[0])

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
        tiep = driver.find_elements_by_css_selector("button.sqdOP.L3NKy._4pI4F.y3zKF")
        tiep[0].click()
        #confirmationCode - get_code
        time.sleep(random.uniform(39, 45))
        code = get_code(token, txt_phone[1])
        if int(code[0]) == 0:
            otp = driver.find_element_by_name("confirmationCode")
            filltext(otp, str(code[1]))
            ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
            ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
            ketqua.close()
            time.sleep(random.uniform(10, 15))
            acceptxt = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
            acceptxt.click()
            time.sleep(random.uniform(20, 25))
            driver.delete_all_cookies()
            driver.close()
        else:
            newc = driver.find_elements_by_css_selector("button.sqdOP.yWX7d.y3zKF")
            newc[1].click()
            time.sleep(random.randint(50, 55))
            code = get_code(token, txt_phone[1])
            if int(code[0]) == 0:
                otp = driver.find_element_by_name("confirmationCode")
                filltext(otp, str(code[1]))
                acceptxt = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                acceptxt.click()
                ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
                ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
                ketqua.close()
                time.sleep(random.uniform(20, 25))
                # -> regthanhcong
                driver.delete_all_cookies()
                driver.close()
            else:
                requests.get('http://otpsim.com/api/sessions/cancel?session=' + txt_phone[1] + '&token=' +token)
                txt_phone = get_phone(token)
                if int(txt_phone[2]) == 1:
                    print("erro !")
                    driver.close()
                else:
                    newp = driver.find_elements_by_css_selector("button.sqdOP.yWX7d.y3zKF")
                    newp[0].click()
                    time.sleep(random.randint(5, 9))
                    newphone = driver.find_element_by_name("newPhoneNumber")
                    filltext(newphone, "0"+str(txt_phone[0]))
                    time.sleep(random.randint(2, 5))
                    acceptxt = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                    acceptxt.click()
                    time.sleep(random.randint(5, 8))
                    #otp = driver.find_element_by_name("confirmationCode")
                    time.sleep(random.randint(39, 45))
                    code = get_code(token, txt_phone[1])
                    if int(code[0]) == 0:
                        otp = driver.find_element_by_name("confirmationCode")
                        filltext(otp, str(code[1]))
                        time.sleep((random.randint(3, 7)))
                        ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
                        ketqua.write(str(inf[1]) + "|" + str(inf[2]) + "|" + "reg thanh cong" + "\n")
                        ketqua.close()
                        time.sleep(random.uniform(10, 15))
                        acceptxt = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
                        acceptxt.click()
                        time.sleep(random.uniform(20, 25))
                        driver.delete_all_cookies()
                        driver.close()
                    else:
                        requests.get('http://otpsim.com/api/sessions/cancel?session=' + txt_phone[1] + '&token=' + token)
                        ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
                        ketqua.write(str(inf[1]) + "|" + str(inf[2])+ "|" +"reg KO thanh cong"+ "\n")
                        ketqua.close()
                        driver.delete_all_cookies()
                        driver.close()

def regforend(token):
    money = check_cost(token)
    while (money >= 700):
        money = check_cost(token)
        print(money)
        regins(token)
        time.sleep(10)
        reconnect()
        time.sleep(random.randint(30, 45))

regforend("2596cf29acceefb84207533244fe5c7a")