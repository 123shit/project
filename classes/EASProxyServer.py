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
        try:
            Mt4Connection = socket.socket()
            Mt4Connection.connect(("fin.ds.fincdn.com", 443))  # 主动初始化与服务器端的连接
            Mt4Connection.send(bytes(Message, encoding="utf8"))
            RespData = Mt4Connection.recv(1024)
            logging.debug(str(RespData, encoding="utf8"))
            logging.info("Server Response Success: {}".format(RespData))
            Mt4Connection.close()
        except Exception as Err:
            logging.critical("Server Send Err: {}".format(Err))
        logging.info("Server Transmit Data: {}".format(Message))

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

                    Buffer = conn.recv(2048)
                    if Buffer == b'':
                        conn.close()
                        self.wLog(IpAddress, "Disconnected!")
                        logging.info(_lineBr)
                        return

                    # 处理客户端的消息
                    AcceptData = str(Buffer, encoding="utf8")

                    # log
                    self.wLog(IpAddress, "Get Data {}".format(AcceptData))

                    # 检查数据签名
                    CheckSign = self.EASecure.checkSign(AcceptData, _key)
                    if not CheckSign:
                        self.wLog(IpAddress, "CheckSign Failed!")
                        logging.info(_lineBr)
                    self.wLog(IpAddress, "CheckSign Success!")

                    # 发送数据给Mt4
                    self.SendMt4Server(self.EASecure.getOriginData(AcceptData))

                    send_data = bytes("Success", encoding="utf8")
                    conn.sendall(send_data)
                except ConnectionAbortedError as Err:
                    self.wLog(IpAddress, "Disconnected!")
                    logging.info(_lineBr)
                    return