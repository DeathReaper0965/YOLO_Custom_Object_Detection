import os
import urllib.request as ulib
import json
from bs4 import BeautifulSoup as Bsoup


def find_links(name):
    name = name.replace(" ", "+")

    url_str = 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}' + \
              '\&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}' + \
              '\&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg' + \
              '\.i&ijn=1&asearch=ichunk&async=_id:rg_s,_pms:s'

    headers = {"User-Agent": "Chrome/65.0.3325.162 Safari/537.36", "Content-Type": "application/json"}
    url_str = url_str.format(name, 0)
    print(url_str)
    request = ulib.Request(url_str, None, headers)
    json_str = ulib.urlopen(request).read()
    json_str = json.loads(json_str)
    soup = Bsoup(json_str[1][1], 'lxml')
    soup_imgs = soup.find_all("img")
    img_links = [img["src"] for img in soup_imgs]
    return img_links

def download_images(links, name):
    dir_name = name.replace(" ", "_")
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    for i, img_link in enumerate(links):
        img_path = os.path.join(dir_name, "{:06}.png".format(i))
        ulib.urlretrieve(img_link, img_path)

if __name__ == "__main__":

    search_str = "yoyo"
    links = find_links(search_str)
    download_images(links, search_str)

    print("downloding images.... done!!!")