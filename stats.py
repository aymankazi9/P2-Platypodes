import requests
import lxml.html as lh
import sqlite3 as sl

url = 'https://www.worldometers.info/coronavirus/country/us/'  # URL
page = requests.get(url) # Request the data
doc = lh.fromstring(page.content) #convert the HTML data to string
tr_elements = doc.xpath('//tr')
col=[]  # empty list to append the collected records

for j in range(1,53): #len(tr_elements)): Iterating through data table, record by record (increase it to around 60 records)

    T=tr_elements[j] # Assigning each record to T (whole record)


    # now iterate through all columns in that particular record
    i=0 # column counter
    data_tup=() # empty tuple, for each record you create tuple appeading all columns to it.

    for t in T.iterchildren(): # iteration through the columns of the record - t will hold the actual column data not the column counter

        data= (t.text_content().replace(',','')).strip() # replacing commas(,) with nothing and Removing newline character (enter) and any blank space before and after the data

        if i < 13: # excluding last 2 columns (source & Projection)

            if j>0: # J is outer loop, and excluding the 0th record which is column headers from processing. But it will be added to record tuple without processing at the end of this "if" construct
                # for your project you can completely exclude the Header reacord as you dont need it.

                if i !=1 : # Do not convert the data to integer if the column number is 1 which is actually holds the state name which cannot be converted to number
                    try:
                        data= int(data) # convert the data to number
                    except: # if there is None or NULL you will get exception when you try to convert to number, that why you need exception block
                        print(data,'cannot be converted to Integer, row,col=',j,i)
                        data=0


            data_tup = data_tup+(data,) #add the column data to the Record tuple..
            i+=1 # increase the column counter

    # column iteration ends here..


    col.append (data_tup)

    con = sl.connect('platypodes.db')

try:
    with con:
        con.execute("""
            CREATE TABLE COVIDSTATS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                state_name TEXT,
                total_cases INTEGER,
                new_cases INTEGER,
                total_deaths INTEGER,
                new_deaths INTEGER,
                total_recovered INTEGER,
                active_cases INTEGER,
                case_mill INTEGER,
                death_mill INTEGER,
                total_tests INTEGER,
                test_mill INTEGER,
                population INTEGER
                );
        """)
except:
    print("The table already exists.")
with con:
    data = con.execute("DELETE FROM COVIDSTATS")

sql = 'INSERT INTO COVIDSTATS (id, state_name, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, case_mill, death_mill, total_tests, test_mill, population) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

with con:
    con.executemany(sql, col)

with con:
    data = con.execute("SELECT * FROM COVIDSTATS")
    for row in data:
        print(row)

