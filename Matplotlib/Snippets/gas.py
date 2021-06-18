'''Introduction to data Visualtzation in Python with Matplotlib'''

'''The video in the wakelet (link below) provide a walk through of
of the Data vidualsation in python with MatPlotlib using gas'''

#Load the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read csv file
gas = pd.read_csv('../Data/gas_prices.csv')

#graph formatting
plt.figure(figsize=(8,5))

#labeling the graph
plt.title('Gas Prices over time (USD)',fontdict={'fontweight':'bold', 'fontsize':22})
plt.xticks(gas.Year[::2])
plt.xlabel('Year')
plt.ylabel("US Dollars")


#generate a line graph
plt.plot(gas.Year, gas.USA, label='United States', color='blue', linestyle='--')#optional label parameter, color, linestyle
plt.plot(gas.Year, gas. Canada, label='Canada', color='pink', linestyle='-.' )
plt.plot(gas.Year, gas['South Korea'], label='South Korea')#multiword notation #optional label parameter

#another way to plot many values
# countries_to_look_at =  ['Australia', "USA", 'Canada', 'South Korea']
# for country in gas:
#     # if country != "Year":
#     if country in countries_to_look_at:
#         plt.plot(gas.Year, gas[country], marker='.')


plt.legend()
plt.show()



print(gas)