import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('/Users/asaquelares/Documents/python-training/pytestDemo/BackendAutomation/utilities/properties.ini')
    return config


connect_config = {
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database']
}


def get_password():
    return 'API key for github'


def get_connection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def get_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

