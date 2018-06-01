#Single slider application


#Import the required packages

from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.io import curdoc

#Create a slider widget

slider_widget = Slider(start = 0, end = 100, step = 10, title = 'Single Slider')

#Create a layout for the widget

slider_layout = widgetbox(slider_widget)

#Add the slider widget to the application

curdoc().add_root(slider_layout)

#Launching application from terminal/powerhsell

bokeh serve --show bokeh.py

--------------------------------------------------------------------------------------------------

#Multi-Slider application

#Import the required packages

from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.io import curdoc

#Create multiple slider widgets

slider_widget1 = Slider(start = 0, end = 100, step = 10, title = 'Slider 1')

slider_widget2 = Slider(start = 0, end = 50, step = 5, title = 'Slider 2')

slider_widget3 = Slider(start = 50, end = 100, step = 5, title = 'Slider 3')

#Create a layout for the widget

slider_layout = widgetbox(slider_widget1, slider_widget2, slider_widget3)

#Add the slider widget to the application

curdoc().add_root(slider_layout)

#Launching the application

bokeh serve --show bokeh.py

-----------------------------------------------------------------------------------------------------

#Slider application with a scatter plot


#Import the required packages

from bokeh.models import Slider, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
from numpy.random import random

#Create data for the plot

initial_points = 500

data_points = ColumnDataSource(data = {'x': random(initial_points), 'y': random(initial_points)})

#Create the plot

plot = figure(title = "Random scatter plot generator")

plot.diamond(x = 'x', y = 'y', source = data_points, color = 'red')

#Create the slider widget

slider_widget = Slider(start = 0, end = 10000, step = 10, value = initial_points, title = 'Slide right to increase number of points')

#Define the callback function

def callback(attr, old, new):
    
    points = slider_widget.value
    data_points.data = {'x': random(points), 'y': random(points)}
    
slider_widget.on_change('value', callback)

#Create a layout for the application

layout = row(slider_widget, plot)

#Add the layout to the application

curdoc().add_root(layout)

#Launching the application

bokeh serve --show bokeh.py

----------------------------------------------------------------------------------------------------

#Slider application with line plot

#Import the required packages

from bokeh.models import Slider, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
from numpy.random import random

#Define the points that create the line plot

x = [1,2,3,4,5,6,7,8,9]
y = [2,3,4,5,6,7,8,9,10]

#Create the data source

data_points = ColumnDataSource(data = {'x': x, 'y': y})

#Create the line plot

plot = figure(title = 'Random Line plot generator')

plot.line('x', 'y', source = data_points, color = 'red')

#Create the slider widget 

slider_widget = Slider(start = 0, end = 100, step = 1, value = 10)

#Define the callback function

def callback(attr, old, new):
    
    points = slider_widget.value
    data_points.data = {'x': random(points), 'y': random(points)}
    
slider_widget.on_change('value', callback)

#Create the layout

layout = row(slider_widget, plot)

#Add the layout to the application

curdoc().add_root(layout)

#Launching the application

bokeh serve --show bokeh.py

-------------------------------------------------------------------------------------------------------

#Application with the select widget

#Import the required packages

from bokeh.models import Select, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
from numpy.random import random, normal

#Create data for the plot

initial_points = 500

data_points = ColumnDataSource(data = {'x': random(initial_points), 'y': random(initial_points)})

#Create the plot

plot = figure(title = "Scatter plot distribution selector")

plot.diamond(x = 'x', y = 'y', source = data_points, color = 'red')

#Create the select widget

select_widget = Select(options = ['uniform distribution', 'normal distribution'], value = 'uniform distribution', title = 'Select the distribution of your choice')

#Define the callback function

def callback(attr, old, new):
    
    if select_widget.value == 'uniform distribution':
        function = random
    else:
        function = normal
    data_points.data = {'x': function(size = initial_points), 'y': function(size = initial_points)}

select_widget.on_change('value', callback)

#Create a layout for the application

layout = row(select_widget, plot)

#Add the layout to the application

curdoc().add_root(layout)

#Launching the application

bokeh serve --show bokeh.py

----------------------------------------------------------------------------------------------------------
#Creating an application with the button widget

#Import the required packages

from bokeh.models import Button, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
from numpy.random import random, normal
import numpy as np

#Create data for the plot

initial_points = 500

data_points = ColumnDataSource(data = {'x': random(initial_points), 'y': random(initial_points)})

#Create the plot

plot = figure(title = "Data change application")

plot.diamond(x = 'x', y = 'y', source = data_points, color = 'red')

#Create the button widget

button_widget = Button(label = 'Change Data')

#Define the callback function

def callback():
    
    #New y values 
    
    y = np.cos(initial_points) + random(initial_points)
    
    data_points.data = {'x': random(initial_points), 'y': y}
    
button_widget.on_click(callback)
 
#Create a layout for the application

layout = row(button_widget, plot)

#Add the layout to the application

curdoc().add_root(layout)

#Launching the application

bokeh serve --show bokeh.py

---------------------------------------------------------------------------------------------------------

#Application to select different columns

#Importing the required packages

import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.io import curdoc
from bokeh.layouts import row

#Read in the data

df = pd.read_csv('all_stocks_5yr.csv')

#Filtering for apple stocks

df_apple = df[df['Name'] == 'AAL']

#Create the ColumnDataSource object

data = ColumnDataSource(data = {
    'x' : df_apple['high'],
    'y' : df_apple['low'],
    'x1': df_apple['volume']
    
})

#Creating the scatter plot 

plot = figure(title = 'Attribute selector application')

plot.diamond('x', 'y', source = data, color = 'red')

#Creating the select widget

select_widget = Select(options = ['low', 'volume'], value = 'low', title = 'Select a new y axis attribute')

#Define the callback function

def callback(attr, old, new):
    
    if new == 'low':
        
        data.data = {'x' : df_apple['high'], 'y': df_apple['low']}
        
    else:
        
        data.data = {'x' : df_apple['high'], 'y': df_apple['volume']}
        
select_widget.on_change('value', callback)


#Add the layout to the application

layout = row(select_widget, plot)

curdoc().add_root(layout)

#Launching the application

bokeh serve --show bokeh.py

-----------------------------------------------------------------------------------------------------


