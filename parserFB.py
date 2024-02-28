import requests
import time
from datetime import datetime, timedelta
import json

class Parser_fb:
    session = requests.Session()

    login_url = 'http://fbtool.pro/login'
    statistics_url = 'http://fbtool.pro/statistics'
    test1_url = 'http://fbtool.pro/site/set-statistics-mode'
    params_url ='http://fbtool.pro/ajax/get-statistics'
    
    header = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"
    }

    data = {
        'username': 'nickstokes21@yandex.ru',
        'password': 'h9dl4e#n#n)leU',
        'g-recaptcha-response': '03AFcWeA6V5RgU6YaAOpQ_8WyHJ8FZfLoVlQ57KxrBLZYEXtN8f0_65qSjApaUNA6-Iire9CUO0QYIls0UOUUpd3oKxec4t6R9zo1RXRuccsEu_svTX3yzzoLD-EtbvRWy8R4ocIAdfCN4Cy-UVtPbIiR4QZ6ghhgzgxLFhiF3tXTa9EmIEf5cGWl6j-6e28Iptn-PFkDbkod4M8Hb_r2HpMoChz3yZSpgZeLebRRpm74EKRd8LmTrTlsoEbpNDdSq2FnSDZiiZTVpLvrb49ygbC2QcYAZ_UmZ3y9k60bZuDzTFn9sJh_ODLvB3xL373sr-oW-wDKE0zQq2azkEIxX9dLeintKoJ5a_diKkP0yTEe1hFGw9Re0Krcd0qs9gRlMyZhpsm0DMdbyJ1tlt4n3eSViaXz2ynfkR3MnWYqSZT9c2tBRqXkRjlz-xx-Y-vjYJ3Bls556GywqdSBZHYQ_NBLvzSuPVKf7CAAmHWkBTbzpF8--E_ij_pkNQwPRCFUdq-vFGEk6H8VY0Sl2L7igx9kZm7hnnSvJuFe2JCRAPtr7PZOsZ1HzPCF3mCm0EB4F04MKs9cXYr_s9Ac7cJPPm59upCSMG_Lh1A'
    }

    data2 = {
        'username': 'nickstokes21@yandex.ru',
        'password': 'h9dl4e#n#n)leU',
        'g-recaptcha-response': '03AFcWeA6V5RgU6YaAOpQ_8WyHJ8FZfLoVlQ57KxrBLZYEXtN8f0_65qSjApaUNA6-Iire9CUO0QYIls0UOUUpd3oKxec4t6R9zo1RXRuccsEu_svTX3yzzoLD-EtbvRWy8R4ocIAdfCN4Cy-UVtPbIiR4QZ6ghhgzgxLFhiF3tXTa9EmIEf5cGWl6j-6e28Iptn-PFkDbkod4M8Hb_r2HpMoChz3yZSpgZeLebRRpm74EKRd8LmTrTlsoEbpNDdSq2FnSDZiiZTVpLvrb49ygbC2QcYAZ_UmZ3y9k60bZuDzTFn9sJh_ODLvB3xL373sr-oW-wDKE0zQq2azkEIxX9dLeintKoJ5a_diKkP0yTEe1hFGw9Re0Krcd0qs9gRlMyZhpsm0DMdbyJ1tlt4n3eSViaXz2ynfkR3MnWYqSZT9c2tBRqXkRjlz-xx-Y-vjYJ3Bls556GywqdSBZHYQ_NBLvzSuPVKf7CAAmHWkBTbzpF8--E_ij_pkNQwPRCFUdq-vFGEk6H8VY0Sl2L7igx9kZm7hnnSvJuFe2JCRAPtr7PZOsZ1HzPCF3mCm0EB4F04MKs9cXYr_s9Ac7cJPPm59upCSMG_Lh1A',
        '_csrf': 'RpAAxy3fNzdaAf6a01hISsK0bNWrlcOxCg-eqqvnRRxr3HKRea9-BzEsjO2rFXEEicEdr9qjrMFoYtry8d4OKA==',
        'mode': 'adsets'
    }

    data3 = { 'more volnuetsia'}

    cookie = {
        '_identity':'05791ce0ff7f31569188e7396811314e888e28b3cf36468160c9b47a671a3fbba%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B296%2C%22yIPtYw5tR9RkAMFbFk-W9UAGSNaGhdhZ%22%2C2592000%5D%22%3B%7D',
        'currency': 'c096c807ae48cec3d2b6e45310c33ead0c9ce162b3bad6ed329bf4c2c22a870ba%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22currency%22%3Bi%3A1%3Bs%3A3%3A%22USD%22%3B%7D',
        'ad_status': '654233790f455972c207a9d4092f5ed64e09114c214276bf47e3ba0dd6b600b4a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22ad_status%22%3Bi%3A1%3Bs%3A3%3A%22all%22%3B%7D',
        'statistics_mode': '6ec1bc29072e5996463c26df4a25aa03a7d6df53d49977e5908e214127058c5ea%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22statistics_mode%22%3Bi%3A1%3Bs%3A6%3A%22adsets%22%3B%7D'
    }


    yesterday = datetime.now() - timedelta(days=1)

    yesterday1 = yesterday.strftime('%Y-%m-%d')
    yesterday2 = yesterday.strftime('%Y-%m-%d')


    

    login_response = session.post(login_url, headers=header, data=data, cookies=cookie)

    cookies_dist = [
        {"name":key.name,"value":key.value, 'domain':key.domain, 'path':key.path}
        for key in session.cookies
        ]

    session2 = requests.Session()

    for cookiea in cookies_dist:
        session2.cookies.set(**cookiea)

    statistics_response = session2.get(statistics_url, headers=header).text

    test2_res = session2.post(test1_url, headers=header, data=data2).text

    cookies_dist2 = [
        {"name":key.name,"value":key.value, 'domain':key.domain, 'path':key.path}
        for key in session2.cookies
        ]

    session3 = requests.Session()

    for cookies in cookies_dist2:
        session3.cookies.set(**cookies)

    id_list = ['group_260139']
