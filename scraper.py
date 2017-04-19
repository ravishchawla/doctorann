__author__ = 'Adamlieberman'
from bs4 import BeautifulSoup
from mechanize import Browser
import requests

'''
Scrape ICD-9 descriptions for a given ICD-9 code
'''

def scrape_icd9(codes):
    all_descriptions = []
    for c in codes:
        link = "https://www.findacode.com/code.php?set=ICD9&c="+str(c)
        html = requests.get(link).text
        soup = BeautifulSoup(html,"html.parser")
        blockquote = soup.find("div",{"class":"sectionbody"})
        ls = list(blockquote)
        count = 1
        for i in ls[1]:
            if count == 3:
                description = i.replace("-","").lstrip()
                all_descriptions.append(description)
                break
            count = count + 1
    return all_descriptions


def cliner_response(note):
    browser = Browser()
    browser.open('http://text-machine.cs.uml.edu/cliner/demo/cgi-bin/cliner_demo.cgi/')
    browser.select_form(nr=0)
    browser['user_input'] = note
    response = browser.submit()
    content = response.read()
    soup = BeautifulSoup(content,"lxml")
    cleaned_response = soup.find_all('p')[0]
    return cleaned_response
   # print type(content)


if __name__=="__main__":
    note = "Patient was admitted for a routine surgery on Thursday.  He had complications overnight and was transferred to the ICU."
    cleaned_response = cliner_response(note)
    print cleaned_response
    #codes = [250.01,250.02,250.03]
    #description = scrape_icd9(codes)
    #print description
