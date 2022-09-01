import requests
import time


class Stackoverflow:

    def get_recent_questions(self):
        url = 'https://api.stackexchange.com/2.3/questions/'
        days_to_sec = 2 * 86400
        todate = int(time.time())
        fromdate = int(todate - days_to_sec)
        params = {'fromdate': fromdate,
                  'order': 'desc',
                  'sort': 'activity',
                  'tagged': 'python',
                  'site': 'stackoverflow',
                  'pagesize': 100,
                  'page': 1}
        response = requests.get(url, params=params).json()
        while response['has_more']:
            response = requests.get(url, params=params).json()
            for quest in response['items']:
                print(quest['link'])
            params['page'] += 1
        print('Вывод успешно завершён.')



loader = Stackoverflow()
loader.get_recent_questions()


