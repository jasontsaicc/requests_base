import requests

url = 'https://github.com/jasontsaicc'

# 構建請求頭
headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
}

# 構建cookie字典
temp = '_octo=GH1.1.858944075.1612590665; tz=Asia/Taipei; _device_id=83a6fb3fbf2f9a6ca2051cf2a4f99a9e; has_recent_activity=1; user_session=aDGO7ZMH1JcY8oMe_MKgW1QFQgN2o83sZ2dTgN25mooBtAdd; __Host-user_session_same_site=aDGO7ZMH1JcY8oMe_MKgW1QFQgN2o83sZ2dTgN25mooBtAdd; tz=Asia/Taipei; logged_in=yes; dotcom_user=jasontsaicc; _gh_sess=VkPBy81gXUIhW02sWVJSN+xaZoeBiljmLuUyaoiw/xu3gSUo8N7DRW9v/6cz5CuehW7G7yUJTcF8f48862LcznK8TU2TOA0cBe2+Y9PpyWrZXBuV7D3FUs4nAnf7t5ClGgw3Xkjt4P2lGPVRMv06NJutKggYjfj3wa5TOmgLQvAkKn4neRlARUlHNldB1KUU9z9MBk8ArrlkvHJyfPnMDIbqs2bi2WBH7R//+ifPmj6PwqwUOJAfm3BAQdIzAtyZOH/izrCO0jKqVfjPbf2Gx3a83F/0ngfdu0WIXU0awdNfiHBW7eHbjECioypxLkkni/elR8zAO230YLjxlAIfJXh3bxRcMKZF1DKOjCaE4CIwiDj/Gh//WTMQ5za+9hOWa45jHHwjBlcQTn9wu5Ndazpx3wTcjUxxmFgJ+LCsAXs+eIloLIpG0aEFnbYgoIg32pi0/xbAt1QbxjTcULNcHf6c+QjXN2/bDeNumbJl0riW9MFIMN0uWvBbcFnrujM3yFAq8C3W8YDeIGHBBeB/Mz5hxxc0p3StM31EgNVPtcKNEeg660zGVHpNN5pfaBZJGwq69nxkbz5UJZEmITEdWHftOI7WO7ZCVAH1QysN9H7AEgH5EcGJzWeRvJM+ZtcS/nc8bzENTa2OW8PMslPLObIYWDIUpC2EZXWUczkicNh3lTVgC/2Az+HhqLOm9sU8Ztb5GXPCYZNd6nSUp98nSEyPmh+ZUxxc6eX4yXgsATHBYnnTHsMB1Y2HrkU/QTf253KP1ixAum3BiHeqZZyfT65N8D7/436t1cgqOQGdxZntLC4NNjgknsf+eByMtdVHscI8GS/cyy9ptgfktxrDsrdoHGdmmm+5kMW9X4EOwWMOyQ5Va5CCXkENdbCjGM/SEY8RRL3KpY+fg+3oemVrQj2PeOhZsznahIMylvC0OcA=--yExjVS+OcTs+Uevd--PMRYtvX27Yn3Kxe4uLSCsQ== '

# 方案一 切割key vaule
# cookie_list = temp.split(';')
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split('=')[0]] = cookie.split('=')[-1]
# print (cookies)

# 方案二 字典推導式
cookie_list = temp.split(';')
cookies = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookie_list}

reponse = requests.get(url, headers=headers ,cookies=cookies)

with open("github_with_cookies3.html", "wb")as f:
    f.write(reponse.content)