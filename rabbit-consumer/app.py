import pika, os

RABBITMQ_SERVICE_HOST = os.environ.get('RABBITMQ_SERVICE_HOST', 'localhost')
RABBITMQ_AUTH_USERNAME = os.environ.get('RABBITMQ_AUTH_USERNAME', 'user')
RABBITMQ_AUTH_PASSWORD = os.environ.get('RABBITMQ_AUTH_PASSWORD', '')

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_SERVICE_HOST,
        credentials=pika.PlainCredentials(RABBITMQ_AUTH_USERNAME, RABBITMQ_AUTH_PASSWORD)
    ))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f'Received message {body}')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print('Started consumer')

    channel.start_consuming()

if __name__ == '__main__':
    main()