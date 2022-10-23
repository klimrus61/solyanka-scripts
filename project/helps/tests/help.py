import requests, json, sys

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir' # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie = 'tmr_reqNum=4; cfidsw-avito=CaU9wrN3ZoIlaNkCL/Oq+7eAM/PG88bRIzBkTjLTCnTH//pdUC5ibFU6oNjMxqjZHhJeKltQd/6M3rKMiR37/tYkVcfvWWu3Z+LrEbFT57e6rTKb8zW6lpKN11NQdHCeppjijieYf/RHiP+mqCaOoMd3ZhArXkMZcqEeHg==; fgsscw-avito=yPZw4a18e0674fc175b39da192c975369a8f85f7; gsscw-avito=iL63JSxLFiZGT04W7MAwtQsNGhjYnRkjNYEJGvcSU74ABmThAucsKb9Gu/n6tmmUZRHMiRp6UmsWUO3moVnpy4hd58CZyXwgyHkVqcneQeKEfRHp+Ycw9hkuQN0hz21L2UX5b9BJEdwGZs6pMgKMLDjaC3bkkVIuQhjPyVHBjMEpCpYzdXUMM/jp8yJlvuILMS+FIsIA8ZzARv7/GI7Sh/erOMtLvHZmJ/BSiLwNzGLbct/J5KEhJJxD…032732732629d599154f4aaf0a7b4f49f1d8b2afcb5aedc413853268fd398da2ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd74865cea24febc6ca6a3de19da9ed218fe23de19da9ed218fe2aa6f746d757dff059427383f0d84727ce8f5c0f5d0d8fa02; ft="e91rfG3d8xpbufLnNqZ2hsjd+xVxx/0wziZtZ7DH6Dawei0sDJnF5n0+8j0pG8tykur0shbkxrJYoIxr5GfbUBAiVADvpWSQK6T6QVFFFz04CKjoNnYeiLybfFSyvcEICqPFq2x5Vx6RbClEHC6T6V5Icc5MXXbPZLgEOMNtchTKQtcUZmSWC7St3JTsZ7zS"; sessid=ef466c98a77c3f101bfb014ead20e497.1663234977; auth=1; redirectMav=1; v=1663256979' 
# Если забанили, то добавьте свои куки, это не боевой код но он делает то, что надо
search = 'suzuki+gsx-r'     # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = 14
locationId = 641780         # Новосибирск
searchRadius = 200
priceMin = 200000
priceMax = 450000
sort = 'priceDesc'
withImagesOnly = 'true'     # Только с фото
limit_page = 50     # Количество объявлений на странице 50 максимум

def except_error(res): # Эту функцию можно дополнить, например обработку капчи
    print(res.status_code, res.text)
    sys.exit(1)

s = requests.Session()                          # Будем всё делать в рамках одной сессии
# Задаем заголовки:
headers = { 'authority': 'm.avito.ru',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9',}
if cookie:                                      # Добавим куки, если есть внешние куки
    headers['cookie'] = cookie
s.headers.update(headers)                       # Сохраняем заголовки в сессию
s.get('https://m.avito.ru/')                    # Делаем запрос на мобильную версию.
url_api_9 = 'https://m.avito.ru/api/9/items'    # Урл первого API, позволяет получить id и url объявлений по заданным фильтрам
                                                # Тут уже видно цену и название объявлений
params = {
    'categoryId': 14,
    'params[30]': 4969,
    'locationId': locationId,
    'searchRadius': searchRadius,
    'priceMin': priceMin,
    'priceMax': priceMax,
    'params[110275]': 426645,
    'sort': sort,
    'withImagesOnly': withImagesOnly,
    'lastStamp': 1610905380,
    'display': 'list',
    'limit': limit_page,
    'query': search,
}
cicle_stop = True       # Переменная для остановки цикла
cikle = 0               # Переменная для перебора страниц с объявлениями
items = []              # Список, куда складываем объявления
params['key'] =  key
while cicle_stop:
    cikle += 1          # Так как страницы начинаются с 1, то сразу же итерируем
    params['page'] = cikle
    res = s.get(url_api_9, params=params)
    try:
        res = res.json()
    except json.decoder.JSONDecodeError:
        except_error(res)
    if res['status'] != 'ok':
            print(res['result'])
            sys.exit(1)
    if res['status'] == 'ok':
        items_page = int(len(res['result']['items']))

        if items_page > limit_page: # проверка на "snippet"
            items_page = items_page - 1

        for item in res['result']['items']:
            if item['type'] == 'item':
                items.append(item)
        if items_page < limit_page:
            cicle_stop = False
####################################################################
params = {'key': key}
for i in items: # Теперь идем по ябъявлениям:
    ad_id = str(i['value']['id'])
    # url_more_data_1 = 'https://m.avito.ru/api/1/rmp/show/' + ad_id  # more_data_1 = s.get(url_more_data_1, params=params).json() # Тут тоже моного информации, можете посмотреть
    url_more_data_2 = 'https://m.avito.ru/api/15/items/' + ad_id
    more_data_2 = s.get(url_more_data_2, params=params).json()
    if not 'error' in more_data_2:
        # print(more_data_2)            # В more_data_2 есть всё, что надо, я вывел на принт наиболее интересные для наглядности:
        print(more_data_2['title'])
        print(more_data_2['price'])
        print(more_data_2['address'])
        url_get_phone = 'https://m.avito.ru/api/1/items/' + ad_id + '/phone'    # URL для получения телефона
        phone = s.get(url_get_phone, params=params).json()                      # Сам запрос
        if phone['status'] == 'ok': phone_number = requests.utils.unquote(phone['result']['action']['uri'].split('number=')[1]) # Прверка на наличие телефона, такой странный синтсксис, чтоб уместиться в 100 сторочек кода)))
        else: phone_number = phone['result']['message']
        print(phone_number)
        print(more_data_2['seller'])
        # print(more_data_2['description']) # Скрыл, т.к. много букв
        print('=======================================================\n')