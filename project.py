from pandas_datareader.data import Options
import pandas as pd
from pandas import DataFrame
import datetime
import csv
import time
import sys

tickers = pd.read_csv('nxxx.csv', index_col=[0]) #List of Nyse symbols, Add Nasdaq
money_list = [] #List from which we send option symbols to a .csv file

for i in tickers.index:
    option = Options(i,'yahoo')
    data = option.get_all_data()

    if len(data[data.Vol].all ) > 0:

        if (data[data.Vol > 1000].all): #sys.getsizeof(data[data.Vol > 1000].all) != 0:

            x = 3
            while x < 1:

                try:
                    money_list.append(data[data.Vol > 1000].index.get_level_values('Symbol'))
                    print data[Symbol] #This don't work
                    time.sleep(1)
                    x += 1

                except: # RemoteDataError:
                    time.sleep(1)
                    x += 1
                    continue
        else:
            pass

    else:
        pass

new_file = open("output.csv", 'wb') #Fix: 1)make it write to .csv in rows 2) skipping lines?
writer = csv.writer(new_file)       #Should I have them written in the function above?

for item in money_list:
   writer.writerow(item)