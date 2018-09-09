from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components
import quandl
import pandas as pd
import numpy as np
import math

quandl.ApiConfig.api_key = 'SM3z1sMm8gwUgJrkMsJL'

app = Flask(__name__)
app.vars = {}

@app.route('/')
def main():
	return render_template('index.html')
 
@app.route('/graph',methods = ['POST', 'GET'])
def graph():
        if request.method == 'POST':
                app.vars['ticket'] = request.form['ticket']
		app.vars['startDate'] = request.form['startDate']
		app.vars['endDate'] = request.form['endDate']
		timeRange = pd.date_range(app.vars['startDate'], app.vars['endDate'])
                rawData = quandl.get_table('WIKI/PRICES', ticker = app.vars['ticket'])
                rawDataTime = rawData.date.values
		indexList = []
                for x in range(rawDataTime.size):
                        if rawDataTime[x] in timeRange:
                                indexList.append(x)
                data = rawData.iloc[indexList]                
                p = figure(plot_height = 400, plot_width = 800, x_axis_label= 'date', x_axis_type= 'datetime',
                           title = app.vars['ticket'] + ' stock price from ' + app.vars['startDate'] \
                           + ' to ' + app.vars['endDate'])

                p.title.text_color = "black"
                p.title.text_font = "times"
                p.title.text_font_style = "italic"
                p.title.text_font_size = "28pt"
                p.title.align = "center"
                p.xaxis.major_label_text_font_size = "12pt"
                p.xaxis.major_label_orientation = math.pi/4
                p.yaxis.major_label_text_font_size = "12pt"

		xVal = data.date
		yVal = data.close
		p.line(xVal, yVal, color="red", line_width = 3)
		p.background_fill_color = "beige"
		p.background_fill_alpha = 0.5
		p.outline_line_width = 7
                p.outline_line_alpha = 0.3
                p.outline_line_color = "navy"
		p.xaxis.axis_label = 'date'
		p.xaxis.axis_label_text_font_size = '18pt'
		p.yaxis.axis_label = 'Stock Close Price ($)'
		p.yaxis.axis_label_text_font_size = '18pt'

                script,div = components(p)
                return render_template('graph.html',script = script, div = div)
        else:
                return render_template('index.html')
                

if __name__ == '__main__':
	app.run(port = 3000)




