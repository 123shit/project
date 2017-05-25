import hashlib

# 安全类
class EASecure():

    def __init__(self):
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

    # 检查签名
    def checkSign(self, OriginData, Key):
        # 数据分割
        Sp = str(OriginData).split('|')
        # 待签名数据
        Signed = self.createSign(Sp[2], Key)
        # 校验签名
        return Signed == Sp[1]