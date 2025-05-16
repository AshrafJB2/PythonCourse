import requests
import random
import psycopg2

# PostgreSQL connection settings
DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "ashraf2003"
HOST = "localhost"
PORT = "5432"

def connect():
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return connection, connection.cursor()

def fetch_random_countries(n=10):
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = response.json()
    return random.sample(countries, n)

def insert_country_data(country):
    connection, cursor = connect()
    try:
        name = country.get('name', {}).get('common', 'N/A')
        capital = country.get('capital', ['N/A'])[0]
        flag = country.get('flags', {}).get('png', 'N/A')
        subregion = country.get('subregion', 'N/A')
        population = country.get('population', 0)

        query = """
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, capital, flag, subregion, population))
        connection.commit()
    except Exception as e:
        print(f"Error inserting {name}: {e}")
    finally:
        connection.close()

def main():
    countries = fetch_random_countries(10)
    for country in countries:
        insert_country_data(country)
    print("10 random countries inserted successfully.")

if __name__ == "__main__":
    main()
