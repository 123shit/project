import socketserver
import socket
from classes.EASecure import EASecure
import logging

_key = '29dQrqxAJOgHA3IC5kXYNscvfjAOEB7u'
_lineBr = '<-------------------------------------'

# Socket服务
class EASProxyServer(socketserver.BaseRequestHandler):

    EASecure = EASecure()

    # 发送数据到Mt4Server
    def SendMt4Server(self, Message):
        logging.info("Server Transmit Data: {}".format(Message))
        try:
            Mt4Connection = socket.socket()
            Mt4Connection.connect(("103.242.72.46", 9501))  # 主动初始化与服务器端的连接
            bMessage = []
            for tmp in Message:
                if tmp == 124:
                    print(1)
                    break
                else:
                    bMessage.append(tmp)
            bMessage = bytes(bMessage)
            # bMessage = b'\x02\x00\x00\x00\x07\x010\xe7\x03\x00\x00\x03'
            Mt4Connection.send(bMessage)
            RespData = Mt4Connection.recv(1024)
            logging.info("Server Response Success: {}".format(RespData))
            Mt4Connection.close()
            return RespData
        except Exception as Err:
            logging.critical("Server Send Err: {}".format(Err))
            return b''

    def wLog(self, Addr, Message):
        logging.info("Client <{}> {}".format(Addr, Message))
        return

    # 创建一个类，继承自socketserver模块下的BaseRequestHandler类
    def handle(self):
        # 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
        while 1:
            conn = self.request
            Addr = self.client_address
            IpAddress = Addr[0]
            IpPort = Addr[1]
            # 上面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法
            while 1:
                try:

                    Buffer = conn.recv(1024)
                    if Buffer == b'':
                        conn.close()
                        self.wLog(IpAddress, "Disconnected!")
                        logging.info(_lineBr)
                        return

                    # log
                    self.wLog(IpAddress, "Get Data {}".format(Buffer))

                    # 安全过滤
                    CheckVail = self.EASecure.filter(self.EASecure.getSerial(Buffer), IpAddress)

                    if not CheckVail:
                        logging.critical("Go to Hell {}:{}".format(IpAddress, IpPort))
                        logging.info(_lineBr)
                        conn.close()
                        return False

                    # 检查数据签名
                    CheckSign = self.EASecure.checkSign(Buffer, _key)
                    if not CheckSign:
                        self.wLog(IpAddress, "CheckSign Failed!")
                        logging.info(_lineBr)
                    self.wLog(IpAddress, "CheckSign Success!")

                    # 发送数据给Mt4
                    RespData = self.SendMt4Server(Buffer)
                    conn.sendall(RespData)
                    conn.close()
                    logging.info(_lineBr)
                    return

                except ConnectionAbortedError as Err:
                    self.wLog(IpAddress, "Disconnected!")
                    logging.info(_lineBr)
                    return