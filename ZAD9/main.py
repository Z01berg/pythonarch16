import sys
import wikipediaapi

def read_titles(filename):
  with open(filename, "r") as file:
    for line in file:
      yield line.strip()

titles_generator = read_titles("small.txt")
print(sys.getsizeof(titles_generator))

def get_article(title,lang="en"):
  w_api = wikipediaapi.Wikipedia(lang)
  page = w_api.page(title)
  if page.exists():
    return page.text
  else:
    return ""

title = next(titles_generator)
print("title1",title)
art = get_article(title)
print(art)
title=next(titles_generator)
print("Tytul 2:",title)
art2 = get_article(title)
print(art)