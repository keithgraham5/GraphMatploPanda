'''Data visulation Tutorial from Codeacademy

The process of data visulatizationo involves three main steps:
Formattting the data
Vislulsing the data
Styling the visualzation

keywords:

references
https://www.codecademy.com/paths/visualize-data-with-python/tracks/introduction-to-python-dvp/modules/introduction-to-data-visualization/lessons/why-data-visualization/exercises/data-discover
global_population.csv
Netflix_Stock_Prices.csv
'''

#import libraires
from matplotlib import pyplot as plt
import pandas as pd
import csv

# csvfile = list(csv.reader(open('Netflix_Stock_Prices.csv')))
# # print(csvfile)
#
# opening1 = []
# closed1 = []

# for row in csvfile:
#     opening1.append(row.loc[:,'Open'])
#     closed1.append(row[6])
#
# print(opening1)

#how to read a specfici column from csv file in python
col_list = ["Date",'Open','High','Low','Close','Adj Close','Volume']

csv_File = pd.read_csv('../Data/Netflix_Stock_Prices.csv', usecols=col_list)
open = list(csv_File['Open'])
closed = list(csv_File['Close'])
business_days= range(252)
print(open)
print(closed)


plt.plot(business_days, open)
plt.plot(business_days, closed)
plt.xlabel("Stock Exchange Days for Past Year")
plt.ylabel("Price")

plt.title("Netflix Stock Prices for 2017")
legend_labels = ["Opening Price", "Closing Price"]
plt.legend(legend_labels, loc=8)

ax = plt.subplot()
ax.set_xticks([0,50,100,150,200,250])
month_names = ["Feb 2017", "Apr 2017", "Jun 2017", "Aug 2018","Oct 2018", "Dec 2017"]
ax.set_xticklabels(month_names)


plt.show()

##Formatting
'''The first step in the data visualzation process is cleaning and prepping the data. This step is 
different depending on the data format or the file your are visualizing'''

'''using global_population.csv'''
#read .csv file
# df = pd.read_csv('global_population.csv')
# print(df)

