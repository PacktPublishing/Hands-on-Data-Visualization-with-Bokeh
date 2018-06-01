#Creating a network

#Import the required packages

import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval

#Configure the number of nodes

total_nodes = 10
node_points = list(range(total_nodes))

#Create the network

plot = figure(x_range=(-1.1,1.1), y_range=(-1.1,1.1))

network = GraphRenderer()

#Customize your network

network.node_renderer.data_source.add(node_points, 'index')

network.node_renderer.glyph = Oval(height=0.2, width=0.3, fill_color='blue')

network.edge_renderer.data_source.data = dict(start=[1]*total_nodes, end=node_points)

#Render your network in 2-D space

node_circumference = [node*2*math.pi/10 for node in node_points]

x = [math.cos(circum) for circum in node_circumference]

y = [math.sin(circum) for circum in node_circumference]

network_layout = dict(zip(node_points, zip(x, y)))

#Output the network

network.layout_provider = StaticLayoutProvider(graph_layout=network_layout)

plot.renderers.append(network)

output_file('network.html')

show(plot)

---------------------------------------------------------------------------------------------------------

#Network with explicit paths

#Import the required packages

import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval

#Configure the number of nodes

total_nodes = 10
node_points = list(range(total_nodes))

#Create the network

plot = figure(x_range=(-1.1,1.1), y_range=(-1.1,1.1))

network = GraphRenderer()

#Customize your network

network.node_renderer.data_source.add(node_points, 'index')

network.node_renderer.glyph = Oval(height=0.2, width=0.3, fill_color='green')

network.edge_renderer.data_source.data = dict(start=[1]*total_nodes, end=node_points)

#Render your network in 2-D space

node_circumference = [node*2*math.pi/10 for node in node_points]

x = [math.cos(circum) for circum in node_circumference]

y = [math.sin(circum) for circum in node_circumference]

network_layout = dict(zip(node_points, zip(x, y)))

network.layout_provider = StaticLayoutProvider(graph_layout=network_layout)

#Function that outputs the quadratic path

values = [value/100. for value in range(100)]

def quad_path(start, end, control, values):
    return [(1-value)**2*start + 2*(1-value)*value*control + value**2*end for value in values]

#Initialize empty lists to store the x and y co-ordinates
x_point, y_point = [], []

#Store the starting and ending points

x_start, y_start = network_layout[0]

#Create the set of co-ordinates for the quadratic path

values = [value/100. for value in range(100)]
for node in node_points:
    x_end, y_end = network_layout[node]
    x_point.append(quad_path(x_start, x_end, 0, values))
    y_point.append(quad_path(y_start, y_end, 0, values))
    
#Add the x and y co-ordinates of the quadratic path to the network

network.edge_renderer.data_source.data['xs'] = x_point

network.edge_renderer.data_source.data['ys'] = y_point

#Output the plot

plot.renderers.append(network)

output_file("quad_path.html")

show(plot)

------------------------------------------------------------------------------------------------------

#Creating georpahic visualizations

#Import the required packages

from bokeh.sampledata import us_states
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

#Create a copy of the USA data in our notebook

usa_data = us_states.data.copy()

#Delete the states that are not of interest 

del usa_data["HI"]
del usa_data["AK"]

#Extract the latitude and longitude information

longitude = [usa_data[long]["lons"] for long in usa_data]

latitude = [usa_data[lat]["lats"] for lat in usa_data]

#Create the Hover Tool

hover_tool = HoverTool(tooltips = [
    ('Longitude', '@x'),
    ('Latitude', '@y')
]) 

#Create the figure

plot = figure(title="The 3 safest states in the USA", tools = [hover_tool])

#Configure the borders of the states

plot.patches(longitude, latitude, line_color="red", line_width=2)

#Mapping the longitude and latitude information into lists

long_list = [-69.44, -72.57, -71.57]

lat_list = [45.25, 44.55, 43,19]

# Create the markers for the states

plot.diamond(long_list, lat_list, size=15, color='yellow')

# output the plot

output_file("safe.html")

show(plot)

-----------------------------------------------------------------------------------------

#WebGL 

#Import required packages

import numpy as np
import random
from bokeh.io import output_file, show
from bokeh.plotting import figure

#Creating an array for the points along the x and y axes

array_x =np.array([1,2,3,4,5,6])

array_y = np.array([5,6,7,8,9,10])

#Creating a line plot

plot = figure(output_backend = 'webgl')

plot.line(array_x, array_y)

#Output the plot

output_file('numpy_line.html')

show(plot)

---------------------------------------------------------------------------------------------

#Exporting plots as PNG images

#Package installations on terminal/PowerShell

conda install selenium phantomjs pillow

pip3 install selenium

#Import the required packages

from bokeh.io import export_png

#Export the png image

export_png(plot, filename="safe_states.png")

-----------------------------------------------------------------------------------------------
