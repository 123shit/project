import socketserver
# 导入socketserver模块
from classes.EASProxyServer import EASProxyServer
import logging

# 入口类
class EASProxy():

    _socket = False
    _socketListen = '0.0.0.0'
    _socketPort = 9516

    def __init__(self):
        return

    def run(self):
        # 通过调用对象的serve_forever()方法来激活服务端
        logging.info("Listening {} On [{}]".format(self._socketListen, self._socketPort))
        sever = socketserver.ThreadingTCPServer((self._socketListen, self._socketPort), EASProxyServer)
        # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
        sever.serve_forever()
        return