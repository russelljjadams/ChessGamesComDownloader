import sys
import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/99.0.4844.51 Safari/537.36')
}

def get_game_links(collection_url):
    response = requests.get(collection_url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        return ["https://www.chessgames.com" + link.get('href') for link in soup.find_all('a', href=True) if "gid=" in link['href']]
    else:
        print("Error fetching the collection page.")
        return []

def get_pgn(game_url):
    response = requests.get(game_url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        pgn_data = soup.find('div', {'id': 'olga-data'})
        if pgn_data:
            return pgn_data.get('pgn').replace('\\r\\n', ' ').strip()
    return None

def main(collection_url, output_file):
    game_links = get_game_links(collection_url)
    pgns = []
    for game_url in game_links:
        pgn = get_pgn(game_url)
        if pgn:
            pgns.append(pgn)

    # Ensure that the directory for the output file exists
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write the PGNs to the output file
    with open(output_file, 'w') as pgn_file:
        for pgn in pgns:
            pgn_file.write(pgn + '\n\n')
    
    print(f"All PGNs have been saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scriptname.py <URL of the Games Collection page> <Output PGN file name>")
        sys.exit(1)
    collection_url = sys.argv[1]
    output_file = "./collections/" + sys.argv[2]
    main(collection_url, output_file)