import webbrowser

url=input("Podaj stronę internetową (pisać bez http://): ")
timestamp = input ("Podaj rok dla tej strony (2006.01.01 -> 20060101): ")

webbrowser.open("http://web.archive.org/web/" + timestamp + "/" + "http://" + url)