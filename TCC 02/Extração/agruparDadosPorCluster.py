# -*- coding: UTF-8 -*-
import numpy as np
import pandas

class GrupoPorCluster(object):
	
	def teste(self):
		dataFrame = pandas.read_csv("./janeiro.csv")
		indices = dataFrame.groupby('CLUSTER').indices
		#print (indices)
		
		for i in indices:
			novo = dataFrame[dataFrame['CLUSTER'] == i]
			#print ('------------------------------------------------------------------------------------------')
			#print (i)
			novo.to_csv("./indice=" + str(i) + "-grupos-janeiro.csv", index=False)


if __name__ == '__main__':
	ts = GrupoPorCluster()
	ts.teste()
