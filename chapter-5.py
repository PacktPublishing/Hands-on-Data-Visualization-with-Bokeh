#Setting up the data for chapter 

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




#Adding titles to plots


#Import the required packages

from bokeh.plotting import figure, show, output_file

#Create the plot with the title

plot3 = figure(title = "5 year time series distribution of volumn of Apple stocks traded", title_location = "above", 
               x_axis_type = 'datetime', x_axis_label = 'date', y_axis_label = 'Volume Traded')

#Create the time series plot

plot3.line(x = 'x2', y = 'y2', source = data, color = 'red')

plot3.circle(x = 'x2', y = 'y2', source = data, fill_color = 'white', size = 3)

#Output the plot

output_file('title.html')

show(plot3)




#Adding legends to plots

#Import the required packages

from bokeh.plotting import figure, show, output_file

#Create the two scatter plots

plot = figure()

#Create the legends

plot.cross(x = 'x', y = 'y', source = data, color = 'red', size = 10, alpha = 0.8, legend = "High Vs. Low")

plot.circle(x = 'x1', y = 'y1', source = data, color = 'green', size = 10, alpha = 0.3, legend = "Open Vs. Close")

#Output the plot

output_file('legend.html')

show(plot)



#Adding colormaps to plots

#Reading in the S&P 500 data

df = pd.read_csv('all_stocks_5yr.csv')

#Filtering for Google or USB

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Import the required packages

from bokeh.models import CategoricalColorMapper

#Store the data in the ColumnDataSource object

data = ColumnDataSource(df_multiple)

#Create the mapper 

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

#Plot the figure

plot = figure()

plot.circle('high', 'low', size = 8, source = data, color = {'field': 'Name', 'transform': category_map})

#Output the plot

output_file('category.html')

show(plot)



#Button widget

#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button

#Create the button

button = Button(label="Click me", button_type = "success")

#Output the button

output_file("button.html")

show(widgetbox(button))



#Checkbox widget


#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxGroup

#Create the checkbox

checkbox = CheckboxGroup(
        labels=["Category: 1", "Category: 2", "Category: 3"], active=[0, 1, 2])

#Output the checkbox

output_file("checkbox.html")

show(widgetbox(checkbox))


#Dropdown menu widget


#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown

#Create the menu

menu = [("Option 1", "item_1"), ("Option 2", "item_2")]

#Create the Dropdown

dropdown = Dropdown(label="Dropdown Menu", button_type="warning", menu=menu)

#Output the dropdown menu

output_file("dropdown.html")

show(widgetbox(dropdown))



#Radio button widget

#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import RadioGroup

#Create the radio button 

radio_button = RadioGroup(
        labels=["Option 1", "Option 2"], active=0)

#Output the radio button widget

output_file("radiobutton.html")

show(widgetbox(radio_button))


#Slider widget

#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Slider

#Create the slider widget

slider = Slider(start=0, end=50, value=0, step= 5, title="Simple Slider")

#Output the slider

output_file("slider.html")

show(widgetbox(slider))


#Text input widget

#Import the required packages

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import TextInput

#Create the text input widget

text_widget = TextInput(value="", title="Type your text here")

#Output the text input widget

output_file("text_input.html")

show(widgetbox(text_widget))



#Hover tooltip

#Import the required packages

from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.plotting import figure
import pandas as pd

#Read in the data and filter for Google and USB stocks

df = pd.read_csv('all_stocks_5yr.csv')

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Create the hover tooltip

hover_tool = HoverTool(tooltips = [
    ('Stock Ticker', '@Name'),
    ('High Price', '@high'),
    ('Low Price', '@low')
]) 

#Save the data in a ColumnDataSource object

data = ColumnDataSource(df_multiple)

#Create the categorical color mapper

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

#Create the plot with the hover tooltip

plot = figure(tools = [hover_tool])

plot.circle('high', 'low', size = 8, source = data, color = {'field': 'Name', 'transform': category_map})

#Output the plot

output_file('hover.html')

show(plot)




#Creating selections


#Import the required packages

from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.plotting import figure

#Read in the dataset and filter for Google and USB stocks

df = pd.read_csv('all_stocks_5yr.csv')

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Save the data into a ColumnDataSource object

data = ColumnDataSource(df_multiple)

#Create the categorical color mapper

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

#Create the plot with the selection tool 

plot = figure(tools = 'box_select')

plot.circle('high', 'low', size = 8, source = data, 
            color = {'field': 'Name', 'transform': category_map}, selection_color = 'green',
           nonselection_fill_alpha = 0.3, nonselection_fill_color = 'grey')

#Output the plot

output_file('selection.html')

show(plot)



#Styling the title

#Import the required packages

from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.plotting import figure

#Read in and filter the data for Google and USB stocks

df = pd.read_csv("all_stocks_5yr.csv")

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Store the data in a ColumnDataSource

data = ColumnDataSource(df_multiple)

#Create the categorical color mapper

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

#Create the plot and configure the title 

plot = figure(title = "High Vs. Low Prices (Google & USB)")

plot.title.text_color = "red"

plot.title.text_font = "times"

plot.title.text_font_style = "bold"

plot.circle('high', 'low', size = 8, source = data, 
            color = {'field': 'Name', 'transform': category_map})

#Output the plot

output_file('title.html')

show(plot)




#Styling the background



#Import the required packages

from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.plotting import figure

#Read in the data and filter for Google and USB stocks

df = pd.read_csv("all_stocks_5yr.csv")

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Save the data in a ColumnDataSource object

data = ColumnDataSource(df_multiple)

#Create the categorical color mapper

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

#Create the plot and configure the background

plot = figure(title = "High Vs. Low Prices (Google & USB)")

plot.background_fill_color = "yellow"
plot.background_fill_alpha = 0.3

plot.circle('high', 'low', size = 8, source = data, 
            color = {'field': 'Name', 'transform': category_map})

#Output the plot

output_file('title.html')

show(plot)



#Styling the outline of the plot



#Import the required packages

from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.plotting import figure

#Read in the data and filter for Google and USB stocks

df = pd.read_csv("all_stocks_5yr.csv")

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Save data into a ColumnDataSource object

data = ColumnDataSource(df_multiple)

#Create the color mapper

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

plot = figure(title = "High Vs. Low Prices (Google & USB)")

#Configure the outline of the plot

plot.outline_line_width = 8
plot.outline_line_alpha = 0.8
plot.outline_line_color = "black"

#Create and output the plot

plot.circle('high', 'low', size = 8, source = data, 
            color = {'field': 'Name', 'transform': category_map})

output_file('outline.html')

show(plot)



#Styling the labels


#Import the required packages

from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.plotting import figure

#Read in the data

df = pd.read_csv("all_stocks_5yr.csv")

df_multiple = df[(df['Name'] == 'GOOGL') | (df['Name'] == 'USB')]

#Save the data as a ColumnDataSource object

data = ColumnDataSource(df_multiple)

#Create a categorical color mapper

category_map = CategoricalColorMapper(
    factors = ['GOOGL', 'USB'], palette = ['blue', 'red'])

#Create the plot and configure the labels

plot = figure(title = "High Vs. Low Prices (Google & USB)")

plot.xaxis.axis_label = "High Prices"
plot.xaxis.axis_label_text_color = "green"

plot.yaxis.axis_label = "Low Prices"
plot.yaxis.axis_label_text_font_style = "bold"

plot.circle('high', 'low', size = 8, source = data, 
            color = {'field': 'Name', 'transform': category_map})

#Output the plot

output_file('title.html')

show(plot)








