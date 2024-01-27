import psycopg2
import json
import getpass

config = json.load(open('config.json'))
user = input('Username: ')
password = getpass.getpass()

try:
    connection = psycopg2.connect(host=config['host'],
        database=config['db_name'], port=config['port'],
        user=user, password=password)

    with connection.cursor() as cursor:
        cursor.execute('SELECT version();')
        print(f'{cursor.fetchone()}')

except Exception as _ex:
    print('Error while connecting to Postgres', _ex)
finally:
    if connection: connection.close()



