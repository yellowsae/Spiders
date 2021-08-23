import requests
from fake_useragent import UserAgent 
from parsel import Selector
from requests import ConnectionError, ReadTimeout
from time import sleep


def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS)"
    }
    ip = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + ip,
        'https':'https://' + ip
    }
    try:
        sleep(0.1)
        response = requests.get(url,headers=headers,proxies=proxies)
        if response.status_code == 200:
            return response.status_code
        else:
            print(" Get page Failed ",response.status_code)
            return None
    except (ConnectionError, ReadTimeout):
        return None


def main():
    for page in range(2,20):
        url = f'https://www.tujigu.com/a/41553/{page}.html'
        html = get_url(url)
        print(html,url)


if __name__ == '__main__':
    main()