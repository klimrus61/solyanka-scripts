import ssl
import requests
import json
import time

from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from urllib3.util import ssl_


def getPageAvito(url: str = 'https://www.avito.ru', method: str = 'GET'):

    '''Доступ к авито страничке, возвращает response.content'''

    CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

    class TlsAdapter(HTTPAdapter):

        def __init__(self, ssl_options=0, **kwargs):
            self.ssl_options = ssl_options
            super(TlsAdapter, self).__init__(**kwargs)

        def init_poolmanager(self, *pool_args, **pool_kwargs):
            ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
            self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

    session = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)

    try:
        response = session.request(method, url)
        return response.content
    except Exception as exception:
        print(exception)

def parse_a_auto_page(url: str) -> list:
    '''
    Получает url с примененными фильтрами и парсит 
    '''
    html_page = getPageAvito(url=url)
    soup = BeautifulSoup(html_page, 'html.parser')
    cars = soup.find_all('div', attrs={'class': 'iva-item-titleStep-pdebR'}) # div блок 1 обьявления
    cars_info = []
    for car in cars:
        try:
            cars_info.append({
                'id': car.parent.parent.parent['id'],
                'title': car.a.h3.text, 
                'uri': car.a['href'],
                'specific': car.next_sibling.next_sibling.next_sibling.div.string, # Проход по дереву объекта soup в ширь, затем в глубину
                'text': car.next_sibling.next_sibling.next_sibling.next_sibling.text,
                'location': car.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,
                'price': car.next_sibling.span.span.meta.next_sibling['content'],
                })
        except:
            pass
    return cars_info



# response = getPageAvito('https://www.avito.ru/search/filters/list?_=&categoryId=9&locationId=652000&searchRadius=200&correctorMode=1&sort=101&page=1&verticalCategoryId=0&rootCategoryId=1&localPriority=0&currentPage=&filtersGroup=desktop_catalog_filters')
# decoded_response = response.decode('UTF-8')
# with open('list_filters.txt', 'w') as f:
#     f.write(decoded_response)

# from pprint import pprint

# with open('list_filters.txt', 'r') as f:
#     a = f.read()
# pprint(json.loads(a))

# pprint(parse_a_auto_page('https://www.avito.ru/rostov-na-donu/avtomobili?f=ASgBAgECBETyCrCKAYYUyOYB4LYNpIo09sQNvrA6AUXGmgwbeyJmcm9tIjoxMjIyLCJ0byI6NDMyNDIzNDF9&presentationType=serp&radius=200'))