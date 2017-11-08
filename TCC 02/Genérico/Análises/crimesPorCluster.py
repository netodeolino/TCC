# -*- coding: UTF-8 -*-
import pandas

class CrimesPorCluster(object):
	
	def crimes(self):
		dataFrame = pandas.read_csv("./cluster-janeiro.csv")
		indices = dataFrame.groupby('CLUSTER').indices
		
		for i in indices:
			novo = dataFrame[dataFrame['CLUSTER'] == i]

			novo.to_csv("./cluster-" + str(i) + "-janeiro.csv", index=False)


if __name__ == '__main__':
	cpc = CrimesPorCluster()
	cpc.crimes()