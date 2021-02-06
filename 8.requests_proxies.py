import requests

url = 'http://www.baidu.com'

proxies = {
    'http':'http://47.93.24.243:8080',
    # 'https':'https://183.166.162.226:9999'
}
response = requests.get(url, proxies=proxies)

print(response.text)