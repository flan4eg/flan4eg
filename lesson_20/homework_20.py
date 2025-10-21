from dotenv import load_dotenv
import os
import psycopg2
import pytest


load_dotenv()

@pytest.fixture(scope="session")
def open_close_connection():
    dbname = 'postgres'
    user = 'postgres.yeztcaoftcgbqsblfqvn'
    password = os.getenv('PGpassword')

    host = 'aws-1-eu-central-1.pooler.supabase.com'
    port = '5432'

    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    print("Connected to the database successfully!")

    cursor = connection.cursor()

    yield connection, cursor

    connection.close()
    cursor.close()

def test_connection(open_close_connection):
    connection, cursor = open_close_connection

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record)


def test_version(open_close_connection):
    connection, cursor = open_close_connection
    cursor.execute("SELECT version();")
