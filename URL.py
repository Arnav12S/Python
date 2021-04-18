import requests
import csv
from bs4 import BeautifulSoup

search_urls = []  # To store search URLs from the input CSV
profile_urls = []  # To store the Profile URLs

pg_count = 0  # To traverse through Google results pages
# Loop through first 15 pages (10 per page, so count 15*10=150)

logging = 0  # Logging toggle, change to 1 for detailed print statements


# Loading search URLs from input CSV to search_urls[]
def load_search_urls():
    global search_urls
    global logging

    csv_file = open('/Users/arnav/Downloads/all_connections.csv', mode='r')
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are:{}'.format(",".join(row)))
        search_urls.append(row["search_url"])
        line_count += 1
    print('Processed {} lines'.format(line_count))
    csv_file.close()


# Checking if URLs from Google search are of the proper format
def is_required_format(url):
    if "https://www.linkedin.com/" in url and not url.startswith("https://www.google.com/"):
        return True
    return False


# Scraping Google results and storing results to profile_urls[]
def browse_search_urls():
    global search_urls
    global profile_urls
    global logging

    # NOTE: Change to required number of pages
    pgs_to_browse = 1
    # search_urls = search_urls[:50]

    log("URLs in search_urls:{}".format(len(search_urls)), logging)
    for search in search_urls:
        log("Browsing for entry:{}..".format(search), logging)
        pg_count = 0
        while pg_count < pgs_to_browse:
            query = search + str(pg_count)
            log("Query:{}".format(query), logging)
            print("Query:{}".format(query))
            response = requests.get(query)
            soup = BeautifulSoup(response.text, 'html.parser')
            for anchor in soup.find_all('a'):
                url = anchor["href"]
                log("URL:{}".format(url), logging)
                if is_required_format(url):
                    url = url[7:url.find('&')]
                    profile_urls.append([url])
            pg_count = pg_count + 1


def write_results():
    global profile_urls
    global logging

    fd = open('/Users/arnav/Downloads/linkedin_similar_connections.csv', 'w')
    writer = csv.writer(fd)
    writer.writerows(profile_urls)
    fd.close()


def log(stmt, isOn):
    if isOn:
        print(stmt)


if __name__ == "__main__":
    load_search_urls()
    browse_search_urls()
    write_results()
