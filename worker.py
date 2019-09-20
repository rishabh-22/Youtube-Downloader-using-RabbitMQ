#!/user/bin/env python
import pika
import time
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue = 'hello', durable=True)

def callback(ch, method, properties, body):
    body = body.decode("utf-8")
    
    print(" [x] Received %r" % body)
    cmd = "youtube-dl {}".format(body)
    # call script
    
    os.system(cmd)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='hello', on_message_callback=callback)

print("press ctrl + C to stop.")

channel.start_consuming()
