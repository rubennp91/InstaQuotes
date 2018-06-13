# InstaQuotes
This is a tool for creating non-motivational posters. Just give it an instagram profile, a wikiquote name to search and a language.

Call example:
```
python InstaQuotes.py natgeo "Snoop Dogg" en
```
The script collects the latest 20 uploaded instagram pictures in that profile and selects a random one. Then it collects a random quote found inside the wikiquote page and puts it together in a picture that will be saved inside the folder where the script is located.

An instagram login can be used to download pictures from private profiles, but only if the account you're logging in has an approved follow. This login is by default deactivated but it can be activated by uncommenting the lines in getLogin. The username and password are not stored anywhere.

The quote retrieved from wikiquotes can be downloaded in the following languages: en, es, de, fr, it

Quotes (") are necessary when inputting the page parameters if the search for wikiquote has one space or more in between (e.g. "Snoop Dogg").

The fonts are searched inside the ./fonts folder. More fonts can be included and the script will randomly select one each time. The text is written inside an outline so it can be better read.

Tools used:
* instagram-scraper (https://github.com/rarcega/instagram-scraper)

Libraries used:
* wikiquotes (https://github.com/FranDepascuali/wikiquotes-python-api)
* os
* time
* sys
* getpass
* random
* PIL

Font used:
* IndieFlower.ttf (https://fonts.google.com/specimen/Indie+Flower)

ruben.np91 at gmail.com
