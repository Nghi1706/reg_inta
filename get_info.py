import random
from random import choice
import re
import string
def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

def get_inf():
    ho = open(r'E:\.Autoreg\data_text\ho.txt', 'r', encoding="utf8")
    ten = open(r'E:\.Autoreg\data_text\ten_get.txt', 'r', encoding="utf8")
    a = choice(list(ho))
    b = choice(list(ten))
    ho.close()
    ten.close()
    a = a.strip('\n')
    b = b.strip('\n')
    b = re.sub(r'[0-9]+.', '', b)
    name = a+b
    usermame = no_accent_vietnamese(a)+"."+no_accent_vietnamese(b)
    username = re.sub(r' ', '', usermame)
    username += "_"+str(random.randint(100, 999)) + "."+str(random.randint(100, 999))
    username = no_accent_vietnamese(username)
    namepass = no_accent_vietnamese(re.sub(r' ', '', b))
    return [name, username, namepass]

def get_birth():
    year = random.randint(1990, 2002)
    month = random.randint(1, 12)
    def date(months):
        if (months == 1 or months == 3 or months == 5 or months == 7 or months == 8 or months == 10 or months == 12):
            return random.randint(1, 31)
        if (months == 2):
            return random.randint(1, 28)
        else:
            return random.randint(1, 30)
    date = date(month)
    datepass = str(date)+"_"+str(month)+"_"+str(year)
    return[date, month, year, datepass]

def full_inf():
    pwd = string.ascii_letters + string.digits + str("!@#$%^&*()}{")
    pwd = "".join(random.choice(pwd) for x in range(random.randint(4, 8)))
    a = get_inf()
    b = get_birth()
    fullname = a[0]
    username = a[1]
    date = b[0]
    month = b[1]
    year = b[2]
    password = a[2]+str(pwd)
    return[fullname, username, password, date, month, year]
def get_inf_FB():
    ho = open(r'E:\.Autoreg\data_text\ho.txt', 'r', encoding="utf8")
    ten = open(r'E:\.Autoreg\data_text\ten_get.txt', 'r', encoding="utf8")
    a = choice(list(ho))
    b = choice(list(ten))
    ho.close()
    ten.close()
    sex = [0, 1]
    sex = choice(sex)
    a = a.strip('\n')
    b = b.strip('\n')
    b = re.sub(r'[0-9]+.', '', b).lstrip()
    DOB = get_birth()
    namepass = no_accent_vietnamese(re.sub(r' ', '', b))
    pwd = string.ascii_letters + string.digits + str("!@#$%^&*()}{")
    pwd = "".join(random.choice(pwd) for x in range(random.randint(4, 8)))
    password = namepass+str(pwd)
    return [a, b, sex, DOB[0], DOB[1], DOB[2], password]
def status():
    status = open(r'E:\.Autoreg\data_text\status.txt', 'r', encoding="utf8")
    stt = choice(list(status))
    status.close()
    stt = re.sub(r'[0-9]+.', '', stt)
    stt = stt.lstrip()
    return stt


#date = get_birth()
#print(name)
#print(username)

#print(str(date[0])+"_"+str(date[1])+"_"+str(date[2]))
#print("dateofbirth = "+str(date(month))+"-"+str(month)+"-"+str(year))
#password = no_accent_vietnamese(re.sub(r' ', '', b))+str(year)+"_"+str(month)+"_"+str(date(month))
#print("password = "+password)

#i = full_inf()
#ketqua = open(r'E:\.Autoreg\ketqua\ketqua.txt', 'a', encoding="utf8")
#ketqua.write(str(i[1]) + "|" + str(i[2]) + "\n")
#ketqua.close()
#print(i)