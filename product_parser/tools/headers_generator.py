from typing import Dict


class HeadersGenerator:
    def generate(self) -> Dict:
        return {
        'authority': 'www.amazon.com',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-dest': 'document',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept-language': 'en-US,en;q=0.9,uk;q=0.8,ru;q=0.7',
        'cookie': 'aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1584136628484-842485; aws-target-visitor-id=1584136628488-910020; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=343F4FAE4DFBB6C5-2DBC08C3187E5855; s_vn=1615672628845%26vn%3D1; regStatus=pre-register; s_dslv=1584136687195; s_nr=1584136687197-New; session-id=140-6236298-9064037; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:UA"; ubid-main=132-0403673-2092729; x-wl-uid=1G1OPZI2gtItset8H7bq4I1GRjYN/W6imr+8TXpzBhx8hX4EDtsxUX6DF1GJCrIGM2gTmjKXBmuY=; session-token=ECVeehAns47LjabM7f8yQBMVTV1jDM+/SJaRTsI4bPOkNPvbdUZfxNzlRP/beEROP/0MI/XFnluvXhO9qUvPCkJzUcOcUkI/uWiTYTaxB+W45/XHpXrNGXTaXzENna2fxU0i2IyeAr7ZgAQJ2HX0XjIrGBPlZc0yGKMk8Br7STcehFEHlMh9UNimZ9SqmSRW; csm-hit=tb:s-1XTNE521J6P4B0Z5NJ49|1586615246046&t:1586615246901&adb:adblk_yes; cdn-session=AK-3db23fffe4d723aa39cad73a24dd15e8',
    }
