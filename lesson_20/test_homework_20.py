from dotenv import load_dotenv
import os
import psycopg2
import pytest
import allure

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



@allure.epic("DB testing")
@allure.feature("Postgres connection")
@allure.story("Check connection")
def test_connection(open_close_connection):
    connection, cursor = open_close_connection
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record)


@allure.epic("DB testing")
@allure.feature("Postgres connection")
@allure.story("Check version")
def test_version(open_close_connection):
    connection, cursor = open_close_connection
    cursor.execute("SELECT version();")



@allure.epic("DB testing")
@allure.feature("Check INSERT, SELECT, DELETE")
@allure.story("Categories table")
def test_categories(open_close_connection):
    connection, cursor = open_close_connection
    table_name = "public.categories"
    category_name = "Illumination"
    cursor.execute(f"""insert into {table_name} ("category_name") values ('{category_name}')""")
    cursor.execute(f"""select * from {table_name} where category_name = \'{category_name}\'""")

    record = cursor.fetchone()
    assert len(record) > 0
    print("You have added ", record)

    cursor.execute(f"""delete from {table_name} where category_name = \'{category_name}\'""")
    connection.commit()


@allure.epic("DB testing")
@allure.feature("Check INSERT, SELECT, DELETE")
@allure.story("Products table")
@allure.description("Insert products into table and delete them")
@allure.title("Insert value {product_name} into table")
def test_products(open_close_connection):
    connection, cursor = open_close_connection
    table_name = "public.products"
    product_name = "Lamp"
    cursor.execute(f"""insert into {table_name} (product_name, description, price, category_id) values ('Lamp', 'Lamp in Tiffany style', 200.00, 1)""")
    cursor.execute(f"""select * from {table_name} where product_name = \'{product_name}\'""")

    record = cursor.fetchone()
    assert len(record) > 0
    print("You have added ", record)

    cursor.execute(f"""delete from {table_name} where product_name = \'{product_name}\'""")
    connection.commit()
