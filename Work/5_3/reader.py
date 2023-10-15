# reader.py

import csv
from typing import List




def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        return csv_as_dicts(file, types)
    

def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        
        records = csv_as_instances(file,cls)
    return records



def csv_as_dicts(lines, types, *, headers=None):
    return convert_csv(lines, 
                       lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })

def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines,
                       lambda headers, row: cls.from_row(row))


def convert_csv(lines, conversion, *, headers=None):
    '''
    Read CSV data into a list based on the conversion function
    '''  
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    records = list(map(lambda row: conversion(headers, row), rows))
    """ for row in rows:
        record = conversion(headers, row)
        records.append(record) """
    return records


def make_dict(headers, row):
        return dict(zip(headers, row))

lines = ''
convert_csv(lines, make_dict)