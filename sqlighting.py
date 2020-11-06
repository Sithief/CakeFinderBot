import sqlite3


class SQLighting:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_product(self, article, product_name, description, image, price, status):
        with self.connection:
            product = (article, product_name, description, image, price, status)
            return self.cursor.execute("INSERT INTO `catalog` VALUES (?,?,?,?,?,?);", product)

    def get_products(self):
        with self.connection:
            result = self.cursor.execute('SELECT `product` FROM `catalog`').fetchall()
            return result

    def close(self):
        self.connection.close()