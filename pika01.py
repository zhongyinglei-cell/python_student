import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel() # 建立管道
channel.queue_declare(queue='hello') # 声明管道
channel.basic_publish(exchange='',routing_key='hello',body='hello world!')
print('[x]Sent"hello world!"')
connection.close()