import os
import sys
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

BASE_URL = "https://earthview.withgoogle.com"

def get_url(url, css_class):
    image_url = None
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    for link in links:
        if css_class in link['class']:
            image_url = BASE_URL + '%s' % (link.get('href'),)
    return image_url

image_url = get_url(BASE_URL, 'explore')
image_file_url = get_url(image_url, 'menu__item--download')
file_name = image_file_url.split('/')[-1]
os.chdir(os.environ['HOME']+'/Pictures/earthview-wallpaper')

# check if file already exists
if file_name not in os.listdir():
    urlretrieve(image_file_url, '%s/Pictures/earthview-wallpaper/%s' % (os.environ['HOME'], file_name))

sys.stdout.write(file_name)
