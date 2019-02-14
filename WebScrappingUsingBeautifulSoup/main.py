import requests
from bs4 import BeautifulSoup

search_para = input("Enter Search keyword: ")
parameter = {"q": search_para}
r = requests.get("https://www.bing.com/search", params=parameter)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class":"b_algo"})

for item in links:
    item_name = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_name and item_href:
        print(item_name)
        print(item_href)
        print("Parent : ", item.find("a").parent.parent.find("p").text)