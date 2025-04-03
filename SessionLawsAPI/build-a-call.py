#  ALL RIGHTS RESERVED

#this script gets user input and then builds a GET request for the Colorado Session Laws community
#hosted by Elsevier's Digital Commons for the University of Colorado Law School

import requests
import json
import pandas as pd

#headers for api call
head = {'Authorization':'{{auth_token}}'}

def make_call():
    
  #grab the inputs from the user
    url = 'https://content-out.bepress.com/v2/{{digital_commons_base_url}}/query?fields=title,author,publication_date,configured_field_t_session_type,configured_field_t_session_num,document_type,configured_field_t_chapter,configured_field_t_start_page,url'
    title = input("Title:")
    year = input("Year:")
    sess_type = input("Session Type:")
    sess_num = input("Session Number:")
    doc_type = input("Document Type:")
    chapter = input("Chapter:")
    page = input("First Page:")

    #build the query/url
    if title != '':
        url = url + '&title=' + title
        
    if year != '':
        url = url + '&publication_date=' + year + '-01-01T08:00:00Z'

    if sess_type != '':
        url = url + '&configured_field_t_session_type=' + sess_type

    if sess_num != '':
        url = url + '&configured_field_t_session_num=' + sess_num

    if doc_type != '':
        url = url + '&document_type=' + doc_type

    if chapter != '':
        url = url + '&configured_field_t_chapter=' + chapter

    if page != '':
        url = url + '&configured_field_t_start_page=' + page

    print(url)
    
    #make a GET request as a json resp
    response = response = requests.get(url,headers=head)
    json1 = response.json()

    #get rid of the first "layer" of the json resp. (the "results" piece)
    #basically, this gets the the values of the
    #"results" key which is the first "layer" of the json
    json1_list = json1.get("results")

    #make json1_list into a dictionary by enumerating the DC records
    records = dict(enumerate(json1_list))

    df = pd.DataFrame.from_dict(records, orient='index')
    df.to_csv('buildacall.csv')
    #df.to_csv('buildacall.csv', mode='a', header=False)


make_call()
