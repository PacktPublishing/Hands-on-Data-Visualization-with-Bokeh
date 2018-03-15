#Preparing all the plots needed for this chapter

#Import the required packages

import pandas as pd

#Read in the data

df = pd.read_csv('all_stocks_5yr.csv')

#Convert the date column into datetime data type

df['date'] = pd.to_datetime(df['date'])

#Filter the data for Apple stocks only

df_apple = df[df['Name'] == 'AAL']

#Import the required packages

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource


#Create the ColumnDataSource object

data = ColumnDataSource(data = {
    'x' : df_apple['high'],
    'y' : df_apple['low'],
    'x1': df_apple['open'],
    'y1': df_apple['close'],
    'x2': df_apple['date'],
    'y2': df_apple['volume'],
    
    
})


#Create the first scatter plot

plot1 = figure()

plot1.cross(x = 'x', y = 'y', source = data, color = 'red', size = 10, alpha = 0.8)

#Create the second scatter plot

plot2 = figure()

plot2.circle(x = 'x1', y = 'y1', source = data, color = 'green', size = 10, alpha = 0.3)

#Create the third scatter plot

plot3 = figure(x_axis_type = 'datetime', x_axis_label = 'date', y_axis_label = 'Volume Traded')

plot3.line(x = 'x2', y = 'y2', source = data, color = 'red')

plot3.circle(x = 'x2', y = 'y2', source = data, fill_color = 'white', size = 3)



#Output the 3 plots

#Output the plot1

output_file('first_plot.html')

show(plot1)


#Output the plot2

output_file('second_plot.html')

show(plot2)


#Output the plot3

output_file('third_plot.html')

show(plot3)


#Creating multiple plots along the same row

#Import the required packages

from bokeh.layouts import row
from bokeh.io import output_file, show

#Group the 3 plots into a 'row' layout

row_layout = row(plot1,plot2,plot3)

#Output the plot

output_file('horizontal.html')

show(row_layout)


#Creating multiple plots along the same column

#Import the required packages

from bokeh.layouts import column
from bokeh.io import output_file, show

#Group the 2 plots into a 'column' layout

col_layout = column(plot1,plot2)

#Output the plot

output_file('vertical.html')

show(col_layout)



#Creating multiple plots along a row and column

#Import the required packages

from bokeh.layouts import column, row
from bokeh.io import output_file, show

#Construct the nested layout

nested_layout = column(row(plot1,plot2), plot3)

#Output the plot

output_file('nested.html')

show(nested_layout)



#Creating multiple plots on a tabbed layout

#Import the required packages

from bokeh.models.widgets import Tabs, Panel
from bokeh.io import output_file, show
from bokeh.layouts import column, row

#Create the two panels 

tab1 = Panel(child = plot1, title = 'Tab One')

tab2 = Panel(child = column(plot2,plot3), title = 'Tab Two')

#Feed the tabs into a Tabs object

tabs_object = Tabs(tabs = [tab1, tab2])

#Output the plot

output_file('tab_layout.html')

show(tabs_object)



#Creating a grid layout


#Import required packages

from bokeh.io import output_file, show
from bokeh.layouts import gridplot

#Create the grid layout

grid_layout = gridplot([plot1, plot2], [plot3, None])

#Output the plot

output_file('grid.html')

show(grid_layout)


#Linking multiple plots along the y axis

#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import row

#Creating equal y axis ranges

plot3.y_range = plot1.y_range

#Create the row layout

row_layout = row(plot3, plot1)

#Output the plot

output_file('grid.html')

show(row_layout)



#Linking multiple plots along the x axis

#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import row

#Creating equal x-axis ranges

plot2.x_range = plot1.x_range

#Create the row layout

row_layout = row(plot2, plot1)

#Output the plot

output_file('row.html')

show(row_layout)



