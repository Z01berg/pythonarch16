import sys
import wikipediaapi

def read_titles(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

def get_article(title, lang="en"):
    w_api = wikipediaapi.Wikipedia(lang)
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""

titles_generator = read_titles("small.txt")
total_letter_count = 0
article_count = 0

for title in titles_generator:
    article = get_article(title)
    letter_count = len(set(article.replace(" ", "")))  # Counting distinct letters
    total_letter_count += letter_count
    article_count += 1

if article_count > 0:
    average_letter_count = total_letter_count / article_count
    print("Average number of letters per article:", average_letter_count)
else:
    print("No articles found.")
