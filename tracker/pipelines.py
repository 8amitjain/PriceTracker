# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class TrackerPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("tracker.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tracker""")
        self.curr.execute("""
                            create table tracker(
                            product_name text,
                            product_price text,
                            product_sold_by text)
                          """)

    def store_db(self, item):
        self.curr.execute("""insert into tracker values(?,?,?)""", (
                            item['product_name'][0].strip(),
                            item['product_price'][0].strip(),
                            item['product_sold_by'][0].strip(),
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        print('Pipeline:' + item['product_name'][0].strip())
        print('Pipeline:' + item['product_price'][0].strip())
        print('Pipeline:' + item['product_sold_by'][0].strip())
        print(item['product_image_link'])
        return item
