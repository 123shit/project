import socket
import time
from classes.EASecure import EASecure

EASecure = EASecure()

testKey = '29dQrqxAJOgHA3IC5kXYNscvfjAOEB7u'
testData = b'\x02\x00\x00\x00\x07\x010\xe7\x03\x00\x00\x03|d14c4814e3834bc508ba8be48b1ea99a|999201705265.13:54:24.98541'

for i in range(0, 200):
    sk = socket.socket()
    sk.connect(("127.0.0.1", 9516))  # 主动初始化与服务器端的连接
    sk.send(b'\x02\x00\x00\x00\x07\x014\xe7\x03\x00\x00\x03|4ff3346768a408bd3342dd6972338ce6|99920170525.17:46:58.32612685000')
    accept_data = sk.recv(1024)
    print(accept_data)
    sk.close()

# sk = socket.socket()
# sk.connect(("103.242.72.46", 9501))  # 主动初始化与服务器端的连接
# sk.send(b'\x02\x00\x00\x00\x07\x010\xe7\x03\x00\x00\x03')
# accept_data = sk.recv(1024)
# print(accept_data)
# # print(str(accept_data, encoding="utf8"))
# sk.close()

# 测试签名算法
# SignCheck = EASecure.checkSign(testData, testKey)
#
# if(SignCheck):
#     print("Sign Check Success!")
# else:
#     print("Fuck")

# sk = socket.socket()
# sk.connect(("127.0.0.1", 9071))  # 主动初始化与服务器端的连接
# # 原始数据
# rawdata = '02000000070134e703000003'
# # 时间戳 1495639878
# time = str(int(time.time()))
# # 签名使用数据
# data = rawdata + '|' + time
# # 进行签名
# sign = EASecure.createSign(data, testKey)
# # 最终发送的数据 b'02000000070134e703000003|1495639878|fb002ebf140bfd3a4391f9dbe244f22e'
# finalData = data + '|' + sign
# sk.send(bytes(finalData, encoding="utf8"))
# accept_data = sk.recv(1024)
# print(str(accept_data, encoding="utf8"))
# sk.close()