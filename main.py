import psycopg2
import requests
from dataclasses import dataclass
from bs4 import BeautifulSoup

from CONFIG import DB_CONNECTION_STRING
from services import ProductService


@dataclass
class TableItem:
    key: str
    value: str


def create_soup() -> BeautifulSoup:
    ASIN = 'B081CB3RJJ'
    url = 'https://www.amazon.com/dp/' + ASIN

    # url = 'https://www.amazon.com/CamelBak-Chute-Water-Bottle-Glass/dp/B07663TZNT/ref=sr_1_1?dchild=1&qid=1585992016&s=sporting-goods&sr=1-1'
    headers = {
        "User-Agent": 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    resp = requests.get(url, proxies={'socks5': '153.3.7.164:1080'})
    soup = BeautifulSoup(resp.content, features="lxml")

    if 'Sorry, we just need to make sure you\'re not a robot' in soup.text:
        raise Exception('The site thinks you are a robot.')

    return soup


def main() -> None:
    soup_outcome = create_soup()

    poduct_title= soup_outcome.select("#productTitle")[0].get_text().strip()
    print (poduct_title)
    poduct_price= soup_outcome.select("#priceblock_saleprice")[0].get_text().strip()
    print (poduct_price)
    poduct_reviews_number= soup_outcome.select("#acrCustomerReviewText")[0].get_text().strip()
    print (poduct_reviews_number)

    text_bullets = [
        b.text.replace('\n', '').replace('\t', '')
        for b in soup_outcome.select('#feature-bullets > ul > li > span')
        if len(list(b.children)) < 2
    ]

    print(text_bullets)

    values = [
        TableItem(
            t.findChild('th').text.replace('\n', '').replace('  ', ''),
            t.findChild('td').text.replace('\n', '').replace('  ', '')
        )
        for t in soup_outcome.select('.prodDetTable tr')
    ]

    print(values)

    with psycopg2.connect(DB_CONNECTION_STRING) as connection:
        with connection.cursor() as cursor:
            service = ProductService(cursor)
            #
            service.insert(asin='asdff', url='url1')
            print(service.get_all())


if __name__ == '__main__':
    main()
