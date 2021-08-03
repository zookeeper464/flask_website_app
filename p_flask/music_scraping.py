import re
import requests
from bs4 import BeautifulSoup
from requests.api import head

def get_page(page_url):
    page = requests.get(page_url, headers={'User-Agent' : 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup

def get_music_code(music,singer):
    search_url = f"https://www.melon.com/search/total/index.htm?q={singer}+{music}&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&linkOrText=T&ipath=srch_form"
    soup = get_page(search_url)
    ul_class_first = soup.find('div', {"class":'tb_list d_song_list songTypeOne'})
    table_class_first = ul_class_first.find('td',{'class':'t_left'})
    link_class_first = table_class_first.find('a', {'class':"btn btn_icon_detail"})["href"]
    string = link_class_first.split(';')[1]
    music_code = re.findall('\d+',string)[0]
    return int(music_code)

def get_music (music_code):
    search_url = f"https://www.melon.com/song/detail.htm?songId={music_code}"
    soup = get_page(search_url)
    music_text = soup.find('div', {"id":'conts'})
    music = music_text.find('div',{'class':'song_name'}).text
    music = re.sub("\n|\t|\r|곡명","",music)
    singer = music_text.find('div',{'class':'artist'}).find('a')['title']
    tags = music_text.find('div',{'class':'meta'}).find_all('dd')[2].text.split('/')
    return music, singer, tags

def run (my_music,my_singer):
    music_code = get_music_code(my_music,my_singer)
    music, singer, tags = get_music_code(music_code)
    return music, singer, tags
