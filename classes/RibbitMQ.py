import pika
import pika.exceptions
import logging
from classes.Utils import Config

"""
RabbitMQ
"""
class Rabbit:

    _channel = False

    _connection = False

    def __init__(self):
        # 启动连接
        return

    """
    发布消息
    """
    def publishMessage(self, message, exchange):
        """
        :param message: 消息体
        :return: 执行结果
        """
        result = self._channel.basic_publish(
            exchange=exchange,
            routing_key='',
            body=message
        )
        return result

    """
    消费消息
    """
    def comsumeMessage(self, _callback, QueueName):
        for method_frame, properties, body in self._channel.consume(QueueName):
            try:
                # 消息ACK，确认已经处理
                self.askMessage(method_frame.delivery_tag)
                _callback(body)
            except Exception as Err:
                raise Err

    # 消息ACK，确认已经处理
    def askMessage(self, delivery_tag):
        self._channel.basic_ack(delivery_tag)

    """
    连接到rabbitMQ
    """
    def initConnection(self):
        config = Config()
        logging.info("Connecting to RabbitMQ [{}:{}]".format(config.get('RabbitMQ', 'host'), config.get('RabbitMQ', 'port')))
        credentials = pika.PlainCredentials(config.get('RabbitMQ', 'user'), config.get('RabbitMQ', 'pass'))
        try:
            self._connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=config.get('RabbitMQ', 'host'),
                port=config.getInt('RabbitMQ', 'port'),
                credentials= credentials,
                virtual_host=config.get('RabbitMQ', 'vhost'))
            )
            self._channel = self._connection.channel()
            logging.info("Connecting to RabbitMQ Success")
            return True
        except pika.exceptions.ConnectionClosed as Err:
            logging.critical("Connecting to RabbitMQ Failed")
        except Exception as Err:
            logging.critical("Connecting to RabbitMQ Failed Unknow Err!")
        return False
