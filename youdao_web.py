#匯入urllib庫
# https://iter01.com/566888.html
import urllib.request
import urllib.parse
import json

while True: #無限迴圈
    content = input("請輸入您要翻譯的內容(輸入 !!! 退出程式): ")
    #設定退出條件
    if content == '!!!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule' #選擇要爬取的網頁，上面找過了
    #加上一個帽子，減少被發現的概率（下面head列表的內容就是上面找的）
    head = {}
    head['User - Agent'] = '請替換'

    #偽裝計算機提交翻譯申請（下面的內容也在在上面有過，最好根據自己的進行修改）
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom:'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url, data)
    #解碼
    html = response.read().decode('utf-8')

    paper = json.loads(html)

    #列印翻譯結果
    print("翻譯結果: %s" % (paper['translateResult'][0][0]['tgt']))