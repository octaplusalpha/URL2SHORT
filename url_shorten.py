from typing import Final
import requests

API_KEY: Final[str] = "17736d1a82caa16967cd581a9c8411a2d3f95"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def url_shortener(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()
    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortlink']
            print('Link: ', short_link)
    else:
            print('Error Status: ', url_data['status'])


def main():
    input_link: str = input('Enter a Link: ')
    url_shortener(input_link)


if __name__ == '__main__':
    main()
