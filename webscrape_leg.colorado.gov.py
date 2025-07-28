#this script can be used to scrape the Colorado Legislature site for session laws.

import requests
from html.parser import HTMLParser
import re
import os


links = []

def PDF():
    count = 0
    
    while count < 20:
        count += 1
        url = 'URL TO SCRAPE' + str(count) #add the URL you'd like to scrape
        response = requests.get(url)
        text = response.text
        links = re.findall('https://leg.colorado.gov/sites/default/files/documents/.*pdf',text)

        download_dir = "NAME DOWNLOAD FOLDER" #add the foldername to which you would like to download. this creates a new folder.
        os.makedirs(download_dir, exist_ok=True)

        for link in links:
            try:
                filename = filename = os.path.join(download_dir, os.path.basename(link))
                r = requests.get(link, stream=True)
                if r.status_code == 200:
                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192): # Download in chunks
                            f.write(chunk)
            except requests.exceptions.RequestException as e:
                 print(f"Error downloading {link}: {e}")
        
PDF()
