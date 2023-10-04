
def print_table(data, fields, formatter):
    formatter.headings(fields)
    for r in data:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


        
########
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))




########
#(c)
class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print('<th>%s</th>' % h, end=' ')
        print('</tr>')

    
    def row(self, rowdata):
        
        
        print('<tr>', end=' ')
        for r in rowdata:
            print('<th>%s</th>' % r, end=' ')
        print('</tr>')

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
        
#(e)
def create_formatter(type):
    if type == 'html':
        formatter_cls =  HTMLTableFormatter
    elif type == 'csv':
        formatter_cls = CSVTableFormatter
    elif type == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % type)
    return formatter_cls()
