from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def search():
    search = input("Type to Search: ")
    param = {"q": search}
    r = requests.get("https://www.bing.com/images/search", params=param)

    dirName = search.replace(" ", "_").lower()
    if not os.path.isdir(dirName):
        os.makedirs(dirName)

    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.findAll("a", {"class": "thumb"})

    for item in result:

        try:
            image_obj = requests.get(item.attrs["href"])
            name = item.attrs["href"].split("/")[-1]

            try:
                image = Image.open(BytesIO(image_obj.content))
                image.save("./"+ dirName + "/" +name , image.format)
            except:
                print("Unable to Download this image")

        except:
            print("Couldn't request !")

    search()

search()