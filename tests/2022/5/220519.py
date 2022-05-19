# Getting png to pdf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# import img2pdf
# https://i3.nhentai.net/galleries/1741848/1.jpg
# https://i5.nhentai.net/galleries/1741848/1.jpg
import os


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


number = '330300'
link = f'https://nhentai.net/g/{number}/'

driver.get(link)
#html_source = driver.page_source

#print(html_source)

soup = BeautifulSoup(driver.page_source, 'html.parser')

def download_image(link):
    import requests
    response = requests.get(link)
    file = open(f'images/nh/{link.split("/")[-1]}', "wb")
    file.write(response.content)
    # return response


low_quality = True
thumbs = soup.find('div', {'class': 'thumbs'})
print(thumbs.children)
images = []
for child in thumbs.children:
    img_link = child.find('img').get('data-src')
    print(img_link)
    images.append(download_image(img_link))

import PIL
import PIL.Image
import os

#Image = PIL.Image
path = 'images/nh'

print(os.listdir(path))
files = os.listdir(path)
#files.sort(key=int)
files = sorted(files, key=lambda i: int(i.split('t')[0]))
print('\n\n\n\n\nALOOOOOOOOOOOO')
print(files)
images = [
    PIL.Image.open(f'{path}/{f}')
    for f in files
]
images

pdf_path = "nh.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)


files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
for file in files:
    os.remove(path+'/'+file)