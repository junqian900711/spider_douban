import requests
import json
import pymongo
#url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=rank&page_limit=20&page_start=0"
"""
https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=rank&page_limit=20&page_start=20
"""
client = pymongo.MongoClient(host='localhost', port=27017, connect=False)

douban = client['douban']
#douban.authenticate(name='douban_user', passward='123456')

douban_tv = douban['douban_tv']
douban_tv.create_index([("id", 1)], unique=True)
urls = ["https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=rank&page_limit=20&page_start=" + str(n) for n in range(0, 200, 20)]
for url in urls:
    response_data = requests.get(url)
    print(response_data.text)
    json_data = json.loads(response_data.text)
    # print(type(json_data))
    # print(json_data)
    for tv in json_data["subjects"]:
        # print(tv)
        data = {
            'rate': tv['rate'],
            'title': tv['title'],
            'img_url': tv['cover'],
            'id': tv['id'],
            'tag': '美剧'
        }
        douban_tv.insert_one(data)
        print(data)
