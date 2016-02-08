#Scraping SRM University's main web page to check if the results have been declared or not.

from bs4 import BeautifulSoup
import urllib.request, time, webbrowser, os

BASE_URL = "http://www.srmuniv.ac.in/Announcements"
RESULT_URL = "http://www.srmuniv.ac.in/"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
music_path = 'F:/Songs/English/siren.mp3'

keywords = ['Results', 'E&T', 'B.Tech', '7th', 'Semester', '2012']

def checkForSem(heading):
    if all(key in heading for key in keywords):
        return True
    else:
        return False

def main():
    url = urllib.request.urlopen(BASE_URL)
    soup = BeautifulSoup(url.read(), 'html.parser')
    content_class = soup.find_all('div', class_="col-lg-10  col-xs-10 col-sm-10 col-md-10 latest-text padding-left-10px")
    for heading in content_class:
        content_heading = heading.find('h4').get_text()
        page_url = heading.find('a')['href']
        print(RESULT_URL + page_url)
        results_out = checkForSem(content_heading)
        print("results: " + str(results_out))
        print(content_heading)
        if results_out:
            os.startfile(music_path)
            webbrowser.get(chrome_path).open(RESULT_URL + page_url)
            break
    time.sleep(2)


main()