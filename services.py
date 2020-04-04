from typing import List

from models import Product


class ProductService:
    def __init__(self, cursor):
        self._cursor = cursor

    def get(self, id: str):
        self._cursor.execute('SELECT * FROM product WHERE ID = %s', id)
        return Product(*self._cursor.fetchone())

    def get_all(self, skip: int = 0, take: int = 100) -> List:
        self._cursor.execute('SELECT * FROM product OFFSET %s LIMIT %s', (skip, take))
        return [Product(*value) for value in self._cursor.fetchall()]

    def insert(self, **kwargs) -> None:
        keys = kwargs.keys()
        columns = ', '.join(keys)
        values = ','.join([f'%({k})s' for k in keys])
        insert = 'insert into product({0}) values ({1})'.format(columns, values)
        self._cursor.execute(insert, kwargs)
