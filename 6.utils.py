import requests
url = 'http://www.baidu.com'

response = requests.get(url)
print(response.cookies)

dict_cookie = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookie)

jar_cookies = requests.utils.cookiejar_from_dict(dict_cookie)
print(jar_cookies)