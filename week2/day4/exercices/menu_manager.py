from menu_item import connect, MenuItem

class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        connection, cursor = connect()
        if connection is None:
            return None
        try:
            query = '''
                SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s
            '''
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            if result:
                return MenuItem(result[0], result[1])
            else:
                return None
        except Exception as e:
            print(f"get_by_name Error: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def all(cls):
        connection, cursor = connect()
        if connection is None:
            return []
        try:
            query = '''
                SELECT item_name, item_price FROM Menu_Items
            '''
            cursor.execute(query)
            results = cursor.fetchall()
            return [MenuItem(name, price) for name, price in results]
        except Exception as e:
            print(f"all_items Error: {e}")
            return []
        finally:
            cursor.close()
            connection.close()
