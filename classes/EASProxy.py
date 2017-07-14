import socketserver
from classes.EASProxyServer import EASProxyServer
import logging
import sys
# 入口类
class EASProxy():

    _SocketListen = '0.0.0.0'
    _SocketPort = False

    def __init__(self):
        return

    def run(self):

        ParamListen=sys.argv[1]

        # 通过调用对象的serve_forever()方法来激活服务端
        logging.info("Listening {} On [{}]".format('0.0.0.0', ParamListen))
        sever = socketserver.ThreadingTCPServer((self._SocketListen,self._SocketPort),EASProxyServer)
        # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
        sever.serve_forever()
        return