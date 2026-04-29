"""
This projects help sus to check the status of website, whether it is online or offline. it is going to give us back some
basic information regarding the website such as response time.
"""
import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


def check_website_status(website_url: str) -> None:
    try:
        response: Response = requests.get(website_url)

        # information of website
        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = CaseInsensitiveDict(response.headers)
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        url: str = response.url
        response_time: float = response.elapsed.total_seconds()

        print(f'URL of the website is : {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time: .2f} seconds')

    except RequestException as ex:
        print(f"Error: ", {ex})


def main() -> None:
    url_to_check = 'https://indently.io'

    check_website_status(url_to_check)


if __name__ == '__main__':
    main()
