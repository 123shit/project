import socket
import time
from classes.EASecure import EASecure

EASecure = EASecure()

testKey = '29dQrqxAJOgHA3IC5kXYNscvfjAOEB7u'
Buffer = b'\x02\x00\x00\x00\x07\x010\xe7\x03\x00\x00\x03|d14c4814e3834bc508ba8be48b1ea99a|99920170525.13:54:24.98541'

# 安全过滤
CheckVail = EASecure.filter(EASecure.getSerial(Buffer), '127.0.0.1')

print(CheckVail)