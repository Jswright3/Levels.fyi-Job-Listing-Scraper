import requests, re, selenium, time,sys
from selenium import webdriver
from bs4 import BeautifulSoup

def parse_input(argv):
    if len(argv) >= 2:
        url = argv[1]
        #Set default optional arguments
        minPay = -1
        tag = ""
        hasLink = False
        #Check and assign optional variable values
        for i in range(2,len(argv)):
            if argv[i].isdigit() == True:
                minPay = int(argv[i])
            elif argv[i] == "Y":
                hasLink = True
            else:
                tag = argv[i]
        #Call Scraper
        scraper(url, minPay, tag, hasLink)
    else:
        #Bad Input
        print("Levels.fyi Scraper usage: python3 scraper.py <url(string)> [minPay(int)] [tag(string)] [hasLink(char)]")
        print("variables in [] are optional, variables in <> are required\nhasLink is auto false, unless \"Y\" is provided in input")

def scraper(url, minPay, tag, hasLink):
    #Path of Chromedriver for the current build of Google chrome you are using
    chromePath = "./chromedriver"
    driver = webdriver.Chrome(chromePath)
    driver.get(url)
    #Scroll to bottom of page and wait 5 seconds to ensure complete loading of javascript elements
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    #Gathers source code for url
    source = driver.page_source
    driver.quit()
    #Builds BeautifulSoup that we can query
    soup = BeautifulSoup(source,"html.parser")
    #located table containing job listings
    table = soup.find('table', class_ = "table internships-table table-borderless table-condensed")
    #grabs all table rows in job listing table
    result = table.find("tbody").find_all("tr")
    result_index = 0
    for company in result:
        try:
            #retrieves the important details from each job listing
            name = company.contents[0].find("h6").getText() #name
            hourly = company.contents[1].find("h6").getText()#hourly pay
            location = company.contents[0].find("p").getText() #location
            benefits =  company.contents[2].find("p").getText()  #benefits
            link = company.contents[3].find("a")["href"]
            #Parsing job listings by the arguments given
            if minPay == -1 or (int(re.sub("[^0-9]","",hourly)) > int(minPay)):
                if (hasLink == True and link.find("docs.google") == -1) or hasLink == False:
                    if (tag != "" and (location.find(tag) != -1 or benefits.find(tag) != -1)) or tag == "":
                        print(f"Job Result #{result_index}\n"+name.strip()+"\n"+hourly+"\n"+benefits+"\n"+location+"\n"+str(link)+"\n")
                        result_index += 1
        #Ignores the Errors that result from attempting to access data that is missing from the listing
        except AttributeError:
            pass
    return

if __name__ == "__main__":
    parse_input(sys.argv)
