import csv
import sys
import collections
def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()      # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
    return records

class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)
    def __getitem__(self, ref):
        if isinstance(ref, int):
            return { 'route': self.routes[ref],
                     'date': self.dates[ref],
                     'daytype': self.daytypes[ref],
                     'rides': self.numrides[ref] }
        elif isinstance(ref, slice):
            sliced = RideData()
            for i in range(ref.start or 0, ref.stop or sys.maxsize, ref.step or 1):
                sliced.append({
                    'route': self.routes[i],
                    'date': self.dates[i],
                    'daytype': self.daytypes[i],
                    'rides': self.numrides[i] })
            return sliced
        else:
            return NotImplemented
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
    


rows = read_rides_as_columns('ctabus.csv')

r = rows[0:10]
