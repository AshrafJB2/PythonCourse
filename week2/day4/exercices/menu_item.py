import psycopg2

DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "ashraf2003"
HOST = "localhost"
PORT = "5432"

def connect():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        print(f"Connection Error: {e}")
        return None, None

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        connection, cursor = connect()
        if connection is None:
            return
        try:
            query = '''
                INSERT INTO Menu_Items (item_name, item_price)
                VALUES (%s, %s)
            '''
            cursor.execute(query, (self.name, self.price))
            connection.commit()
        except Exception as e:
            print(f"Save Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection, cursor = connect()
        if connection is None:
            return
        try:
            query = '''
                DELETE FROM Menu_Items WHERE item_name = %s
            '''
            cursor.execute(query, (self.name,))
            connection.commit()
        except Exception as e:
            print(f"Delete Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def update(self, new_name, new_price):
        connection, cursor = connect()
        if connection is None:
            return
        try:
            query = '''
                UPDATE Menu_Items
                SET item_name = %s, item_price = %s
                WHERE item_name = %s
            '''
            cursor.execute(query, (new_name, new_price, self.name))
            connection.commit()
            self.name = new_name
            self.price = new_price
        except Exception as e:
            print(f"Update Error: {e}")
        finally:
            cursor.close()
            connection.close()
