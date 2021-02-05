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

# 常見的響應對象參數和方法
# 響應url
print(response.url)

# 狀態碼
print(response.status_code)

# 響應對應的請求頭
print(response.request.headers)

# 響應頭
print(response.headers)

# 響應設置的cookie
print(response.cookies)

