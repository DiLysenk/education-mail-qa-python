from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_token(self):
        headers = self.session.get(self.base_url).headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in main page headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]

        return token

    def post_login(self, user, password):
        location = '/login/'

        csrf_token = self.get_token()

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': f'csrftoken={csrf_token}'
        }

        data = {
            'csrfmiddlewaretoken': csrf_token,
            'login': user,
            'password': password
        }

        result = self.session.post(urljoin(self.base_url, location), headers=headers, data=data)
        response_cookies = result.headers['Set-Cookie'].split(';')

        new_csrf_token = [c for c in response_cookies if 'csrftoken' in c][0].split('=')[-1]
        sessionid_gtp = [c for c in response_cookies if 'sessionid_gtp' in c][0].split('=')[-1]

        self.session.cookies = cookiejar_from_dict({'csrftoken': new_csrf_token, 'sessionid_gtp': sessionid_gtp})

        return result
