import requests

url = "http://fy.iciba.com/ajax.php?a=fy"

proxies = {
    'http':'http://113.214.13.1:1080',
    # 'https':'https://183.166.162.226:9999'
}
response = requests.get(url, proxies=proxies)

print(response.content.decode())