import requests

url = 'http://www.baidu.com'

response = requests.get(url)

print(len(response.content.decode()))
print(response.content.decode())

# 構建請求頭宇典
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}

# 發送帶請求頭的請求
response1 = requests.get(url, headers=headers)

print(len(response1.content.decode()))
# print(response1.content.decode())
