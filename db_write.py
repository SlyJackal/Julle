import os
import psycopg2
from os import getenv


class data_writer():
    def __init__(self, shop, itemid, price, link, brand, product_name, size, units):
        self.shop = shop
        self.itemid = itemid
        self.price = price
        self.link = link
        self.brand = brand
        self.product_name = product_name
        self.size = size
        self.units = units
    
    def connection(self):
        try:      
            login = getenv('login')
            password = getenv('password')
            conn = psycopg2.connect(f'postgresql://{login}:{password}@localhost:5432/julle')
            #print('Connected to database julle')        
        except:
            print('Can`t establish connection to database')
        
        return conn

    def write(self):
        # connect
        conn = self.connection()
        cursor = conn.cursor()
        # write data
        with cursor as curs:
            curs.execute("INSERT INTO actual_data (shop, itemid, price, link, brand, product_name, size, units) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                         (self.shop, self.itemid, self.price, self.link, self.brand, self.product_name, self.size, self.units))
            #print('data_write_in_db')
        # save changes
        conn.commit()

        
        # close connection
        conn.close()
