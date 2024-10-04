from typing import Final
import requests

API_KEY: Final[str] = "17736d1a82caa16967cd581a9c8411a2d3f95"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"

def url_shortener(full_link: str):
    # create a variable of type dict for the parameters needed
    payload: dict = {'key': API_KEY, 'short': full_link}
    try:
        # Making the request to the URL shortener API
        request = requests.get(BASE_URL, params=payload)
        request.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        data: dict = request.json()

        # Checking if the 'url' key exists in the data
        url_data = data.get('url')
        if url_data and url_data.get('status') == 7:  # Valid status check
            short_link: str = url_data.get('shortLink', 'No short link available')  # Updated key from the response
            print('Shortened Link:', short_link)
        else:
            error_status = url_data.get('status')
            if error_status == 1:
                error_status = 'Link already shortened'
            elif error_status == 2:
                error_status = 'Not a valid link'
            elif error_status == 4:
                error_status = 'invalid API KEY'
            elif error_status == 5:
                error_status = 'link contains invalid characters'
            elif error_status == 6:
                error_status = 'Blocked domain link'
            else:
                error_status = 'unknown error'

            print('Error Status:', error_status)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    input_link: str = input('Enter a Link: ')
    url_shortener(input_link)

if __name__ == '__main__':
    main()
