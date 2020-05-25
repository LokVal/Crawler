from dataclasses import dataclass
from typing import List, Final

from django.db import connections


@dataclass
class Competitor:
    id: int
    asin: str


class CompetitorsRepository:
    _table_name: Final = 'Competitors'
    _db_alias: str = None

    @property
    def connection(self):
        return connections[self._db_alias]

    def __init__(self, db_alias: str):
        self._db_alias = db_alias

    def get_all(self) -> List:
        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT ID, ASIN FROM {self._table_name}')
            columns = self._get_columns(cursor)
            return [
                self._map(columns, row)
                for row in cursor.fetchall()
            ]

    def get_all_new(self, existing: Competitor) -> List:
        return [
            item
            for item in self.get_all()
            if item not in existing
        ]

    @staticmethod
    def _get_columns(cursor):
        return [col[0] for col in cursor.description]

    @staticmethod
    def _map(row, columns):
        return Competitor(
            **dict(
                zip(columns, row)
            )
        )
