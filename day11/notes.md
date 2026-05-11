# Day 11 – Web Scraping with Python (BeautifulSoup & Requests)

Today I started working with web scraping in Python, learning how to extract and process data from websites using `requests` and `BeautifulSoup`.

## What I learned

### HTTP Requests

- Sending GET requests using the `requests` library
- Retrieving HTML content from web pages
- Working with different URLs and endpoints

### Web Scraping Basics

- Parsing HTML using `BeautifulSoup`
- Using different parsers like `lxml`
- Selecting elements using CSS selectors

### Data Extraction

- Extracting text from HTML tags like `<title>` and `<p>`
- Navigating and filtering DOM elements
- Selecting elements by class names

### Image Downloading

- Extracting image URLs from HTML attributes
- Downloading binary files using `requests`
- Saving images locally using file handling (`wb` mode)

## Mini Project – Book Scraper

I built a web scraper that:

- Navigates through multiple pages of a book website
- Extracts book titles from each page
- Filters books based on rating (4 and 5 stars only)
- Stores and prints a list of high-rated books

## Summary

This day helped me understand how to extract real-world data from websites and how Python can automate data collection tasks using web scraping techniques.