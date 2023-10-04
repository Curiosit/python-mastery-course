#(a)
import stock, read, tableformat
portfolio = read.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)



#(b)
import stock, read, tableformat
portfolio = read.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)