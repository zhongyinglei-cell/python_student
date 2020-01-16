import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel() # 建立管道
channel.queue_declare(queue='hello') # 声明管道

def callback(ch,method,properties,body):
    print('[x]Received %r'%body)
channel.basic_consume(queue='hello',auto_ack=True,on_message_callback=callback)

print('[*]Waiting for messages.To exit press CTRL+C')
channel.start_consuming()
