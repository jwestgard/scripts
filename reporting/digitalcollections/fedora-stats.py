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
        self.type = mydict.get('doType', "undefined")
            
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
    
    # gather the full set of all columns
    fieldnames = set([])
    for row in data:
        fieldnames.update(list(row.keys()))
        
    # make sure the numeric and year columns appear leftmost
    fn_sorted = ['n', 'year']
    fn_sorted.extend([f for f in fieldnames if f not in fn_sorted])
        
    # write out all the rows of data to the output file
    with open(outputfile, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fn_sorted)
        writer.writeheader()
        writer.writerows(data)


# report generator
def year_report(assets, year, n):
    type_counts = {'year': year, 'n': n}
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
    
    
# generate stats for period between two dates
def range_report(assets, begindate, enddate):
    type_counts = {}
    for asset in assets:
        if asset.date.replace(tzinfo=None) > enddate:
            pass
        elif asset.date.replace(tzinfo=None) < begindate:
            pass
        else:
            t = asset.type
            print(asset.id, asset.date)
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
    
    report = []
    for n, year in enumerate(range(2005, 2017)):
        report.append(year_report(assets, year, n+1))
    
    write_report(sys.argv[2], report)
    
    fy15 = range_report(assets, datetime(2014, 7, 1), datetime(2015, 6, 30))
    print(fy15)


if __name__ == '__main__':
    main()
