# ChessGamesComDownloader
Download game collections from http://www.chessgames.com

## Description

This is a Python command-line application that scrapes game data from a specified chess games collection URL on chessgames.com. It extracts the Portable Game Notation (PGN) for each game and saves the information to an output file. This allows you to conveniently gather games for analysis or personal review.

## Installation

Before running the Chess Games Scraper, make sure you have Python and the required packages installed:

1. Python 3.x (The script is compatible with Python 3, not Python 2)
2. `requests` library
3. `beautifulsoup4` library

To install the required packages, run:

```bash
pip install requests beautifulsoup4
```

## Usage

To use the Chess Games Scraper, navigate to the directory containing the script and run the following command in the terminal:

```bash
python chess_scraper.py <Collection_URL> <Output_PGN_Filename>
```

Replace `<Collection_URL>` with the full URL of the www.chessgames.com games collection page you wish to scrape. Replace `<Output_PGN_Filename>` with the filename you want to save the PGN data as.

For example:

```bash
python chess_scraper.py "https://www.chessgames.com/perl/chesscollection?cid=1049411" "my_chess_games.pgn"
```

This will scrape the games from the collection at the provided URL and save the PGN data to "my_chess_games.pgn".

### Notes

- Ensure the output directory exists before running the scraper or the script might throw an error.
- Use quotes around URLs and filenames if they contain special characters or spaces.

## License

[MIT](https://choosealicense.com/licenses/mit/)