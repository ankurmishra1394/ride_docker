import pika, os, json, sys
import subprocess

# credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='flas_engine_docker')

def callback(ch, method, properties, body):
	import uuid
	data = json.loads(body)
	
	file = open('/tmp/test_case_name.txt', 'w')
	file.write(data['robot_file_name']+'\n')
	file.close()

	file = open('/tmp/test_case_link.txt', 'w')
	file.write(data['self_link']+'\n')
	file.close()

	file = open('/tmp/test_case_path.txt', 'w')
	file.write(data['path']+'\n')
	file.close()
	sys.exit(0)

channel.basic_consume(callback,queue='flas_engine_docker',no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()