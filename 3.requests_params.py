import requests
#
# url = 'https://www.baidu.com/s?wd=python'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers)
#
# with open('baidu.html' , 'wb')as f:
#     f.write(response.content)


url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}

# 構建參數字典
data = {
    'wd':'python'
}

response = requests.get(url, headers=headers, params=data)


print(response.url)
with open('baidu1.html' , 'wb')as f:
    f.write(response.content)