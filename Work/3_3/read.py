import csv
import sys
import collections

# (b)
def read_csv_as_dicts(filename, types):
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)     # Skip headers
        records = []
        for row in rows:
            record = {name:func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)
    return records

# (d)

def read_csv_as_columns(filename, types):
    columns = collections.defaultdict(list)
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for name, func, val in zip(headers, types, row):
                columns[name].append(func(val))
            
    return DataCollection(columns)


class DataCollection(collections.abc.Sequence):
    def __init__(self, columns):
        self.column_names = list(columns)
        self.column_data = list(columns.values())

    def __len__(self):
        return len(self.column_data[0])

    def __getitem__(self, index):
        return dict(zip(self.column_names,
                        (col[index] for col in self.column_data)))
        

# python -i read.py
# rows = read_csv_as_dicts('ctabus.csv', [str,str,str,int])
# rows = read_csv_as_columns('ctabus.csv', [str,str,str,int])