import pika, os, time

RABBITMQ_SERVICE_HOST = os.environ.get('RABBITMQ_SERVICE_HOST', 'localhost')
RABBITMQ_SERVICE_PORT = os.environ.get('RABBITMQ_SERVICE_PORT', '5672')
RABBITMQ_AUTH_USERNAME = os.environ.get('RABBITMQ_AUTH_USERNAME', 'user')
RABBITMQ_AUTH_PASSWORD = os.environ.get('RABBITMQ_AUTH_PASSWORD', '')

def main():
    count = 0

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_SERVICE_HOST,
        credentials=pika.PlainCredentials(RABBITMQ_AUTH_USERNAME, RABBITMQ_AUTH_PASSWORD)
    ))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    while True:
        print('Sending message to queue')
        channel.basic_publish(exchange='', routing_key='hello', body=f'Hello {count}')
        time.sleep(1)

if __name__ == '__main__':
    main()