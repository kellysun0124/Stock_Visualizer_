from script import fetch_all_stock_data 

#Ask the user to enter the stock symbol for the company they want data for.
#and return data for said company
def getSymbol():
    stock_symbol = input("\nenter the stock symbol for the company:  ")
    #gets data from API
    return fetch_all_stock_data(stock_symbol)




def main():
    print("Stock Data Visualizer")
    print("------------------------")
    getSymbol()



main()

#Ask the user for the chart type they would like.
#Ask the user for the time series function they want the api to use.
#Ask the user for the beginning date in YYYY-MM-DD format.
#Ask the user for the end date in YYYY-MM-DD format.
#The end date should not be before the begin date
#Generate a graph and open in the user’s default browser.