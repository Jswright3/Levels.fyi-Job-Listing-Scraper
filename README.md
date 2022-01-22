<h1>Levels.fyi Job Posting Scraper</h1>

Dependencies:

    pipenv
        Manages project dependencies.
        Installation and documentation: https://pipenv.pypa.io/en/latest/

    BeautifulSoup4
        Creates a queryable object of the source code.

    Selenium
        Allows the scraper to render javascript elements so it can get the entire source code.

    Requests
        Allows for easy HTTP requests.

    ChromeDriver: 
        ChromeDriver for the current build of Google Chrome your system has.
        Allows Selenium to open and run chrome to gather webpage data.
        Releases found here: https://chromedriver.chromium.org/downloads

Scraper Usage (variables in [] are optional, variables in <> are required):
    

    python3 scraper.py <url> [minPay] [tag] [hasLink]

    <url> (string): url to level.fyi page containing job listings to search, 
        MUST BE IN QUOTES TO PASS THROUGH COMMANDLINE

    [minPay] (int): minimum hourly wage for job search.

    [tag] (string): single word string that must appear in job listing.

    [hasLink] (char): only returns jobs with an application hasLink
            Default is false, to make true pass argument "Y"

Setup:

    1. This scraper uses pipenv to manage the dependencies. There is a link above to the installation page.
    
    2. Once pipenv is installed you can use "pipenv install" to install all required dependencies in a virtual environment
       You may have to prefix the pipenv command with "python3 -m" depending on your system and PATH configuration.

    3. To run the scraper follow the usage above



Example Usage: (my system requires the prefix "python3 -m" to run pipenv):

python3 -m pipenv run python3 scraper.py "https://www.levels.fyi/internships/?track=Software%20Engineer" remote 20 Y > remoteOver20.txt

Explaination of arguments passed into scraper.py

    "https://www.levels.fyi/internships/?track=Software%20Engineer":  Runs the scraper on Job Postings from given link

    "remote":   Checks if listing contains the tag "remote" anywhere in the posting.

    "20" :  Checks that Job posting has a pay of at least $20 per hour

    "Y" : returns only jobs that have a valid application link


https://user-images.githubusercontent.com/26271194/150628205-427b588c-c5ac-4afa-a70f-58c08b9bf786.mp4
