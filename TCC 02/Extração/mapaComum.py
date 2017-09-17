# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
import pandas
import gmplot

dataFrame = pandas.read_csv("./janeiro-crimes.csv")
novoFrame = dataFrame.copy()

lats = []
lons = []
for i, row in dataFrame.iterrows():
	if row['LONGITUDE']:
		lons.append(row['LONGITUDE'])
	if row['LATITUDE']:
		lats.append(row['LATITUDE'])


gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

#gmap.plot(lats, lons, 'cornflowerblue', edge_width=10)
#gmap.scatter(lats, lons, '#3B0B39', size=40, marker=False)
#gmap.scatter(lats, lons, 'k', marker=True)
gmap.heatmap(lats, lons)

gmap.draw("mymap.html")