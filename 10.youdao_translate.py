
import requests
import json
import sys

class Translate(object):

    def __init__(self, word):
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        self.formdata = {
        'type': 'auto',
        'i': word,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom:': 'fanyi.web',
        'ue':'UTF-8',
        'typoResult' :'true',
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.formdata)
        return response.content

    def parse_data(self, data):

        dict_data = json.loads(data)
        print(dict_data)
        print(dict_data['translateResult'][0][-1]['tgt'])

    def run(self):
        # 構思爬取思路
        # url
        # headers
        # formdata
        # 發送請求獲取響應
        data = self.get_data()
        # print(data)

        # 解析響應
        self.parse_data(data)

if __name__ == '__main__':

    word = input('請輸入要翻譯的單字:')
    # word = 'hello'
    translate = Translate(word)
    translate.run()