import requests
import random
import time
def check_cost(token):
    r = requests.get('http://otpsim.com/api/users/balance?token='+token)
    r = r.json()
    r = r['data']['balance']
    return r

def check_network(token):
    r = requests.get('http://otpsim.com/api/networks?token='+token)
    r = r.json()
    r = r['data']
    return r
# 1 : mobi , 2 : vina, 3 : viettel
def check_service(token):
    r = requests.get('http://otpsim.com/api/service/request?token='+token)
    r = r.json()
    r = r['data']
    return r
# {'id': 36, 'name': 'Instagram', 'price': 350}
def get_phone(token):
    r = requests.get('http://otpsim.com/api/phones/request?token='+token+'&service=36&network='+str(random.randint(1, 3)))
    r = r.json()
    a = r['status_code']
    if int(a) == 200:
        r = r['data']
        phone = r['phone_number']
        session = r['session']
        loi = 0
    else:
        phone = 1
        session = 1
        loi = 1
    print(str([phone, session]))
    return [phone, session, loi]


def get_code(token, session):
#http://otpsim.com/api/sessions/b4f71cb62c2a77e13937c00fd0548e1b?token=c28d9fbe880bc18b167e2aac06d733ce
    r = requests.get('http://otpsim.com/api/sessions/'+session+'?token='+token)
    r = r.json()
    status = r['data']['status']
    if int(status) == 0:
        otp = r['data']['messages']
        otp = otp[0]
        otp = otp['otp']
    else:
        otp = "nothing !"
    return [status, otp]

def check_otp(token, session):
    c = get_code(token, session)
    time.sleep(120, 139)
    if c[0] == 0:
        return c[1]
    else:
        requests.get('http://otpsim.com/api/sessions/cancel?session='+session+'&token='+token)
        p = get_phone(token)
        session2 = p[1]
        time.sleep(59, 69)
        c = get_code(token, session2)
        if c[0] == 0:
            return c[1]
        else:
            return ["khong thanh cong"]

#i = get_phone('b5e5e8e4b890df61edb02bdff2d61863')
#print(check_otp('b5e5e8e4b890df61edb02bdff2d61863', i[1]))
#print(check_service("06211ab751329954877f704596317eaa"))
