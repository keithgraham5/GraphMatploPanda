''' Visulsing Data in python using plt.scatter()

change the marker size
change the maker shape
Change the maker transparency
Change the marker color

Mask the data using Numpy Arrays


Author: Real Python

Packages:
matplotlib - comprehensive plotting library for creating static, animated and interactive visualizations in python
pandas - library offering data structures for data analysis and manipulation
numpy - library adding support for large, multi-dimensional arrays and matrices

Keywords: plt.scatter(x=x_axes, y=y_axes, s=size_of_marker, marker='marker_shape', c=color_of_marker, alpha=transparency)


Golden Snippet:

References:
https://realpython.com/visualizing-python-plt-scatter/
'''


# #Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''CREATING SCATTER PLOTS'''
price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales_per_day = [34, 62, 49, 22, 13, 19]

plt.plot(price, sales_per_day, marker="o")
plt.show()

'''CUSTOMIZING MARKERS IN SCATTER PLOTS, MARKER COLOR, MARKER SHAPE, MARKER TRANSPARENCY, ADD PLAN TEXT'''
low = (0,1,0)#RBG color selection
medium = (1,1,0)
high = (1,0,0)

price_orange = np.asarray([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])#Convert the input into an array
sales_per_day_orange = np.asarray([34, 62, 49, 22, 13, 19])
profit_margin_orange = np.asarray([20, 35, 40, 20, 27.5, 15])
sugar_content_orange = [low, high, medium, medium, high, low]

price_cereal = np.asarray([1.50, 2.50, 1.15, 1.95])
sales_per_day_cereal = np.asarray([67, 34, 36, 12])
profit_margin_cereal = np.asarray([20, 42.5, 33.3, 18])
sugar_content_cereal = [low, high, medium, low]

plt.scatter(
    x=price_orange, # x_axes
    y=sales_per_day_orange,# y_axes
    s=profit_margin_orange * 10, # Marker Size
    c=sugar_content_orange,# Marker colour
    marker='*', # Marker Shape
    alpha=0.5 # Marker Tranparency
)
plt.scatter(
    x=price_cereal,
    y=sales_per_day_cereal,
    s=profit_margin_cereal * 10,
    c=sugar_content_cereal,
    marker='d',
    alpha=0.5
)

plt.title("Sales vs Prices for Orange Drinks and Cereal Bars")
plt.legend(["Orange Drinks", "Cereal Bars"])
plt.xlabel("Price (Currency Unit)")
plt.ylabel("Average weekly sales")
plt.text(
    3.2,
    55,
    "Size of marker = profit margin\n" "Color of marker = sugar content",
)

plt.show()

