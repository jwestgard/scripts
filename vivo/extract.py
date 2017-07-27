#!/usr/bin/env python3

import requests
import json
import sys
from bs4 import BeautifulSoup

MAIN_DIR =   "https://www.lib.umd.edu/directory/specialists/librarian"
BY_COLLEGE = "https://www.lib.umd.edu/directory/specialists/college-or-school"
OUTFILE =    sys.argv[1]


def print_header():
    '''Print a header to stdout'''
    title = "| EXTRACT DATA |"
    bar = "=" * len(title)
    print("\n".join([" ", bar, title, bar]))


def fetch_webpage(url):
    '''Grab a webpage and return the response body'''
    print("Grabbing page {0} ...".format(url))
    response = requests.get(url)
    print("Server response = {0}".format(response.status_code))
    if response.status_code == 200:
        return response.text


def create_college_dir(college_soup):
    '''Generate a directory of librarians by associated college'''
    main = college_soup.find('div', {'class': 'content-container'})
    liasons = main.findAll('div', {'class': 'directory-search-record'})
    result = {}
    for liason in liasons:
        name = liason.find('a', {'class': 'staff-links'})
        if name is not None:
            parent = liason.find_parent('div').find_parent('div')
            college = parent.find_previous_sibling('h3').text
            result[name.text] = college
    return result


def extract_data(entry, college_dir):
    '''Extract the directory data from the HTML snippet'''
    link    = entry.find('a', {'class': 'staff-links'})
    name    = link.text
    first   = link.text.split(',')[1].strip()
    last    = link.text.split(',')[0].strip()
    paras   = entry.findChildren('p')
    title   = paras[1].text
    dept    = paras[2].text,
    phone   = paras[3].find('a').text.strip()
    email   = paras[4].find('a').text.strip()
    address = paras[5].text
    college = college_dir.get(name)
   
    if link['href'].startswith('/directory/staff/'):
        directory_id = link['href'][17:]
    else:
        directory_id = link['href']

    subject_list = entry.findChildren(
                    'li', {'class': 'research-subject'}
                    )
    return {'uid':       directory_id,
            'name':      name,
            'lastname':  last,
            'firstname': first,
            'subjects':  [" ".join(i.contents) for i in subject_list],
            'title':     title,
            'phone':     phone,
            'email':     email,
            'address':   address,
            'college':   college
            }                          


def main():
    '''Pull HTML, parse, and extract entry information'''
    
    # set up
    print_header()
    main_dir = fetch_webpage(MAIN_DIR)
    by_college = fetch_webpage(BY_COLLEGE)
    
    # parse the responses to get directory entries
    soup = BeautifulSoup(main_dir, 'html.parser')
    college_soup = BeautifulSoup(by_college, 'html.parser')
    
    # create dict by college
    college_dir = create_college_dir(college_soup)
    dir_entries = soup.find_all("div",
                                class_="directory-search-specialist-record"
                                )
    print("Found {0} directory entry divs.".format(len(dir_entries)))
    
    # iterate over the directory and extract data for each entry
    results = [extract_data(entry, college_dir) for entry in dir_entries]
    
    # print the result
    pretty_dump = json.dumps(
        results, sort_keys=True, indent=4, separators=(',', ': ')
        )
    print(pretty_dump)
    
    # write to a json file
    with open(OUTFILE, 'w') as outfile:
        outfile.write(pretty_dump)


if __name__ == "__main__":
    main()
