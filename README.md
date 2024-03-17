This repository contains scripts for collecting data from web pages and books using web scraping techniques. 

## Web Scraping

 **Scraping Medical Data from a Website** - *pharmacy website*

The `collect_med.py` script retrieves medical data from a website by iterating over a range of IDs and extracting information from each corresponding webpage. The extracted data includes attributes such as name, price, and company. The collected data is saved into a CSV file named `items.csv`.

**Scraping Book Metadata from Project Gutenberg** - *books website*

The `getbook.py` script extracts metadata from books available on Project Gutenberg. It retrieves information such as the book title and language by accessing the text files of each book. The collected metadata is saved into a CSV file named `books-dectionary.csv`, and the text content of each book is saved into separate text files within the `Books` folder.
