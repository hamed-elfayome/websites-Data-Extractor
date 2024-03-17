import requests
import re
import csv

def extract_title(text):
    title_match = re.search(r"Title:\s+(.*)", text)
    if title_match:
        return title_match.group(1)
    return None

def extract_language(text):
    language_match = re.search(r"Language:\s+(.*)", text)
    if language_match:
        return language_match.group(1)
    return None

def print_loading_bar(progress, total,now,sum, bar_length=50):
    filled_length = int(bar_length * progress / total)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    percentage = progress / total * 100
    print(f"Progress: [{bar}] {percentage:.2f}% [{now}/{sum}]", end='\r')

def get_book_text(book_id):
    # Try different URL formats
    url_formats = [
        f"https://www.gutenberg.org/files/{book_id}/{book_id}.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-1.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-2.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-3.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-4.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-5.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-6.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-7.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-8.txt",
        f"https://www.gutenberg.org/files/{book_id}/{book_id}-9.txt",
    ]

    for url in url_formats:
        response = requests.get(url)
        if response.status_code == 200:
            text = response.text
            if text != "" and text != None:
                return response.text

    return None


def remove_text_before_second_three_stars(text):
    # Find the indices of the second and third occurrences of '***'
    second_index = text.find('***', text.find('***') + 3)
    third_index = text.rfind('***')
    if second_index != -1 and third_index != -1:
        # Extract the text after the second '***'
        cleaned_text = text[third_index + 3:]
        return cleaned_text

    return None


total = 100


for book_id in range(1,total):
    book_text = get_book_text(book_id)
    if book_text is not None:
        title = extract_title(book_text[:1000])
        language = extract_language(book_text[:1000])

        T = f"{title[:-1]} " if title else "None"
        L = f"{language[:-1]}" if language else "None"
        with open('books-dectionary.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
             # Check if the file is empty
            file_empty = csvfile.tell() == 0

            # Write the label row if the file is empty
            if file_empty:
                csv_writer.writerow(['Book ID', 'Title', 'Language'])

            csv_writer.writerow([book_id, T, L])
        
        cleaned_text = remove_text_before_second_three_stars(book_text)
        if cleaned_text != None and cleaned_text != "": 
            with open(f'books/{book_id}.txt', 'a', encoding='utf-8') as file:
                file.write(cleaned_text)
        else:
            with open(f'books/{book_id}.txt', 'a', encoding='utf-8') as file:
                file.write(book_text)
        

    print_loading_bar(book_id, total,book_id ,total)