from script import fetch_all_stock_data 

#Ask the user to enter the stock symbol for the company they want data for.
#and return data for said company
def getSymbol():
    while True:
        stock_symbol = input("\nenter the stock symbol for the company:  ")

        #gets data from API
        data = fetch_all_stock_data(stock_symbol)
            #print(type(data))
    

        #check for error
        if data.get('Error Message') is not None:
            print("please enter a viable symbol")
        else:
            False
            return data



# Define a function that takes the time series number as an argument and returns the corresponding function name
def get_time_series_function(time_series):
    # Use a dictionary to map the numbers to the function names
    time_series_dict = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }
    # Return the function name if the number is valid, otherwise return None
    return time_series_dict.get(time_series, None)

def main():
    print("Stock Data Visualizer")
    print("------------------------")
    getSymbol()

   
    
    print("Enter the time series function:")
    print("1. TIME_SERIES_INTRADAY")
    print("2. TIME_SERIES_DAILY")
    print("3. TIME_SERIES_WEEKLY")
    print("4. TIME_SERIES_MONTHLY")
    time_series = input("Enter the number: ")



main()

#Ask the user for the chart type they would like.
#Ask the user for the time series function they want the api to use.
#Ask the user for the beginning date in YYYY-MM-DD format.
#Ask the user for the end date in YYYY-MM-DD format.
#The end date should not be before the begin date
#Generate a graph and open in the user’s default browser.