# -*- coding: UTF-8 -*-
import pandas

class QuantidadePorCluster(object):
	
	def calcularQuantidade(self):
		dataFrame = pandas.read_csv("./cluster-janeiro.csv")
		indices = dataFrame.groupby('CLUSTER').size().reset_index(name='COUNTS')
		
		array = []
		for df in dataFrame['CLUSTER']:
			for i in indices.iterrows():
				if i[1]['CLUSTER'] == df:
					array.append(i[1]['COUNTS'])

		dataFrame["COUNT"] = pandas.Series(array)
		dataFrame.to_csv("./cluster-janeiro.csv", index=False)

if __name__ == '__main__':
	ts = QuantidadePorCluster()
	ts.calcularQuantidade()
