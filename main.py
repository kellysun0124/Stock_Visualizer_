from script import fetch_all_stock_data 

#ask for stock symbol and return data
def getSymbol():
    stock_symbol = input("enter the stock symbol for the company:  ")
    #gets data from API
    return fetch_all_stock_data(stock_symbol)




def main():
    print("Stock Data Visualizer")
    print("------------------------")
    getSymbol()



main()