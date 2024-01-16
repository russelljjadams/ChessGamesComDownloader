# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:07:42 2024

@author: rjadams
"""

import requests
from bs4 import BeautifulSoup

# User-Agent string to mimic a browser
headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/99.0.4844.51 Safari/537.36')
}

# The initial URL that contains links to all the games
collection_url = "https://www.chessgames.com/perl/chesscollection?cid=1049411"

# Function to extract game links from the collection page
def get_game_links(collection_url):
    response = requests.get(collection_url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        return ["https://www.chessgames.com" + link.get('href') for link in soup.find_all('a', href=True) if "gid=" in link['href']]
    else:
        print("Error fetching the collection page.")
        return []

# Function to extract PGN data from a single game page
def get_pgn(game_url):
    response = requests.get(game_url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        pgn_data = soup.find('div', {'id': 'olga-data'})
        if pgn_data:
            return pgn_data.get('pgn').replace('\\r\\n', ' ').strip()
    return None

# Main script logic
def main():
    # Get all game links from the collection page
    game_links = get_game_links(collection_url)
    
    # Iterate over game links and collect PGN data
    pgns = []
    for game_url in game_links:
        pgn = get_pgn(game_url)
        if pgn:
            pgns.append(pgn)
    
    # Save all PGN data into a single file
    pgn_filename = "spasskys_best_games.pgn"
    with open(pgn_filename, 'w') as pgn_file:
        for pgn in pgns:
            pgn_file.write(pgn + '\n\n')

    print(f"All PGNs have been saved to {pgn_filename}")

# Run the script
if __name__ == "__main__":
    main()