import ssl
import requests
import json
import time


from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from urllib3.util import ssl_


# Получение доступа к Avito обход, антибота

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
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "content-type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "x-source": "client-browser",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },)
    
    params = {"categoryId": "9",
			"locationId": "652000",
			"radius": "200",
			"user": "1",
			"cd": "1",
			"s": "101",
			"p": "1",
			"params[697]": "8856",
			"params[1375][from]": "0",
			"params[1375][to]": "15544",
			"params[110000]": "329273",
			"params[110001]": "330296",
			"params[110005]": "333431",
			"params[110006][0]": "331247",
			"params[110907][0]": "478239",
			"verticalCategoryId": "0",
			"rootCategoryId": "1",
			"localPriority": "0",
			"countOnly": "1"}
    params2 = {
	
			"_": "",
			"categoryId": "9", # Автомобиль
			"locationId": "652000", #Ростов-на-дону
			"radius": "200", # радиус в км от локации
			"pmin": "200000", # мин цена
			"pmax": "1000000", # мах цена
			"user": "1", #
			"cd": "1", #
			"s": "101", # поиск (сортировка 101 по умолчанию)
			"p": "1", # 
			"params[697]": "8856", #
			"params[1375][to]": "15544", # пробег до 200 000 км 
			"params[110000]": "329306", # марка
			"params[110001]": "330849", # модель
			"params[110005]": "335408", # покoление
			"params[110006][0]": "331247", # тип двигателя
			"params[110907][0]": "478239", # регистрация авто
			"verticalCategoryId": "0", #
			"rootCategoryId": "1", #
			"localPriority": "0", #
			"countOnly": "1" #
		},
    # Все параметры фильтров 
    catalog = 'https://www.avito.ru/search/filters/list?_=&categoryId=9&locationId=652000&searchRadius=200&correctorMode=1&sort=101&page=1&verticalCategoryId=0&rootCategoryId=1&localPriority=0&currentPage=&filtersGroup=desktop_catalog_filters'
    city = 'Таганрог'
    location = 'https://www.avito.ru/web/1/slocations?locationId=652000&limit=10&q={}'.format(city)
    try:
        response = session.get('https://www.avito.ru/web/1/js/items', params=params) # Получаю json ответ 
        return (response.json())['url']
    except Exception as exception:
        print(exception)

print(getPageAvito())
'''
await fetch("https://www.avito.ru/web/1/slocations?locationId=652000&limit=10&q=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "content-type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "x-source": "client-browser",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },
    "referrer": "https://www.avito.ru/rostov-na-donu/avtomobili?cd=1&radius=200",
    "method": "GET",
    "mode": "cors"
});
'''