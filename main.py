import string
import requests


def search_fishing():
    list_fish = []
    links_fish = []
    num1= '_1234567890-'
    main_domen = ['.com','.com.ua','.ru','.com.ru','.org']
    link0 = 'http://www.liqpay.ua'

    for md in main_domen:
        link = 'http://www.' + 'liqpay' + md
        try:
            response = requests.get(link)
            if response.status_code == 200:
                print(link, response.status_code)
                links_fish.append(link)
        except Exception:
            '1'

        for md1 in num1 + string.ascii_letters:
            link1 = 'http://www.' + 'liqpay' + md1 + md
            try:
                response = requests.get(link1)
                if response.status_code == 200:
                    print(link, response.status_code)
                    links_fish.append(link1)
            except Exception:
                '-------------------------'

            for md2 in num1 + string.ascii_letters:
                link2 = 'http://www.' + 'liqpay' + md1 + md2 + md
                print(link2)
                try:
                    response = requests.get(link2)
                    if response.status_code == 200:
                        print(link2, response.status_code)
                        links_fish.append(link2)
                except Exception:
                    '-----------------------------'

                # for md3 in num1 + string.ascii_letters:
                #     link3 = 'http://www.' + 'liqpay' + md1  + md2 + md3 + md
                #     print(link3)
                #     try:
                #         response = requests.get(link3)
                #         if response.status_code == 200:
                #             print(link3, response.status_code)
                #             links_fish.append(link3)
                #     except Exception:
                #         '-----------------------------'
                #
                #     for md4 in num1 + string.ascii_letters:
                #         link4 = 'http://www.' + 'liqpay' + md1 + md2 + md3 + md4 + md
                #         print(link4)
                #         try:
                #             response = requests.get(link4)
                #             if response.status_code == 200:
                #                 print(link4, response.status_code)
                #                 links_fish.append(link3)
                #         except Exception:
                #             '-----------------------------'
    print(links_fish)

search_fishing()
