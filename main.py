import requests
import os

os.system('cls')


url = 'https://www.instagram.com/accounts/web_create_ajax/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.instagram.com/'
}


payload = {
    'email': 'wikobed538@aaorsi.com',
    'password': 'Husban1snaughty',
    'username': 'stella.gay',
    'first_name': 'John',
    'opt_into_one_tap': 'false'
}


response = requests.post(url, headers=headers, data=payload)


if response.status_code == 200:
    print('Registration successful')
else:
    print('Registration failed')
