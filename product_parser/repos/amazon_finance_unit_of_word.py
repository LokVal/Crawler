from typing import Final

from product_parser.repos.competitors_repository import CompetitorsRepository


class AmazonFinanceUnitOfWork:
    _db_alias: Final = 'amazon_finance'
    _competitors: CompetitorsRepository

    @property
    def competitors(self) -> CompetitorsRepository:
        if self._competitors is None:
            self._competitors = CompetitorsRepository(self._db_alias)
        return self._competitors
