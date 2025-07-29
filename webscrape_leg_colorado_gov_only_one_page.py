#this does the same thing as the other webscraper, but does not iterate
#this works best for scraping single pages

import requests
from html.parser import HTMLParser
import re
import os

def getPDF():
        url = 'URL' #add URL to scrape
        response = requests.get(url)
        text = response.text
        links = re.findall('https://leg.colorado.gov/sites/default/files/documents/.*pdf',text)

        download_dir = "FOLDER NAME" #name the folder you would like to download to, this makes a folder
        os.makedirs(download_dir, exist_ok=True)
        
        for link in links:
            try:
                filename = os.path.join(download_dir, os.path.basename(link))
                r = requests.get(link, stream=True)
                if r.status_code == 200:
                    with open(filename, 'wb') as f:
                        f.write(r.content)
            except requests.exceptions.RequestException as e:
                 print(f"Error downloading {link}: {e}")
    
getPDF()
