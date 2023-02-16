import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import youtube_dl

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_youtube = "https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw"

# Abrir a página desejada
driver.get(url_youtube)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll to the bottom of the page using ActionChains
while True:
    try:
        # Find the last video on the page
        last_video = driver.find_element_by_xpath("//a[@id='video-title'][last()]")
        # Scroll to the last video
        actions = ActionChains(driver)
        actions.move_to_element(last_video).perform()
        time.sleep(1)
    except:
        break
        
# Get the page source again after scrolling to the bottom
html_content = driver.page_source

time.sleep(5)

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-grid-video-renderer")
    links = ["https://www.youtube.com" + video.get("href") for video in videos]
    titles = [video.get("title") for video in videos]
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()



# Instalando yt-dlp

subprocess.run(['pip', 'install', '--user', '--upgrade', 'yt-dlp'])
subprocess.run(['pip', 'install', 'yt-dlp'])

import yt_dlp

time.sleep(5)

# Get the playlist and write to file
try:
    with open('./YOUTUBEPLAY1.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
    with yt_dlp.YoutubeDL({'default_search': 'ytsearch'}) as ydl:
        info = ydl.extract_info(f"ytsearch:{amor}", download=False)
    entries = info.get('entries', [])
    for i, entry in enumerate(entries):
        if 'url' not in entry:
            print(f"Erro ao gravar informações do vídeo {entry}: 'url'")
            continue
        url = entry['url']
        thumbnail_url = entry['thumbnail']
        description = entry.get('description', '')[:10]  # Use as primeiras 10 palavras da descrição ou menos
        title = entry.get('title', '')
        # Write the stream information to the file
        f.write(f"#EXTINF:-1 group-title=\"YOUTUBE1\" tvg-logo=\"{thumbnail_url}\",{title} - {description}\n")
        f.write(f"{url}\n\n")
        f.write("\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")


