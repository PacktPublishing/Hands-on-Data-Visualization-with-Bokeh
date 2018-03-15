#Creating line plots using NumPy arrays

#Import required packages

import numpy as np
import random
from bokeh.io import output_file, show
from bokeh.plotting import figure

#Creating an array for the points along the x and y axes

array_x =np.array([1,2,3,4,5,6])

array_y = np.array([5,6,7,8,9,10])

#Creating a line plot

plot = figure()

plot.line(array_x, array_y)

#Output the plot

output_file('numpy_line.html')

show(plot)



#Creating scatter plots using NumPy arrays


#Import required packages

import numpy as np
import random
from bokeh.io import output_file, show
from bokeh.plotting import figure

#Creating arrays for two different categories of points

x_red = np.array([1,2,3,4,5])
y_red = np.array([5,6,7,8,9])

x_blue = np.array([10,11,12,13])
y_blue = np.array([14,15,16,17])

#Creating the categorical scatter plot 

plot = figure()

plot.circle(x_red, y_red, size = 9, color = 'red', alpha = 0.8)
plot.circle(x_blue, y_blue, size = 9, color = 'blue', alpha = 0.8)

#Output the plot 

output_file('numpy_scatter.html')

show(plot)



#Creating a time series plot using a Pandas DataFrame


#Importing the required packages

import pandas as pd

#Read in the data

df = pd.read_csv('all_stocks_5yr.csv')

#Filtering for apple stocks

df_apple = df[df['Name'] == 'AAL']


#Import the required packages

from bokeh.io import output_file, show
from bokeh.plotting import figure

#Create the time series plot

plot = figure(x_axis_type = 'datetime', x_axis_label = 'date', y_axis_label = 'High Prices')

plot.line(x = df_apple['date'], y = df_apple['high'])

#Output the plot

output_file('pandas_time.html')

show(plot)


#Creating scatter plots using a Pandas DataFrame

#Import the required packages

from bokeh.io import output_file, show
from bokeh.plotting import figure

#Create the scatter plot

plot = figure()

plot.circle(x = df_apple['high'], y = df_apple['low'], color = 'red', size = 10, alpha = 0.8)

plot.diamond(x = df_apple['open'], y = df_apple['close'], color = 'green', size = 10, alpha = 0.8)


#Output the plot

output_file('pandas_scatter.html')

show(plot)



#Creating a time series plot using the ColumnDataSouce

#Import the required packages

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource

#Create the ColumnDataSource object

data = ColumnDataSource(df_apple)

#Create the time series plot

plot = figure(x_axis_type = 'datetime', x_axis_label = 'date', y_axis_label = 'High Prices')

plot.line(x = 'date', y = 'high', source = data, color = 'red')

plot.circle(x = 'date', y = 'high', source = data, fill_color = 'white', size = 3)

#Output the plot

output_file('CDS_time.html')

show(plot)


#Creating a scatter plot using the ColumnDataSource

#Import the required packages

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource


#Create the ColumnDataSource object

data = ColumnDataSource(data = {
    'x' : df1['high'],
    'y' : df1['low'],
    'x1': df1['open'],
    'x2': df1['close'],
    
})


#Create the scatter plot

plot = figure()

plot.cross(x = 'x', y = 'y', source = data, color = 'red', size = 10, alpha = 0.8)

plot.circle(x = 'x1', y = 'x2', source = data, color = 'green', size = 10, alpha = 0.3)

#Output the plot

output_file('CDS_scatter.html')

show(plot)
