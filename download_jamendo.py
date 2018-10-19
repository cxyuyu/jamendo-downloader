import requests
import time
import re
import os


def get_():
    '''

    :return:
    '''
    #cookie
    header = {
        "user-agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'x-jam-call': '$a6b3c3c8a5a1888b1a41c29517f45ec214621aff*0.5574606687572872~'}
    url = 'https://www.jamendo.com/community/punk/tracks'
    response = requests.get(url, headers=header)
    response.cookies.set("_ga", "GA1.2.1870680278.1539831081", path="www.jamendo.com")
    response.cookies.set("_gid", "GA1.2.1391188083.1539831081", path="www.jamendo.com")
    response.cookies.set("_hjIncludedInSample", "1", path="www.jamendo.com")
    response.cookies.set("jamapplication", "true", path="www.jamendo.com")

    '''
    emotional
    https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=2754&limit=20
    dance
    https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=100&limit=20
    chillout
    https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=1834&limit=20
    ambient
    https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=362&limit=20
    Energetic
    https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=5942&limit=20
    '''
    channel_id = {'emotional': 2754, 'dance': 100, 'chillout': 1834, 'ambient': 362, 'energetic': 5942}
    for channelname in channel_id:
        print(channelname)
        channel_id = channel_id[channelname]
        response = requests. \
            get("https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId={}&limit=30".format(channel_id),
                cookies=response.cookies, headers=header)
        print(response.text)
        ids = re.findall('"id":(\d+),', response.text)
        print(ids)
        #
        save_music(channelname, ids)


def save_music(path, ids):
    if not os.path.exists(path):
        os.mkdir(path)
    get_music(path, ids)


def get_music(path, ids):
    count = 0
    for id in ids:
        song_name = get_name(id)
        # time.sleep(1)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        url = 'https://mp3d.jamendo.com/?trackid={}&format=mp32&from=app-97dab294'.format(id)
        now_date = time.strftime("%Y:%m:%d", time.localtime())
        print("start download {}".format(song_name))
        with open(path + '/{}-{}-{}.mp3'.format(now_date, count, song_name), 'wb') as f:
            response = requests.get(url, headers=header)
            f.write(response.content)
        count = count + 1
        # time.sleep(3)


def get_name(id):
    name = None
    response = requests.get('https://www.jamendo.com/track/' + str(id))
    name = re.split("\/", response.url)[-1]
    return name


#curl 测试代码
'''
curl 'https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=2754&limit=20'-H 'pragma: no-cache' 
 -H 'cookie: jammusiclang=en; 
 jammusicsession=s%3A8NhmQGgR3StOP3GkQ-jEtx8zMnEPzfPS.k%2FfuPj8m5cvrTl3VsMtKczp%2BTPiph3iIhBF79yS02FA; 
 _ga=GA1.2.1870680278.1539831081; 
 _gid=GA1.2.1391188083.1539831081; 
 _hjIncludedInSample=1; 
 jamapplication=true; 
 jamAcceptCookie=true' 
 -H 'x-jam-version: x00iw' 
 -H 'accept-encoding: gzip, deflate, br' 
 -H 'accept-language: zh-CN,zh;q=0.9' 
 -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' 
 -H 'accept: application/json, text/javascript, */*; q=0.01' 
 -H 'cache-control: no-cache' 
 -H 'authority: www.jamendo.com' 
 -H 'x-requested-with: XMLHttpRequest' 
 -H 'referer: https://www.jamendo.com/community/emotional' 
 -H 'x-jam-call: $a6b3c3c8a5a1888b1a41c29517f45ec214621aff*0.5574606687572872~' --compressed


curl 'https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=2754&limit=55' -H 'pragma: no-cache' -H 'cookie: jammusiclang=en; jammusicsession=s%3A8NhmQGgR3StOP3GkQ-jEtx8zMnEPzfPS.k%2FfuPj8m5cvrTl3VsMtKczp%2BTPiph3iIhBF79yS02FA; _ga=GA1.2.1870680278.1539831081; _gid=GA1.2.1391188083.1539831081; _hjIncludedInSample=1; jamapplication=true; jamAcceptCookie=true'  -H 'x-jam-call: $a6b3c3c8a5a1888b1a41c29517f45ec214621aff*0.5574606687572872~' --compressed
'''

if __name__ == "__main__":
    channel_num = {'emotional': 0, 'dance': 0, 'chillout': 0, 'ambient': 0, 'energetic': 0}
    get_()
