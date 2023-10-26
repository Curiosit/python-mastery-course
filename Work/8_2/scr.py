from follow import follow
import csv
lines = follow('stocklog.csv')
rows = csv.reader(lines)
for row in rows:
    print(row)