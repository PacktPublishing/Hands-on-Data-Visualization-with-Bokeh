#Installing Bokeh (Shell/Terminal Code)

conda install bokeh

pip install bokeh

pip3 install bokeh



#Verifying Installation Code

from bokeh.plotting import figure, output_file, show

#HTML file to output your plot into
output_file("bokeh.html")

#Constructing a basic line plot 

x = [1,2,3]
y = [4,5,6]

p = figure()

p.line(x,y)

show(p)



#Code to construct a figure

from bokeh.plotting import figure

# create a Figure object
p = figure(plot_width=500, plot_height=400, tools="pan,hover")
