from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

URL = 'https://soundcloud.com/'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(URL)

data = driver.page_source
driver.quit()

soup = BeautifulSoup(data, 'html.parser')


song_titles = soup.select('li.badgeList__item')

song = []
for div in song_titles:
    song_name = div.select_one('a.sc-link-primary').text.strip()
    song_artist = div.select_one('a.sc-link-secondary').text.strip()
    print(f'{song_name}, by {song_artist}')
    song.append({'title': song_name, 'by': song_artist})

df = pd.DataFrame(song)
df.to_csv('trending_songs', index=False)


