import webbrowser

import requests as requests

http = input("Podaj stronę internetową (pisać bez http://): ")
timestamp = input ("Podaj rok dla tej strony (2006.01.01 -> 20060101): ")
#timestamp2 = 20030101
#timestamp3 = 20120101


url = "http://web.archive.org/web/"+str(timestamp)+"/http://"+http
response = requests.get(url)
d = response.json()
page = d["archived_snapchots"]["closest"]["url"]
#webbrowser.open("http://web.archive.org/web/" + timestamp + "/" + "http://" + url);