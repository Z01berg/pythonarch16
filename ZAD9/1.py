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

def count_unique_letters(article):
    unique_letters = set(article)
    return len(unique_letters)

def calculate_average_letters(filename):
    titles_generator = read_titles(filename)
    total_letters = 0
    article_count = 0

    for title in titles_generator:
        article = get_article(title)
        total_letters += count_unique_letters(article)
        article_count += 1

    if article_count > 0:
        average_letters = total_letters / article_count
        return average_letters
    else:
        return 0

average_letters = calculate_average_letters("small.txt")
print("Średnia liczba liter na artykuł:", average_letters)
