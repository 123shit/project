from classes.EASProxy import EASProxy
import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='proxy.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

if sys.argv[1] !=4:
    logging.critical('Param eer')
#每个分支修改运行文件名称，同时注意修改两个shell文件，每个分支不同的为本文件名称和配置信息
if __name__ == '__main__':

    ES = EASProxy()
    ES.run()