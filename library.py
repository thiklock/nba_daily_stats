"""
This file shall hold all functions of the project
"""


# needed libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def per_game_scrapper():
    # URL to scrape
    url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html#per_game_stats"

    # collect HTML data
    html = urlopen(url)
        
    # create beautiful soup object from HTML
    soup = BeautifulSoup(html, features="lxml")

    # use getText()to extract the headers into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    hearders_spec = headers[1:30]
    print(hearders_spec)
    # get rows from table
    rows = soup.findAll('tr')[1:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
    # if you print row_data here you'll see an empty row
    # so, remove the empty row
    # rows_data.pop(20)
    # for simplicity subset the data for only 39 seasons
    # rows_data = rows_data[0:38]

    # we're missing a column for years
    # add the years into rows_data
    # last_year = 2020
    # for i in range(0, len(rows_data)):
        # rows_data[i].insert(0, last_year)
        # last_year -=1

    # create the dataframe
    nba_stats_21 = pd.DataFrame(rows_data, columns = hearders_spec)
    print(nba_stats_21)
    # export dataframe to a CSV , columns = headers
    nba_stats_21.to_csv("nba_stats_21.csv", index=False)
# scrapping done with the help of https://medium.com/analytics-vidhya/intro-to-scraping-basketball-reference-data-8adcaa79664a
print('function running')
per_game_scrapper()
print('function done')