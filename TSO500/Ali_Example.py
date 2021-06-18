import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
First bit making a made up numpy array and changing it into a pandas dataframe
"""
# creating the Numpy array
array = np.array([[1, 1, 1], [2, 4, 8], [3, 9, 27],
                  [4, 16, 64], [5, 25, 125], [6, 36, 216],
                  [7, 49, 343]])

# creating a list of index names
index_values = ['first', 'second', 'third',
                'fourth', 'fifth', 'sixth', 'seventh']

# creating a list of column names
column_values = ['number', 'squares', 'cubes']

# creating the dataframe
df = pd.DataFrame(data=array,
                  index=index_values,
                  columns=column_values)

# displaying the dataframe
print(df)
"""
Actual graph code
"""
# Making a mask; another dataframe of a filtered subset of the data in df. In this case all rows with squares value over 25
array_mask = df[df['squares'] > 25]
print(array_mask)

# Create a first plot of number against squares using dots ("o") in blue
plt.plot(df['number'], df['squares'], "o", color='#17becf')

# Plot the mask over the top in red. This will "mask" over the relevent blue points. (Can be commented out and will just show blue)
plt.plot(array_mask['number'], array_mask['squares'], "o", color='#fc1703')

# Labels and show the plot.
plt.title('DNA quality metrics: Contamination P Values')
plt.xlabel('P values')
plt.show()