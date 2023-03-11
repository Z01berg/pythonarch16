import requests
import webbrowser

def get_archived_pages(pageurl, dates):
    archived_pages = []
    for date in dates:
        url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
        response = requests.get(url)
        d = response.json()
        if "archived_snapshots" in d and "closest" in d["archived_snapshots"]:
            page = d["archived_snapshots"]["closest"]["url"]
            archived_pages.append(page)
    return archived_pages

pageurl = "https://www.ukr.net/"
dates = ["20060101", "20100101", "20190101"]
archived_pages = get_archived_pages(pageurl, dates)
for page in archived_pages:
    webbrowser.open(page)