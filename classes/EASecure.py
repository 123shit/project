import hashlib
import redis
import platform
import os
import logging

# 安全类
class EASecure():

    _redis = False

    def __init__(self):
        self._redis = redis.Redis(host='127.0.0.1', port=6379)
        return

    def md5(self, String):
        m = hashlib.md5()
        m.update(bytes(String, encoding="utf8"))
        return m.hexdigest()

    # 数据签名
    def createSign(self, RawData, Key):
        RawData = RawData.replace("'", '')
        return self.md5('|' +RawData + '|' + Key)

    # 拆分原始数据
    def getOriginData(self, OriginData):
        # 数据分割
        Sp = str(OriginData).split('|')
        # 校验签名
        return Sp[0]

    # 获取序列号
    def getSerial(self, OriginData):
        # 数据分割
        Sp = str(OriginData).split('|')
        if len(Sp) < 3:
            return False
        # 校验签名
        return Sp[2]

    # 检查签名
    def checkSign(self, OriginData, Key):
        # 数据分割
        Sp = str(OriginData).split('|')
        if len(Sp) < 3:
            return False
        # 待签名数据
        Signed = self.createSign(Sp[2], Key)
        # 校验签名
        return Signed == Sp[1]

    # 安全过滤
    def filter(self, Hash, Ip):

        if Hash is False:
            Hash = 'invaild-params'

        key = 'ea-filter-{}-{}'.format(Hash, Ip)
        keyIp = 'ea-filter-{}'.format(Ip)

        Ext = self._redis.get(key)
        ExtIp = self._redis.get(keyIp)

        if ExtIp is None:
            self._redis.incr(keyIp, 1)
            self._redis.expire(keyIp, 60)
            return True

        if Ext is None:
            self._redis.incr(key, 1)
            self._redis.expire(key, 60)
            return True

        # 判断是否要黑洞
        if int(Ext) > 3:
            self.blackHole(Ip)
            return False
        else:
            self._redis.incr(key, 1)

        # ip过滤
        if int(ExtIp) > 30:
            self.blackHole(Ip)
            return False
        else:
            self._redis.incr(keyIp, 1)

        return True

    def blackHole(self, Ip):
        logging.critical("{} Has Been Block!".format(Ip))
        if platform.system() == "Linux":
            # 屏蔽IP
            os.system("ufw deny from {} to any".format(Ip))