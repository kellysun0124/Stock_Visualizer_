from flask import Flask, render_template, request, url_for, flash, redirect, abort
import pandas

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'pass123'

#flash the secret key to secure sessions
app.config['SECRET KEY'] = 'pass123'

#get stock symbol from csv file
def get_symbol_list():
    symbol_list = []
    count = 0
    csvFile = pandas.read_csv('stocks.csv', usecols=['Symbol'])        
    list = csvFile['Symbol']
    for index in range(len(list)):
        symbol_list.append(list[index])
    #print(symbol_list)


# use the app.route() decorator to create a Flask view function called index()
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        #get title and content submitted by user
        stock = request.form['stock']
        chart_type = request.form['chart type']    
        time_series = request.form['time series']    
        start_date = request.form['start date']    
        end_date = request.form['end date']    

        #display error if not submitted
        #otherwise make a database connection and insert the post
        if not stock:
            flash('stock is required')
        elif not chart_type:
            flash('chart type is required')
        elif not time_series:
            flash('time series is required')
        elif not start_date:
            flash('start date is required')
        elif not end_date:
            flash('end date is required')
        else:
            symbol_list = symbol_list()
            insert_query = 'INSERT INTO posts (title, content) VALUES (?, ?)'
            conn.execute(insert_query, (title, content))
            conn.commit()
            conn.close()
            #redirect to index page when successfully submitted
            return redirect(url_for('index'))

    return render_template('index.html')
    
