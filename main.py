import requests
import json

def get_data(data_list: list, page_number: int):

    cookies = {
        'ngenix_jscv_2198e54375cc': 'cookie_expires=1703435928&bot_profile_check=true&cookie_signature=a6vNFIOs6Li6sBEc7k4qeEZhJbM%3D',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'advcake_track_id': '9b161c17-137f-6769-d450-a70071488abd',
        'advcake_session_id': '34cb9bd2-055d-16c7-cbc0-7a92beeb0ed7',
        '_userGUID': '0:lqjnmmw6:6r~sEDm276PmI5eAhwrER6p~9xweE~BS',
        'dSesn': '535679bb-72af-6f66-c07e-1a8421ec2b76',
        '_dvs': '0:lqjnmmw6:IF2XAFvOQi4_I~5veg~9x9u25QnVPP4A',
        'form_key': 'WqEpzfQW9rxrTHD7',
        'client-store-code': 'default',
        'private_content_version': 'need_version',
        'store': 'default',
        'PHPSESSID': '49244048fb83ec1976173be0092f7a41',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '1607432b-8bde-4e8e-ac40-0e7c7dd4d581',
        '_gid': 'GA1.2.194512935.1703432334',
        'mindboxDeviceUUID': 'e5596b35-84af-4483-8143-95f256467cb7',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22e5596b35-84af-4483-8143-95f256467cb7%22%7D',
        '_spx': 'eyJpZCI6ImNhOTk3Mjk4LTcyODEtNGM0My1hMTc1LWQyYzIzY2Q3ZGU2YyIsImZpeGVkIjp7InN0YWNrIjpbMF19fQ%3D%3D',
        '_ym_uid': '1703432334521123119',
        '_ym_d': '1703432334',
        'tmr_lvid': 'f2e5c2af89a0ea7a5939980a572bbe86',
        'tmr_lvidTS': '1703432333832',
        '_ym_isad': '2',
        '_ga': 'GA1.2.956595905.1703432334',
        'adid': '170343233583176',
        'adrdel': '1',
        'adrcid': 'A65Lm91OyOkNMLKRLme_zbA',
        'tmr_detect': '0%7C1703432337683',
        '_ga_QE5MQ8XJJK': 'GS1.1.1703432333.1.0.1703432341.0.0.0',
        'ga-lang': 'ru',
        'digi-analytics-sessionId': 'JDYnUVvHLO5nyFxoMMkut',
        'X-Magento-Vary': 'a0aa304f6a5a11a6e3340cfd05dccedca49f1a44',
        'rr_rcs': 'eF4NxTEOgCAQBMCGyr9swrIHhz_wGyKQWNip79dpJizXe5890leBHmUSa45JqAIYnmMzTjcxY5_sMOaBlpwYpei_cyZ-aocRGQ',
        'section_data_ids': '%7B%22directory-data%22%3A1703432331%2C%22messages%22%3A1703432331%2C%22customer%22%3A1703432331%2C%22compare-products%22%3A1703432331%2C%22last-ordered-items%22%3A1703432331%2C%22cart%22%3A1703433736%2C%22captcha%22%3A1703432331%2C%22wishlist%22%3A1703432331%2C%22multiplewishlist%22%3A1703432331%2C%22goldcards%22%3A1703432331%2C%22adult_goods%22%3A1703433735%2C%22geolocation%22%3A1703433734%2C%22recently_viewed_product%22%3A1703432331%2C%22recently_compared_product%22%3A1703432331%2C%22product_data_storage%22%3A1703432331%7D',
    }

    headers = {
        'authority': 'goldapple.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'ngenix_jscv_2198e54375cc=cookie_expires=1703435928&bot_profile_check=true&cookie_signature=a6vNFIOs6Li6sBEc7k4qeEZhJbM%3D; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; advcake_track_id=9b161c17-137f-6769-d450-a70071488abd; advcake_session_id=34cb9bd2-055d-16c7-cbc0-7a92beeb0ed7; _userGUID=0:lqjnmmw6:6r~sEDm276PmI5eAhwrER6p~9xweE~BS; dSesn=535679bb-72af-6f66-c07e-1a8421ec2b76; _dvs=0:lqjnmmw6:IF2XAFvOQi4_I~5veg~9x9u25QnVPP4A; form_key=WqEpzfQW9rxrTHD7; client-store-code=default; private_content_version=need_version; store=default; PHPSESSID=49244048fb83ec1976173be0092f7a41; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=1607432b-8bde-4e8e-ac40-0e7c7dd4d581; _gid=GA1.2.194512935.1703432334; mindboxDeviceUUID=e5596b35-84af-4483-8143-95f256467cb7; directCrm-session=%7B%22deviceGuid%22%3A%22e5596b35-84af-4483-8143-95f256467cb7%22%7D; _spx=eyJpZCI6ImNhOTk3Mjk4LTcyODEtNGM0My1hMTc1LWQyYzIzY2Q3ZGU2YyIsImZpeGVkIjp7InN0YWNrIjpbMF19fQ%3D%3D; _ym_uid=1703432334521123119; _ym_d=1703432334; tmr_lvid=f2e5c2af89a0ea7a5939980a572bbe86; tmr_lvidTS=1703432333832; _ym_isad=2; _ga=GA1.2.956595905.1703432334; adid=170343233583176; adrdel=1; adrcid=A65Lm91OyOkNMLKRLme_zbA; tmr_detect=0%7C1703432337683; _ga_QE5MQ8XJJK=GS1.1.1703432333.1.0.1703432341.0.0.0; ga-lang=ru; digi-analytics-sessionId=JDYnUVvHLO5nyFxoMMkut; X-Magento-Vary=a0aa304f6a5a11a6e3340cfd05dccedca49f1a44; rr_rcs=eF4NxTEOgCAQBMCGyr9swrIHhz_wGyKQWNip79dpJizXe5890leBHmUSa45JqAIYnmMzTjcxY5_sMOaBlpwYpei_cyZ-aocRGQ; section_data_ids=%7B%22directory-data%22%3A1703432331%2C%22messages%22%3A1703432331%2C%22customer%22%3A1703432331%2C%22compare-products%22%3A1703432331%2C%22last-ordered-items%22%3A1703432331%2C%22cart%22%3A1703433736%2C%22captcha%22%3A1703432331%2C%22wishlist%22%3A1703432331%2C%22multiplewishlist%22%3A1703432331%2C%22goldcards%22%3A1703432331%2C%22adult_goods%22%3A1703433735%2C%22geolocation%22%3A1703433734%2C%22recently_viewed_product%22%3A1703432331%2C%22recently_compared_product%22%3A1703432331%2C%22product_data_storage%22%3A1703432331%7D',
        'dnt': '1',
        'origin': 'https://goldapple.ru',
        'pragma': 'no-cache',
        'referer': 'https://goldapple.ru/makijazh/glaza/podvodka',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-d05618c0674471d2d57686ba678ddf83-800662617f555d18-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'categoryId': 1000000110,
        # Город cityId
        'cityId': '2763c110-cb8b-416a-9dac-ad28a55b4402',
        'cityDistrict': None,
        'pageNumber': page_number,
        'filters': [],
    }

    response = requests.post('https://goldapple.ru/front/api/catalog/products', cookies=cookies, headers=headers, json=json_data).json()
    data_request = response.get('data').get('products')
    print(data_request)
    #print(data_request)
    if data_request:
        for i in data_request:
            data_set = dict()
            data_set['itemID'] = i.get('itemId')
            data_set['price'] = i.get('price').get('actual').get('amount')
            data_set['url'] = i.get('url')
            data_list.append(data_set)
        #print(data_set)

        return data_list
    else:
        #print(data_request)
        return data_list


    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"categoryId":1000000110,"cityId":"2763c110-cb8b-416a-9dac-ad28a55b4402","cityDistrict":null,"pageNumber":2,"filters":[]}'
    #response = requests.post('https://goldapple.ru/front/api/catalog/products', cookies=cookies, headers=headers, data=data)

def main():
    
    data_list = json.load(open('data_set.json'))
    for i in range (1, 25):
        print(i)
        get_data(data_list, i)

        
        


    with open('data_set.json', 'w') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    main()





