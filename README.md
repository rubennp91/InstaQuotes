# InstaQuotes
This is a tool for creating non-motivational posters. Just give it an instagram profile, a wikiquote name to search and a language.

Call example:
```
InstaGibberish.py natgeo "Snoop Dogg" en
```
The login is by default deactivated but it can be activated by uncommenting the lines in getLogin. Without an approved follow and a login you can only download the public pictures, which is what the script does by default.

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

ruben.np91 at gmail.com
