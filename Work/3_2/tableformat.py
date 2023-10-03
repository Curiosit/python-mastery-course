
def print_table(data, fields):
    print(' '.join('%10s' % fieldname for fieldname in fields))
    print(('-'*10 + ' ')*len(fields))
    for dat in data:
           print(' '.join('%10s' % getattr(dat, fieldname) for fieldname in fields))    


########
