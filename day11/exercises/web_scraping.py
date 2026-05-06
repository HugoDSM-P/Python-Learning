import bs4
import requests

result = requests.get("https://www.scrapethissite.com/pages/")
img_scrap = requests.get("https://www.scrapethissite.com/lessons/sign-up/")

parsing = bs4.BeautifulSoup(result.text, "lxml")
img_parsing = bs4.BeautifulSoup(img_scrap.text, "lxml")

# Get the text of the element <title>

print(parsing.select("title")[0].getText())

# Print the text of the third <p>

print(parsing.select("p")[3].getText())

# Get all the text from elements <p> inside the class .page

content_p = parsing.select(".page p")

for p in content_p:
    print(p.getText())

# Download the first image of the page with the class img-responsive.img-circle.screenshot

img = img_parsing.select(".img-responsive.img-circle.screenshot")[0]["src"]

img_bin = requests.get("https://www.scrapethissite.com" + img)

# "wb" makes Python to understand that you're going to write in binary

f = open("img.png", "wb")
f.write(img_bin.content)
f.close()