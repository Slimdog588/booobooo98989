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
	
	# The returned data is a pandas DataFrame: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
	# RTFM
    
    if not data.empty :
		i = 0
		while i < 5:

			try:
				
				#money_list.append(data[data.Vol > 1000].index.get_level_values('Symbol'))
				print data[Symbol] 

			except Exception as e:
				print "ERROR: " + str(e)
			
			time.sleep(1)
			i += 1

new_file = open("output.csv", 'wb') #Fix: 1)make it write to .csv in rows 2) skipping lines?
writer = csv.writer(new_file)       #Should I have them written in the function above?

for item in money_list:
   writer.writerow(item)
