# Getting png to pdf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# import img2pdf
# https://i3.nhentai.net/galleries/1741848/1.jpg
# https://i5.nhentai.net/galleries/1741848/1.jpg
import PIL
import PIL.Image
import os


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)




def download_image(link):
    import requests
    response = requests.get(link)
    file = open(f'images/nh/{link.split("/")[-1]}', "wb")
    file.write(response.content)
    # return response

def download_images():
    number = '330300'
    link = f'https://nhentai.net/g/{number}/'

    driver.get(link)
    #html_source = driver.page_source

    #print(html_source)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    low_quality = False
    thumbs = soup.find('div', {'class': 'thumbs'})
    print(thumbs.children)
    # images = []
    if low_quality:
        for i, child in enumerate(thumbs.children):
            img_link = child.find('img').get('data-src')
            download_image(img_link)
            print(img_link)
        # images.append(download_image(img_link))
    else:
        driver.get(link+'/1/')
        page_html = BeautifulSoup(driver.page_source, 'html.parser')
        print('ALO?')
        img_el = page_html.find('section', {'id': 'image-container'}).find('img')
        # <img height="1860" src="https://i3.nhentai.net/galleries/1741848/1.jpg" width="1280"/>
        img_link = img_el.get('src')
        gallery_number = img_link.split('/galleries/')[1].split('/')[0]
        img_format = img_link.split('/galleries/')[1].split('/')[1].split('.')[1]
        ts = [i for i in thumbs.children]
        for i in range(len(ts)):
            download_image(f'https://i5.nhentai.net/galleries/{gallery_number}/{i+1}.{img_format}')
        # print(page_html.find('section', {'id': 'image-container'}).find('img').get('src'))
    #     for i, child in enumerate(thumbs.children):
    #         img_link = child.find('img').get('data-src')
    #         download_image(img_link)
    #         print(img_link)


def download_pdf():
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

download_images()
download_pdf()
