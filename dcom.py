import subprocess as sp
from get_pic import *
import time
def up_reconnect():
    print(avata())
    print(avata())
    print(status())
    print(status())
    print(status())
    print(status())
    print(status())
    print(status())
    sp.call('rasdial /disconnect')
    time.sleep(5)
    sp.call('rasdial viettel')
    time.sleep(5)

def reconnect():
    sp.call('rasdial /disconnect')
    time.sleep(5)
    sp.call('rasdial viettel')
    time.sleep(5)
def reconnect_app(name_dcom):
    sp.call('rasdial /disconnect')
    time.sleep(5)
    sp.call('rasdial '+name_dcom)
    time.sleep(5)

#reconnect_app("viettel")