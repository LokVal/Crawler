from typing import Dict, List

from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from crawler.products.detail_parser import DetailParser
import re
from dataclasses import dataclass

from crawler.products.models import Product, CrawlingTask


# class ProductViewSet(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      viewsets.GenericViewSet):
    # queryset = Product.objects.all()
    #
    #
    # def create_headers(self) -> Dict:
    #     return {
    #         'authority': 'www.amazon.com',
    #         'cache-control': 'max-age=0',
    #         'dnt': '1',
    #         'upgrade-insecure-requests': '1',
    #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    #         'sec-fetch-dest': 'document',
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'sec-fetch-site': 'none',
    #         'sec-fetch-mode': 'navigate',
    #         'sec-fetch-user': '?1',
    #         'accept-language': 'en-US,en;q=0.9,uk;q=0.8,ru;q=0.7',
    #         'cookie': 'aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1584136628484-842485; aws-target-visitor-id=1584136628488-910020; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=343F4FAE4DFBB6C5-2DBC08C3187E5855; s_vn=1615672628845%26vn%3D1; regStatus=pre-register; s_dslv=1584136687195; s_nr=1584136687197-New; session-id=140-6236298-9064037; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:UA"; ubid-main=132-0403673-2092729; x-wl-uid=1G1OPZI2gtItset8H7bq4I1GRjYN/W6imr+8TXpzBhx8hX4EDtsxUX6DF1GJCrIGM2gTmjKXBmuY=; session-token=ECVeehAns47LjabM7f8yQBMVTV1jDM+/SJaRTsI4bPOkNPvbdUZfxNzlRP/beEROP/0MI/XFnluvXhO9qUvPCkJzUcOcUkI/uWiTYTaxB+W45/XHpXrNGXTaXzENna2fxU0i2IyeAr7ZgAQJ2HX0XjIrGBPlZc0yGKMk8Br7STcehFEHlMh9UNimZ9SqmSRW; csm-hit=tb:s-1XTNE521J6P4B0Z5NJ49|1586615246046&t:1586615246901&adb:adblk_yes; cdn-session=AK-3db23fffe4d723aa39cad73a24dd15e8',
    #     }
    #
    #
    # def parse(self, headers, url) -> Product:
    #     resp = requests.get(url, headers=headers)
    #     parser = DetailParser(str(resp.content))
    #     detail = parser.parse()
    #     product_title = detail.get('title')
    #     product_reviews_number = detail.get('reviews')
    #     price_elements = parser.selector.css('#priceblock_saleprice') or parser.selector.css('.offer-price')
    #     product_price = None
    #     if len(price_elements) > 0:
    #         product_price = price_elements[0].root.text
    #
    #     product = Product(
    #         product_title=product_title.strip().replace('\n', '').replace('\\n', '').replace('  ', ''),
    #         url=url,
    #         price=float(product_price.replace('$', '')),
    #         rating_amount=float(product_reviews_number or 0)
    #         )
    #
    #     def get_number(str_with_num) -> List[float]:
    #         return [item[1] if item[1] else item[0] for item in re.findall('(\d+\.\d+)|(\d+)', value)]
    #
    #     def get_first_float(numbers: List[float]) -> float:
    #         return float(str(numbers[0])) if len(numbers) else None
    #
    #     for key, value in detail['details'].items():
    #         if 'Shipping Weight' in key:
    #             numbers = get_number(value)
    #             product.shipping_weight = get_first_float(numbers)
    #         elif 'Weight' in key:
    #             numbers = get_number(value)
    #             product.weight = get_first_float(numbers)
    #         elif 'Dimensions' in key:
    #             numbers = get_number(value)
    #             product.dim_x, product.dim_y, product.dim_z = numbers
    #         elif 'model number' in key:
    #             product.model_number = value.replace('  ', '').replace('\n', '').replace('\\n', '')
    #         elif 'ASIN' in key:
    #             product.asin = value.replace('  ', '').replace('\n', '').replace('\\n', '')
    #         elif 'Best Sellers Rank' in key:
    #             numbers = get_number(value)
    #             product.bsr = get_first_float(numbers)
    #
    #
    # def list(self, request):
    #     # url = 'https://www.amazon.com/HONBAY-Convertible-Sectional-L-Shaped-Modern/dp/B07LBRDCTT/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=3733551&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=877c0809-fc53-42a6-91f2-7c8f50e6e9be&pf_rd_r=3ZTDAFY63JXZR72TRJ9G&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1586615936&refinements=p_n_feature_two_browse-bin%3A3248836011&rnid=3248834011&s=home-garden&sr=1-1'
    #     # url = 'https://www.amazon.com/dp/B081CB3RJJ'
    #     url = 'https://www.amazon.com/nuLOOM-HJZOM1B-Tufted-Classie-Multi/dp/B00AW0TX10/ref=sr_1_6?dchild=1&pf_rd_i=684541011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=00b00417-8753-4d7d-a195-6b32e72824d6&pf_rd_r=841BSQVSD4HS6DVDYN9B&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1586618338&refinements=p_28%3Ashag&s=home-garden&sr=1-6'
    #     headers = self.create_headers()
    #
    #     product = self.parse(headers, url)
    #     product.save()
    #
    #     return Response(product.__dict__)