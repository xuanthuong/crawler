from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError
from urllib.request import urlretrieve
import os
import pathlib


main_url = "http://gocthugian.com.vn"
dragonball_url = "http://gocthugian.com.vn/truyen/t178/"
IMG_DIR = './Dragonball/'


def save_image(img_url):
    response = requests.get(fileURL, stream=True)
    # newfilepath = local path to save file
    filedata = file(newfilepath, "wb")
    for block in response.iter_content(1024):
        if not block:
            break
        filedata.write(block)

    import requests
    f = open('00000001.jpg', 'wb')
    f.write(requests.get('http://www.gunnerkrigg.com//comics/00000001.jpg').content)
    f.close()


def save_image_with_url(img_url, path=None):
    try:
        urlretrieve(img_url, path)
    except FileNotFoundError as err:
        print(err)   # something wrong with local path
    except HTTPError as err:
        print(err)  # something wrong with url


def get_volumns(mainpage_url):
    vols_list = []
    vols = requests.get(mainpage_url)
    vols_soup = BeautifulSoup(vols.text, 'lxml')

    # Tra ve list cac the chua thong tin cac vol
    vols_url = vols_soup.find_all('li', attrs={"class": "VI"})
    for tag in vols_url:
        # Duong link cua vol nam trong the div, class: VII
        tmp = tag.find('div', attrs={"class": "VII"})
        link = tmp.find('a', href=True)
        vols_list.append(link['href'])
    return vols_list


def get_chapters(volumn_url):
    chapters_list = []
    chapters = requests.get(volumn_url)
    chapters_soup = BeautifulSoup(chapters.text, 'lxml')

    chapters_url = chapters_soup.find_all('td', attrs={"class": "ChI"})
    for ch in chapters_url:
        link = ch.find('a', href=True)
        chapters_list.append(link['href'])
    return chapters_list


def make_chapter_dir(ch_name):
    ch_name = ch_name.find('h1').string.split("-")
    ch_name = [ch.replace('\r', '').replace(
        '\n', '').replace('\t', '') for ch in ch_name]
    ch_name = [" ".join(ch.split()) for ch in ch_name]
    chapter_dir = IMG_DIR + ch_name[1] + '/' + ch_name[2] + ' - ' + ch_name[3]
    pathlib.Path(chapter_dir).mkdir(parents=True, exist_ok=True)
    return chapter_dir


def download_chapter(chapter_url):
    chapter = requests.get(chapter_url)
    chapter_soup = BeautifulSoup(chapter.text, 'lxml')

    ch_name = chapter_soup.find('div', attrs={"class": "FPH"})
    chapter_dir = make_chapter_dir(ch_name)

    img_url = chapter_soup.find('div', attrs={"class": "TTCD"})
    # contents = img_url.contents
    # tuong duong voi img_url.contents nhung .contents lay het, con cai nay lay <img>
    contents = img_url.find_all('img')
    for i in range(len(contents)):
        tmp_fname = "{0:0>3}".format(i) + ".jpg"
        tmp_path = os.path.join(chapter_dir, tmp_fname)
        save_image_with_url(contents[i]['src'], tmp_path)
        print("Saved file: %s" % tmp_path)


def main():
    # vols_list = get_volumns(dragonball_url)
    # for vol in vols_list:
    #     chapters_list = get_chapters(vol)
    #     for ch in chapters_list:
    #         download_chapter(ch)
    get_volumns("http://gocthugian.com.vn/truyen/t178/")


if __name__ == "__main__":
    main()
    # download_chapter("http://gocthugian.com.vn/truyen/c21008/")
