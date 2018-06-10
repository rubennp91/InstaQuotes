# InstaQuotes
This is a tool for creating non-motivational posters. Just give it an instagram profile, a wikiquote name to search and a language.

Call example:
```
InstaGibberish.py natgeo "Snoop Dogg" en
```
It will ask for an instagram username and a password. If not provided it will fetch the public pictures.

Languages supported: en, es, de, fr, it

Quotes are necessary if the search for wikiquote has a space in between.

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

God, this code uses a lot of libraries for its lenght.

ruben.np91@gmail.com
