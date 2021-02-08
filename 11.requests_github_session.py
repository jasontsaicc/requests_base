import requests
import re

def login():
    #session
    session = requests.session()

    #headers
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }

    #url1_獲取token
    url1 = 'https://github.com/login'
        #發送請求獲取響應
    res_1 = session.get(url1).content.decode()
        #正則表達式提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    print(token)

    #url2_登入
    url2 = 'https://github.com/session'
        #構建表單數據
    data = {
        "commit": "Sign in",
        "authenticity_token": token,
        "login": "jasontsaicc",
        "password": "Fumso4-kutbyk-nokhed",
        "webauthn-support": "supported",
        "webauthn-iuvpaa-support": "supported",
    }
        #發送請求登入
    print(data)
    session.post(url2, data=data)
    #url3_驗證
    url3 = 'https://github.com/jasontsaicc'
    response = session.get(url3)
    with open ('github.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    login()
