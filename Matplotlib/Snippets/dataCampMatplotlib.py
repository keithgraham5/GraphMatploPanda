'''Matplotlib Tutorial:Python Plotting '''

'''This matplotlib tutorial takes you through the basics python data visulization:
 the anatomy of a plot, pyplot and pylab, and much more '''


'''
Author: Karlijn Willems 

version: 1 

Pacakges included:
Matplotlib 

Keywords: add_subplot(); add_axes(); plt.figure(); plot(); show(); 

Stand out: 
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20, 10))

References: 
https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

'''
#importing libraries
import matplotlib.pyplot as plt
import numpy as np

'''Prepare the data'''
# x = np.linspace(0, 10 ,100)
#
# #plot the data
# plt.plot(x ,x, label='linear')
#
# #Add a legend
# plt.legend()
#
# #show the plot
# plt.show()

#The figure
'''The figure is the over all window or page that everythin is drawn on. You can create multiple independent figures 
or a figure can have several things in it. Both Pieces of code below produce the same graph the second piece of code 
is cleaner. However if you have multiple axes its better to make use of the first chunk to make use of Axes object ax'''
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
# ax.scatter ([0.3, 3.8, 1.2, 2.5], [11, 25,9,26], color='darkgreen', marker='^')
# ax.set_xlim(0.5, 4.5)
# plt.show()
#
# plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
# plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
# plt.xlim(0.5, 4.5)
# plt.show()

'''create your plot. The purpose of the of using plt.figure() is to create a figure object. The whole figure is 
regaurded as the figure object. It is necessary to explicityly use plt.figure() when we want to tweak the size of the 
figure and when we want ot add multiple Axes objeccts ina single figure '''
#Initialize a Figure
# fig = plt.figure()#intiate the figure object by calling fig = plt.figure()
#
# #add Axes to the figure ([left, bottom, width, height])
# fig.add_axes([0,0,1,1])
#
# plt.show()

# #create a figure
# fig = plt.figure()
# #set up Axes
# ax = fig.add_subplot(221)#number of rows (1), number of columns (1), and the plot number (1) make one suplot
# #Set up the data
# ax.scatter(np.linspace(0,1,5), np.linspace(0,5,5))
#
# plt.show()

'''How to change the size of figures, alternative method to intitalsing multiple graphs on the same figure  '''

#Initialze the plot
# fig = plt.figure(figsize=(20,10))#width, Height
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)

# # or the code can be written like so
# fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20, 10))
#
# #Plot the data
# ax1.bar([1,2,3], [3,4,5])
# ax2.barh([0.5, 1, 2.5],[0,1,2])
#
# plt.show()


'''Plotting Routines to make graph look awesome'''
# ax.bar()         |  vertical rectangle
# ax.barh()        |  Horixontal rectangles
# ax.axhline()     |  Horizontal line across axes
# ax.vline()       |  veritcal line across axes
# ax.fill()        |  filled polygons
# ax.fill_between()|  Fill between y-values and 0
# ax.stackplot()   |  Stack plot

fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,10))

ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(2,3)

plt.show()

#Vector Field

# ax.arrow()	Arrow
# ax.quiver()	2D field of arrows
# ax.streamplot()	2D vector fields
# ax.hist()	Histogram
# ax.boxplot()	Boxplot
# ax.violinplot()	Violinplot

# ax.pcolor()	Pseudocolor plot
# ax.pcolormesh()	Pseudocolor plot
# ax.contour()	Contour plot
# ax.contourf()	Filled contour plot
# ax.clabel()	Labeled contour plot