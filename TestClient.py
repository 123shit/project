import socket
import time
from classes.EASecure import EASecure

EASecure = EASecure()

testKey = '29dQrqxAJOgHA3IC5kXYNscvfjAOEB7u'
testData = '02000000070134e703000003|1495641323|9053b4190992e6daacd2ab1725e0dae0'

# 测试签名算法
SignCheck = EASecure.checkSign(testData, testKey)

if(SignCheck):
    print("Sign Check Success!")
else:
    print("Fuck")

sk = socket.socket()
sk.connect(("127.0.0.1", 9071))  # 主动初始化与服务器端的连接
# 原始数据
rawdata = '02000000070134e703000003'
# 时间戳 1495639878
time = str(int(time.time()))
# 签名使用数据
data = rawdata + '|' + time
# 进行签名
sign = EASecure.createSign(data, testKey)
# 最终发送的数据 b'02000000070134e703000003|1495639878|fb002ebf140bfd3a4391f9dbe244f22e'
finalData = data + '|' + sign
sk.send(bytes(finalData, encoding="utf8"))
accept_data = sk.recv(1024)
print(str(accept_data, encoding="utf8"))
sk.close()