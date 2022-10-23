from bs4 import BeautifulSoup

with open('/home/klim/project/html_page_parse.txt', 'r') as f:
    html_page = f.read()
    soup = BeautifulSoup(html_page, 'html.parser')
    cars = soup.find_all('div', attrs={'class': 'iva-item-titleStep-pdebR'})
    cars_info = []
    for car in cars:
        cars_info.append({
            'id': car.parent.parent.parent['id'],
            'title': car.a.h3.text, 
            'uri': car.a['href'],
            'specific': car.next_sibling.next_sibling.next_sibling.div.string,
            'text': car.next_sibling.next_sibling.next_sibling.next_sibling.text,
            'location': car.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text,
            'datatime': car.parent.find('span', attrs={'class': 'text-text-LurtD text-size-s-BxGpL text-color-inverted-ZPNb_'}),
            'price': car.next_sibling.span.span.meta.next_sibling['content'],
            })
            
    print(cars_info[0]['datatime'].prettify())