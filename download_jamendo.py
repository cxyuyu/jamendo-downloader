import requests
import time
import re
import os


def get_(channel_num= {'emotional': 0, 'dance': 0, 'chillout': 0, 'ambient': 0, 'energetic': 0}):
    '''

    :return:
    '''
    #cookie
    header = {
        "user-agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'x-jam-call': '$92525533bfd98eba6344f72433e52a2991e122d0*0.7073001144863946~'}
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
    channel_key = {'emotional': 2754, 'dance': 100, 'chillout': 1834, 'ambient': 362, 'energetic': 5942}
    channel_ids = {}
    for channelname in channel_key:
        print(channelname)
        channel_id = channel_key[channelname]
        response = requests. \
            get("https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId={}&limit=30".format(channel_id),
                cookies=response.cookies, headers=header)
        print(response.text)
        time.sleep(5)
        ids = re.findall('"id":(\d+),', response.text)
        print(len(ids[channel_num[channelname]:]))
        print(ids[channel_num[channelname]:])
        ids=ids[channel_num[channelname]:]
        channel_ids[channelname]=ids
    print(channel_ids)
    # for key in channel_ids:
    #     save_music(key, channel_ids[key])


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


curl 'https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=362&limit=55' -H 'pragma: no-cache' -H 'cookie: jammusiclang=en; jammusicsession=s%3A8NhmQGgR3StOP3GkQ-jEtx8zMnEPzfPS.k%2FfuPj8m5cvrTl3VsMtKczp%2BTPiph3iIhBF79yS02FA; _ga=GA1.2.1870680278.1539831081; _gid=GA1.2.1391188083.1539831081; _hjIncludedInSample=1; jamapplication=true; jamAcceptCookie=true'  -H   'x-jam-call: $92525533bfd98eba6344f72433e52a2991e122d0*0.7073001144863946~' --compressed
curl 'https://www.jamendo.com/api/charts/track?type%5B%5D=track&tagId=362&limit=55' -H 'pragma: no-cache' -H 'cookie: jammusicsession=s%3Au5Fm1aez98OH7-8RoLAH0EBMG02wrVDR.8IeGTtnAxemQGmGnsyLoyLXkDcoWCUYudQgxLC4XxQA; jammusiclang=en; _ga=GA1.2.680150216.1539836117; _gid=GA1.2.363062877.1539836117; _hjIncludedInSample=1; jamapplication=true; jamAcceptCookie=true; global-app_hash=b7cb2682057357e5d8b0c8e0b9882e21d4718331aa58f811b6b8e127947eb482ff29924468d68db92b9ba625eb066b05d9d90ff10db69e82a4cf5817a557f306773c1d00b970f77887' -H 'x-jam-version: xrgpd' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-CN,zh;q=0.9' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'cache-control: no-cache' -H 'authority: www.jamendo.com' -H 'x-requested-with: XMLHttpRequest' -H 'referer: https://www.jamendo.com/community/ambient' -H 'x-jam-call: $92525533bfd98eba6344f72433e52a2991e122d0*0.7073001144863946~' --compressed
'''

if __name__ == "__main__":
    channel_num = {'emotional': 0, 'dance': 0, 'chillout': 0, 'ambient': 0, 'energetic': 0}
    # 输入数值如
    # {'emotional': 10, 'dance': 20, 'chillout': 0, 'ambient': 0, 'energetic': 0}
    # 默认下载30首，设置数值的原因（因网速不好，可能导致的中断较多），中断后需要继续可以防止重新下载
    get_(channel_num)
