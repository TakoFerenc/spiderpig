# spiderpig

spiderpig (The Simpsons reference) is the first program I created
in python after studying python from multiple different sources
for a few weeks.

It's key functionalities are:
- collecting urls from sitemap like pages through webscrapping 
and storing those in files or an sqlite database
- verifying the urls directly from the sitemap or from a file or
sqlite database and saving the broken ones in a text file (results)
- create an sitemap like xml from urls from a file or an sqlite
database 

Warning:
Please note that the collecting of urls is specific to a sitemap 
I used: https://pythonprogramming.net/sitemap.xml
If anything else with a different format is used the code has 
to be adapted.Same format is used for the xml creation. 

Usage:

  > pip install -e .
  
  > spiderpig --help
