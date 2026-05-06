import bs4
import requests


base_url = "https://books.toscrape.com/catalogue/page-{}.html"
high_rated_books = []

# Iterate pages

for page in range(1, 51):
    
    # Parse every page

    page_url = base_url.format(page)
    result = requests.get(page_url)
    parse = bs4.BeautifulSoup(result.text, "lxml")
    

    # Select the data of the books

    books = parse.select(".product_pod")

    # Iterate books

    for book in books:
        
        # Check the rating of the book

        if len(book.select(".star-rating.Four")) != 0 or len(book.select(".star-rating.Five")) != 0:

            # Save the title in a variable
            
            book_title = book.select("a")[1]["title"]

            # Add book to the list

            high_rated_books.append(book_title)

for t in high_rated_books:
    print(t)