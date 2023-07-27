import requests
import re
import os

filename = 'D:\music\\'
#如果没有此文件夹就自动创建一个文件夹
if not os.path.exists(filename):
    os.mkdir(filename)

url = 'https://music.163.com/discover/toplist?id=3778678'
#headers 请求头 伪装成浏览器
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
}
response = requests.get(url=url, headers=headers)
# print(response.text)
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)

#批量下载歌曲
for name_id, title in html_data:
    music_url = f'https://music.163.com/song/media/outer/url?id={name_id}.mp3'
    music_content = requests.get(url=music_url, headers=headers).content
    with open(filename + title + '.mp3', mode = 'wb') as f:#wb二进制覆盖写入数据
        f.write(music_content)
    print(name_id, title)
