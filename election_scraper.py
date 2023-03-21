"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Bara Karlinova
email: bara.karlinova@kiwi.com
discord: BaraKar#6094
"""

# import libraries
import sys
import requests
import bs4
import inspect
import csv
import traceback

from bs4 import BeautifulSoup
from urllib.parse import urljoin


initial_url = 'https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ'


# get cities with related urls
def cities_urls(url: str, tr_tag: "bs4.element.ResultSet") -> dict:
    return {
        'city': tr_tag[1].get_text(),
        'url': urljoin(url, tr_tag[3].find('a')['href'])
    }


# get urls of city parts of chosen city
def city_parts_urls(url: str, tr_tag: "bs4.element.ResultSet") -> dict:
    if tr_tag[0].find('a') is not None:
        return {
            'url': urljoin(url, tr_tag[0].find('a')['href'])
        }


# get code and location of city parts of chosen city
def city_parts(tr_tag: "bs4.element.ResultSet") -> dict:
    return {
        'code': tr_tag[0].get_text(),
        'location': tr_tag[1].get_text()
    }


# get number of voters of city parts of chosen city
def city_parts_voters(tr_tag: "bs4.element.ResultSet") -> dict:
    return {
        'registered': tr_tag[3].get_text(),
        'envelopes': tr_tag[4].get_text(),
        'valid': tr_tag[7].get_text()
    }


# get number of votes by parties of city parts of chosen city
def city_parts_votes_by_party(tr_tag: "bs4.element.ResultSet") -> dict:
    return {
        tr_tag[1].get_text(): tr_tag[2].get_text()
    }


# scrape info from web
def get_web_results(url: str, results_func, td_len: int) -> list:
    server_answer = requests.get(url)
    soup = BeautifulSoup(server_answer.text, 'html.parser')

    all_tr = soup.find_all("tr")

    results = []

    for tr in all_tr:
        row_td = tr.find_all("td")
        if len(row_td) == td_len:
            if 'url' in str(inspect.signature(results_func)):
                if results_func(url, row_td) is not None:
                    results.append(results_func(url, row_td))
            else:
                if results_func(row_td) is not None:
                    results.append(results_func(row_td))

    return results


# get list of all cities available for scraping
def get_city(results: list) -> list:
    city = [element for element in results]
    cities_list = []
    for row in city:
        cities_list.append(row['city'])

    return cities_list


# get url of the chosen city
def get_url(city: str, results: list) -> str:
    city_url = [element for element in results if element['city'] == city]
    for row in city_url:
        return row['url']


# get urls of city parts of the chosen city
def get_url_city_part(results: list) -> list:
    list_of_urls = []
    for row in results:
        list_of_urls.append(row['url'])

    return list_of_urls


# check if enough arguments were passed when executing code through terminal
# check if correct city name was passed when executing code through terminal
# if not then exit
def arguments_check():
    if len(sys.argv) != 3:
        print('Incorrect number of parameters passed, two are required.')
        print('Execute the code as: python3 election_scraper.py <city-name> <output-file>.')
        exit()
    elif (sys.argv[1] not in get_city(get_web_results(initial_url, cities_urls, 4))) & \
            (len(sys.argv) == 3):
        print('Execute the code as: python3 election_scraper.py <city-name> <output-file>.')
        print('Select one of the following cities as <city-name>:')
        for i in range(0, len(get_city(get_web_results(initial_url, cities_urls, 4))), 5):
            x = i
            print(*get_city(get_web_results(initial_url, cities_urls, 4))[x:x + 5], sep=', ')
        exit()


# execute the arguments check
arguments_check()


# create lists with scraped data
def get_scraped_data() -> list:
    url_city = get_url(sys.argv[1], get_web_results(initial_url, cities_urls, 4))
    print(f'Extracting data from: {url_city}')

    url_city_part = get_web_results(url_city, city_parts_urls, 3)
    city_part = get_web_results(url_city, city_parts, 3)

    scraped_data = []

    for i in range(len(url_city_part)):
        data_prep = list()
        data_prep.append(city_part[i])
        data_prep += get_web_results(get_url_city_part(url_city_part)[i], city_parts_voters, 9)
        data_prep += get_web_results(get_url_city_part(url_city_part)[i], city_parts_votes_by_party, 5)
        data_prep_flatten = {}
        for item in data_prep:
            data_prep_flatten.update(item)
        try:
            del data_prep_flatten['-']
        except KeyError:
            pass
        scraped_data.append(data_prep_flatten)

    return scraped_data


# write the scraped data into csv
def write_data(data: list, file_name: str) -> str:
    try:
        csv_file = open(file_name + '.csv', mode='w', encoding='utf-8')
        columns = data[0].keys()
    except FileExistsError:
        return traceback.format_exc()
    except IndexError:
        return traceback.format_exc()
    else:
        write = csv.DictWriter(csv_file, fieldnames=columns)
        write.writeheader()
        write.writerows(data)
        return "Saved"
    finally:
        csv_file.close()


def main():
    write_data(get_scraped_data(), sys.argv[2])
    print(f'Saving data to file: {sys.argv[2]}.csv')
    print('Finishing')


if __name__ == "__main__":
    main()

