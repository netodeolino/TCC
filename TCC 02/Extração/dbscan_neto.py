# -*- coding: utf-8 -*-
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
import math
import numpy as np

progress = 0

def euclideanDistance(point, point2):
    x = float(point['latitude'])
    x1 = float(point2['latitude'])
    y = float(point['longitude'])
    y1 = float(point2['longitude'])

    #print np.sqrt((x - x1)**2 + ( y - y1)**2)

    return np.sqrt((x - x1)**2 + ( y - y1)**2)


def neighborhood(point, crimes, eps):
    neighborPts = []
    for point2 in crimes:

        # CHAME AQUI SUA MEDIDA DE SIMILARIDADE
        distance = euclideanDistance(point, point2)
        
        if distance > eps:
            neighborPts.append(point2);
    return neighborPts


def expandCluster(crimes, point, neighborPts, cluster, eps, minPts):
    global progress
    point['cluster'] = cluster

    for point1 in neighborPts:	
        if not point1['visited']:
            point1['visited'] = True
            neighborPts1 = neighborhood(point1, crimes, eps)
            progress = progress + 1
            print progress
            print " ----- Neibohood inside = " + str(len(neighborPts1))
            if len(neighborPts1) >= minPts:
                neighborPts.extend(neighborPts1)
        if point1['cluster'] == 0:
            point1['cluster'] = cluster


def dbScan(crimes, eps, minPts):
    global progress
    cluster = 0
    
    for point in crimes:
        if not point['visited']:
            point['visited'] = True
            neighborPts = neighborhood(point, crimes, eps)
            progress = progress + 1
            print progress
            print " --- Neibohood = " + str(len(neighborPts))
            if len(neighborPts) < minPts:
                point['cluster'] = -1
            else:
                print " ----- Criou um cluster -----"
                cluster += 1
                # point['cluster'] = cluster
                expandCluster(crimes, point, neighborPts, cluster, eps, minPts)


print '- - - - - - - - - - START - - - - - - - - - -'

#import json
#import simplejson as json
import pandas

dataFrame = pandas.read_csv("./janeiro-crimes.csv")

points = {}
points['crimes'] = []

for i, row in dataFrame.iterrows():
    point = {}

    if row['ID']:
        point['id'] = row['ID']
    if row['NATUREZA DA OCORRÊNCIA']:
        point['natureza'] = row['NATUREZA DA OCORRÊNCIA']
    if row['LATITUDE'] and row['LATITUDE'] != "NÃO POSSUI ESSA INFORMAÇÃO":
        #point['latitude'] = row['LATITUDE']
        latitude1 = row['LATITUDE']
    if row['LONGITUDE'] and row['LONGITUDE'] != "NÃO POSSUI ESSA INFORMAÇÃO":
        #point['longitude'] = row['LONGITUDE']
        longitude1 = row['LONGITUDE']

    if (latitude1 != "NÃO POSSUI ESSA INFORMAÇÃO") and (longitude1 != "NÃO POSSUI ESSA INFORMAÇÃO"):
        point['latitude'] = latitude1
        point['longitude'] = longitude1

        points['crimes'].append(point)


for point in points['crimes']:
    point['visited'] = False
    point['cluster'] = 0

dbScan(points['crimes'], 0.18, 27)


print "######## CLUSTERS ########"

# Print cluster amount
groups = defaultdict(list)

for obj in points['crimes']:
    groups[obj['cluster']].append(obj)

output_file = 0
new_list = groups.values()
quantCluster = len(new_list)

# Caminho do arquivo de saida dos clusters
output_file = open('./clusters.csv','a')
for x in range(0, quantCluster):
    print ' -> ' + str(new_list[x][0]['cluster']) + ': ' + str(len(new_list[x]))
    for y in range(0, len(new_list[x])):
        # if new_list[x][y]['cluster'] != -1:
        #     print new_list[x][y]['id']
        if new_list[x][y]['cluster'] != -1:
            text_id = new_list[x][y]['id']
            text_lat = new_list[x][y]['latitude']
            text_lng = new_list[x][y]['longitude']
            #text = str(text)
            #row = (text).encode('utf-8')+'\n'
            row = str(text_id) + ',' + str(text_lat) + ',' + str(text_lng) + '\n'
            output_file.write(row)
            #print row


# print "######## CLUSTERS ########"

print '- - - - - - - - - -  END  - - - - - - - - - -'
