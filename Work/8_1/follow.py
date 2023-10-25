# follow.py
import os
import time

filename = 'stocklog.csv';
def follow(filename):
    print(filename)
    fil = open(filename)
    fil.seek(0, os.SEEK_END)
    while True:
             line = fil.readline()
             if line == '':
                 time.sleep(0.1)    # Sleep briefly to avoid busy wait
                 continue
             yield line




for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))

""" while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change)) """

