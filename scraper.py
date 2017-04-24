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
        c = str(c)

        #If we have a .00 ICD9 code
        if c[-2:] == ".0":
            print "here"
            code = c+"0"
            link = "https://www.findacode.com/code.php?set=ICD9&c="+code
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

        #If we have a .XX ICD9 code
        else:
            link = "https://www.findacode.com/code.php?set=ICD9&c="+c
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





def scrape_icd92(codes):
    all_descriptions = []
    for c in codes:
        num_try = 0
        result = None
        try:
            c = str(c)
            link = "https://www.findacode.com/code.php?set=ICD9&c="+c
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
        except(TypeError, KeyError) as e:
            try:
                c1 = str(c) +".0"
                link = "https://www.findacode.com/code.php?set=ICD9&c="+c1
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
            except(TypeError, KeyError) as e:
                try:
                    c2 = str(c) +".00"
                    link = "https://www.findacode.com/code.php?set=ICD9&c="+c2
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
                except:
                    all_descriptions.append("Desctiption for ICD-9 code "+str(c)+" is not available.")
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
    #note = "Patient was admitted for a routine surgery on Thursday.  He had complications overnight and was transferred to the ICU."
    #cleaned_response = cliner_response(note)
    #print cleaned_response
    #codes = [250.01,250.02,250.03]
    #description = scrape_icd9(codes)
    #print description
    #x = "598.00"
    #print x[-2:]
    #codes = [250.00]
    #codes = ['598','340','E932']
    codes = ['518', '427', '584']
    description = scrape_icd92(codes)
    print description

