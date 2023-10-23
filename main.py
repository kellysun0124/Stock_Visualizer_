#get stock symbol...
def getSymbol():
    stock_symbol = input("enter the stock symbol for the company:  ")
    return stock_symbol



def main():
    print("Stock Data Visualizer")
    print("------------------------")
    getSymbol()



main()