from main import *
import datetime

#i wasn't sure about the assignment so i did it in multiple ways for each
#class Unit_test():

# symbol: capitalized, 1-7 alpha characters
def symbol_test():
    #choose how you want to test from below..
    #1 can use this to test 
    # name = "GOOGL"
    
    #2 can use this to test too
    name = get_symbol()
            
    result = "symbol test = ok"
    #a.) can do this to check 
    if name != name.upper():
        result = "need to be capitalized"
    if len(name) < 1 or len(name) > 7:
        result = "need to be 1-7 alphabets"
    if not name.isalpha():
        result = "needs to be all alphabets"
    return result
    
    #b.) can do this to check too (uses getSymbo_data())
    # if name != name.upper():
    #     #but it doesn't need to be capitalized... anyways 
    #     print("need to be capitalized")
    # if len(name) < 1 or len(name) > 7:
    #     print("need to be 1-7 alphabets")
    # if name != name.isalpha():
    #     print("needs to be all alphabets")

    # symbol_data = getSymbol_data(name)
    # if symbol_data.get('Meta Data'):
    #     result = "symbol test = ok"
    #     return result


# time series: 1 numeric character, 1 - 4
def time_series_test():
     #choose how you want to test from below..
    # 1 test
    #user = '1'

    # 2 test
    user = get_time_series_function()
    
    choice = ['1','2','3','4']

    #a.) can do this to check
    if user in choice:
        result = "time_series test = ok"
    else:
        result = "time_series test = fail"
    return result

    

# start date: date type YYYY-MM-DD
# end date: date type YYYY-MM-DD
def start_end_dates_test():
    start_date, end_date = get_dates()
    result = "date test = ok"
    try:
        datetime.date.fromisoformat(start_date)
        datetime.date.fromisoformat(end_date)
    except ValueError:
        result = "date test = fail, enter date in YYYY-MM-DD format"

    return result
    




#print(symbol_test())
#print(time_series_test())
print(start_end_dates_test())