import stock, read
portfolio = read.read_csv_as_instances('portfolio.csv', stock.Stock)
from tableformat import TextTableFormatter, ColumnFormatMixin, print_table
class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
        formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)

from tableformat import TextTableFormatter, UpperHeadersMixin
class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
        pass




#####
#(c)
from tableformat import create_formatter
formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
print_table(portfolio, ['name','shares','price'], formatter)



formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name','shares','price'], formatter)