from classes.EASProxy import EASProxy
from classes.Utils import Config
import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='proxy.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

if __name__ == '__main__':
    #kill监听端口进程
    # config = Config()
    # _listenPort = config.get('EASProxy', 'listen_port')
    # cmd = "kill -9 $(netstat -tlnp|grep "+_listenPort+"|awk '{print $7}'|awk -F '/' '{print $1}')"
    # print(cmd)
    # os.system(cmd)
    #启动
    ES = EASProxy()
    ES.run()