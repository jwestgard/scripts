#!/usr/bin/env python3
# -*- coding: utf8 -*-

import csv
from datetime import datetime, date
from dateutil.parser import *
import time
import json
import sys


# fedora object class
class fedora_object(object):

    def __init__(self, mydict):
        self.id = mydict['pid']
        self.date = parse(mydict['objcreatedate'])
        try:
            self.type = mydict['doType']
        except KeyError:
            self.type = 'undefined'
            
    def year(self):
        return self.date.year


# find assets between two dates
def assets_in_range(set, begin, end):
    return len([i for i in set if i < end and i > begin])


# read data from json file
def read_data(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
        result = data['response']['docs']
    return result
    
    
# write report to csv
def write_report(outputfile, data):
    for row in data:
        print(row, data[row])
    fieldnames = [key for row in data for key in row]
    print(fieldnames)
    with open(outputfile, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(data)


# report generator
def year_report(assets, year):
    type_counts = {}
    for asset in assets:
        if asset.year() != year:
            pass
        else:
            t = asset.type
            if t in type_counts:
                type_counts[t] += 1
            else:
                type_counts[t] = 1
                
    return type_counts
    

# main loop
def main():

    # read data
    rawdata = read_data(sys.argv[1])
    
    # create list of objects
    assets = [fedora_object(i) for i in rawdata]
    
    report = {}
    for year in range(2005, 2017):
        report[year] = year_report(assets, year)
        
    print(len(report))
    
    write_report(sys.argv[2], report)



if __name__ == '__main__':
    main()
