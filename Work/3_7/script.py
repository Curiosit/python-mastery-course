import stock, read, tableformat
portfolio = read.read_csv_as_instances('portfolio.csv', stock.Stock)
#class MyFormatter:
        #def headings(self,headers): pass
        #def row(self,rowdata): pass


#tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())

#(c)

import read
import stock
port = read.read_csv_as_instances('portfolio.csv', stock.Stock)