#this script searches the Colorado Session Laws community
#hosted by the University of Colorado Law Library
#via Elsevier's Digital Commons

import requests
import json
import pandas as pd

#here are the base API url + auth token
url = 'https://content-out.bepress.com/v2/{{digital_commons_base_url}}/query?'
head = {'Authorization':'{{auth_token}}'} #contact Digital Commons support to get token

#decide on parameters
#comment out fields you are not searching on
year = {{year}} #change year if needed!
keys = {'fields':'title,author,publication_date,configured_field_t_session_type,configured_field_t_session_numdocument_type,configured_field_t_chapter,configured_field_t_start_page,url',
        'title': '{{title}}', #search by title exact match
        'author': '{{author}}', #search by author exact match
        'publication_date': f'{year}-01-01T08:00:00Z', #search by publication date
        'configured_field_t_session_type': '{{session_type}}', #search by session type
        'configured_field_t_session_num': '{{session_num}}', #search by session number
        'document_type': '{{document_type}}', #search by document type
        'configured_field_t_chapter': '{{chapter}}', #search by chapter
        'configured_field_t_start_page':'{{startpage}}',
        } 

def build_request():
    #build the API GET request
    response = requests.get(url,headers=head,params=keys)
    json1 = response.json()

    #get rid of the first "layer" of the json resp. (the "results" piece)
    #basically, this gets the the values of the
    #"results" key which is the first "layer" of the json
    json1_list = json1.get("results")

    #make json1_list into a dictionary by enumerating the DC records
    records = dict(enumerate(json1_list))

    #write results to a csv
    #create a new file OR append to existing
    df = pd.DataFrame.from_dict(records, orient='index')
    df.to_csv('temp.csv')
    #df.to_csv('temp.csv', mode='a', header=False)
    

build_request()
