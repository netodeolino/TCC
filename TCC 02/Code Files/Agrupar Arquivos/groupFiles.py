# -*- coding: UTF-8 -*-
import pandas

class Group(object):
	def __init__(self):
		self.arrayDeFrames = []
		self.ENTITY_NULL = "nulo"


	def removeEmptyEntities(self, dataFrame):
		return dataFrame[dataFrame.LATITUDE.astype(str) != self.ENTITY_NULL]


	def main(self, files, filename, SSPDS=True):
		for file in files:
			dataFrame = pandas.read_csv("./data/" + file + ".csv")
			if (SSPDS):
				dataFrame = self.removeEmptyEntities(dataFrame)
			
			self.arrayDeFrames.append(dataFrame)

		newDataFrame = pandas.concat(self.arrayDeFrames)
		newDataFrame['ID'] = range(1, len(newDataFrame) + 1)

		if (SSPDS):
			newDataFrame = newDataFrame[['ID', 'FONTE', 'FLAGRANTE', 'NATUREZA DA OCORRÊNCIA', 'HISTÓRICO DA OCORRÊNCIA', 'LOCAL:',
					'BAIRRO', 'SUSPEITO:', 'VEÍCULO:', 'VÍTIMA:', 'VÍTIMAS:', 'VÍTIMA FATAL:', 'ARMA APREENDIDA:',
					'MATERIAL APREENDIDO:', 'PLACA:', 'VÍTIMAS LESIONADAS:', 'SUSPEITOS:', 'HORA', 'MINUTO', 'DATA', 'LATITUDE', 'LONGITUDE']]

		newDataFrame.to_csv("./data/" + filename + ".csv", index=False)
