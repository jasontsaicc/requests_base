import requests

url = 'http://www.baidu.com'

response = requests.get(url)

# 手動設置編碼格式
response.encoding = 'utf8'
# 列印出原碼str類型數據
# print(response.text)

# print(response.encoding)

# response.content 是存儲的bytes類型的響應源碼,可以進行decode操作
print(response.content.decode())

