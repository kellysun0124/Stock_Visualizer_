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
def get_time_series_function():
    print("Enter the time series function:")
    print("1. TIME_SERIES_INTRADAY")
    print("2. TIME_SERIES_DAILY")
    print("3. TIME_SERIES_WEEKLY")
    print("4. TIME_SERIES_MONTHLY")
    time_series = input("Enter the number: ")

    time_series_dict = {
        "1": "TIME_SERIES_INTRADAY",
        "2": "TIME_SERIES_DAILY",
        "3": "TIME_SERIES_WEEKLY",
        "4": "TIME_SERIES_MONTHLY"
    }

    # Return the function name if the number is valid, otherwise return None
    return time_series_dict.get(time_series, None)

def getGraphType():
    print("Select graph type...")    

def main():
    print("Stock Data Visualizer")
    print("------------------------")
    getSymbol()

    time_series = get_time_series_function()
    if time_series is not None:
        print(f"Selected time series function: {time_series}")
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()