# , 'group_344356', 'group_351347'
    db_fb =[]
    for id_value in id_list:
        params = {
            'dates': f'{yesterday1} - {yesterday2}',
            'status': 'all',
            'currency': 'USD',
            'adaccount_status': 'all',
            'ad_account_id': 'all',
            'id': id_value  
        }

        response = session3.post(params_url, headers=header, params=params, cookies=cookie, data=data3)
        json_data = response.json()
        
    
    # json_data = response.json()
        reviews = json_data[0]['rows']

        for r in reviews:
            adset_name = r['adset_name']
            link_click = r['link_click']
            leads = r['leads']

            if '№' not in adset_name:
                continue
            
            start_index = adset_name.index('№') + 1
            end_index_before_pipe = adset_name.rfind(' |')
            end_index_before_question = adset_name.find(' ?', start_index)
            
            if end_index_before_question != -1 and end_index_before_question < end_index_before_pipe:
                print("Skipping: '?' found after '№'")
                continue
            
            pipe_index = adset_name.find('| ', start_index)
            bracket_index = adset_name.rfind(' [')
            
            if pipe_index == -1 or bracket_index == -1 or bracket_index <= pipe_index:
                continue

            # Extract values
            number_fb = adset_name[start_index:pipe_index].replace(" ", "")
            id_fb = adset_name[pipe_index + 2:bracket_index]
            buc = adset_name[bracket_index + 2:adset_name.rindex(']')]

            # Calculate cr and store the values in db_fb
            cr =int(round((leads / link_click), 2)*100) if link_click != 0 else 0
            data_entry = [number_fb, id_fb, buc, cr]
            db_fb.append(data_entry)
        # except (json.JSONDecodeError, KeyError) as e:
        #     print(f"Error decoding JSON or accessing data: {e}")
        #     # Handle the error or exit the loop accordingly
        #     continue
    print(db_fb)
