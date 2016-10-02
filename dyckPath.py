from flask import Flask, render_template
import random
import os
import util

# imports for Bokeh plotting
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components

# imports for matplotlib plotting
import tempfile
import matplotlib
matplotlib.use('Agg') # this allows PNG plotting
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def indexPage():
    # generate dyck path
    dyckPath = util.catlanGenerator(10)
    y = dyckPath
    x = range(len(y))

    # generate Bokeh HTML elements
    # create a `figure` object
    p = figure(title='A Dyck Path',plot_width=500,plot_height=400)
    # add the line
    p.line(x,y)
    # add axis labels
    p.xaxis.axis_label = "time"
    p.yaxis.axis_label = "size"
    # create the HTML elements to pass to template
    figJS,figDiv = components(p,CDN)

    return(render_template(
        'index.html',
        y=y,
        figJS=figJS,figDiv=figDiv))



if __name__ == '__main__':
    app.debug=True
    app.run()


