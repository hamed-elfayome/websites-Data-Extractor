import requests
from bs4 import BeautifulSoup
import csv

# Define the range of IDs you want to scrape
start_id = 1
end_id = 33900

# Define the batch size and intervals for progress saving
batch_size = 1000

csv_file_path = "items.csv"

for i in range(start_id, end_id + 1):
    # Replace with the URL of the website you want to scrape
    url = f"https://dwaprices.com/med.php?id={i}"

    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Locate the <tbody> tag you want to extract data from
            table = soup.find("table")

            data_list = []

            if table:
                # Find all <tr> elements within <tbody>
                tr_elements = table.find_all("tr")

                for tr in tr_elements:
                    # Find all <td> elements within the <tr>
                    td_elements = tr.find_all("td")

                    # Skip the first <td> element and print the content of the second <td>
                    if len(td_elements) >= 2:
                        # Get the text content of the second <td>
                        data_list.append(td_elements[1].text.strip())

                if not data_list[5].isnumeric():
                    data_list[5] = ""

                with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(data_list)

            print(f"Processed: {i}/{end_id}  -  %{round(i / end_id * 100, 2)}", end="\r")

        else:
            print(f"Failed to retrieve the webpage for ID {i}. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error occurred for ID {i}: {str(e)}")


print("Scraping completed.")