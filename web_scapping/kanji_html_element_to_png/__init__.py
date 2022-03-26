from email.mime import image
from fileinput import filename
from os import link
from html2image import Html2Image
import requests
from bs4 import BeautifulSoup
hti = Html2Image()
from time import time
from convert import romajiToJapanese
from os.path  import basename
from urllib.parse import quote


# hti.screenshot(url='https://www.romajidesu.com/kanji/%E6%AF%8E', save_as='kanji.png')
# hti.screenshot(
#     html_file='kanji_page.html', css_file='kanji_style.css',
#     save_as='kanji.png'
# )

begin = time()

def get_html_from_url(url: str):
    req = requests.get(url)
    return BeautifulSoup(req.content, 'html.parser')

def download_image(url: str):
    with open(basename(url), "wb") as f:
        f.write(requests.get(url).content)

def search_on_nihongoichiban(searched_kanji: str, jlpt='n5') -> dict:
    # n5, n4 and n3
    url_dict = {
        "n5": "https://nihongoichiban.com/2011/04/10/complete-list-of-kanji-for-jlpt-n5/",
        "n4": "https://nihongoichiban.com/2011/05/22/complete-list-of-kanji-for-the-jlpt-n4/",
        "n3": "https://nihongoichiban.com/2014/07/22/complete-list-of-kanji-for-jlpt-n3/"
    }
    soup = get_html_from_url(url_dict[jlpt])
    rows = soup.find_all("tr")
    rows.pop(0)
    rom_katakana = ''
    for row in rows:
        kanji_column = row.findChildren()[1]
        kanji_link = kanji_column.findChildren()[0]
        if kanji_link.getText() == searched_kanji:
            code = row.findChildren()[0].getText().strip()
            # https://nihongoichiban.com/2011/04/11/%e6%82%aa/
            # ['2011', '04', '11', '%e6%82%aa', '']
            link = kanji_link['href']
            soup = get_html_from_url(link)
            table = soup.find_all("tbody")[0]
            rom_rows = table.find_all("td")
            meaning = rom_rows[2].getText()
            rom_katakana = rom_rows[3].getText()
            rom_hiragana = rom_rows[5].getText()
            rom_katakana = rom_katakana.replace('(', '•').replace(')', '').replace(',', '、')
            rom_hiragana = rom_hiragana.replace('(', '•').replace(')', '').replace(',', '、')
              
            link_info = link.split('nihongoichiban.com/')[1].split('/')
            year = link_info [0]
            month = link_info[1]
            img_url = f'https://nihongoichibandotcom.files.wordpress.com/{year}/{month}/{code.lower()}.gif'
            download_image(img_url)    
            return {
                'kanji': searched_kanji,
                'onyomi': rom_katakana,
                'kunyomi': rom_hiragana,
                'meaning': meaning,
                'link': link
            }
    return None
    

def search_on_romajidesu(searched_kanji: str) -> dict:
    url = f"http://www.romajidesu.com/kanji/{quote(searched_kanji)}"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    div_kanji_info = soup.find_all("div", class_="kanji_meaning")[0]
    meaning = div_kanji_info.findChildren()[0].findChildren()[1].getText()
    meaning = meaning.strip().replace(';', ',').title()
    
    onyomis = div_kanji_info.find_all("div", class_="on_yomi")[0]
    kunyomis = div_kanji_info.find_all("div", class_="kun_yomi")[0]
    
    def get_kana(kanas):
        def get_rid_of_romanji(text):
            final = ''
            for char in text:
                if not char.isascii() and char not in 'kō':
                    final += char
            return final

        kana = ''
        for k in kanas:
            text:str = k.getText().replace(" ", "").replace("\n", "").replace(".", "•").replace("·", "")
            if text != "":
                kana += f'{get_rid_of_romanji(text)}、'
        return kana[:-1]
    
    onyomi = get_kana(onyomis)
    kunyomi = get_kana(kunyomis)
    
    str_file = '<html>'
    for script in soup.find_all("script"):
        content = str(script)
        if 'uniconsent' not in content:
            str_file += content + '\n\n'
    str_file += str(soup.find_all("div", class_="kanji_strokes_order")[0])
    str_file += '</html>'

    with open("kanji_page.html", "w", encoding="utf-8") as file:
        file.write(str_file)
    
    div_kanji_info = soup.find_all("div", class_="kanji_info")[0]
    stroke_count = int(div_kanji_info.findChildren("a")[0].findChildren("b")[0].getText())
    width = 10 if stroke_count >= 10 else stroke_count
    height = 1 if stroke_count <= 10 else (2 if stroke_count <= 20 else 3)
    hti.screenshot(
        html_file='kanji_page.html', save_as='kanji.png', size=(width*58 + 20, height*58 + 20)
    )
    return {
        'kanji': searched_kanji,
        'onyomi': onyomi,
        'kunyomi': kunyomi,
        'meaning': meaning,
        'link': url
    }


def search_kanji():
    kanji = str(input('Enter with kanji: ')).strip()
    jlpts = ['n5', 'n4', 'n3']
    for jlpt in jlpts:
        print(f'Searching on {jlpt} nihongoichiban...')
        r = search_on_nihongoichiban(jlpt)
        if r:
            return r

    print(f'Searching on romajidesu...')
    return search_on_romajidesu(searched_kanji = kanji)

print(search_kanji())

print(time() - begin)

""" str()
print(str(soup)) """

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
""" page = urllib3.urlopen("https://www.romajidesu.com/kanji/%E6%AF%8E")
print(page) """

""" url = 'https://www.romajidesu.com/kanji/%E6%AF%8E'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
image_ = soup.find_all('svg')
# image_ = image_.find('svg')
image_ = [i.find('svg') for i in image_]

for index, i in enumerate(image_):
    with open(f'image_{index}.svg', 'w') as f:
        f.write(str(i)) """
