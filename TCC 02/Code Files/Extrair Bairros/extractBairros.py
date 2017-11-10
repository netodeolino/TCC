# -*- coding: UTF-8 -*-
import pandas

class ExtractBairro(object):

	def arrayToString(self, listRow):
		text = ""
		for strCell in listRow:
			for strIterator in strCell:
				text += strIterator
		return text


	def removeSpaceBeginning(self, string, start):
		i = start
		if (string[i] == " "):
			while (string[i] == " "):
				i = i + 1
		return i


	def extractBairro(self, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.loc[:, dataFrame.columns == "LOCAL:"]

		listHorario = []
		arrayRowHorario = []
		array = []

		for i, row in dataFrame.iterrows():
			if row["LOCAL:"]:
				listHorario.append(dataFrame.loc[i,:])

		for k in listHorario:
			arrayRowHorario.append(k.values)

		t = 0
		while t < len(arrayRowHorario):
			stringLinha = self.arrayToString(arrayRowHorario[t])
			inicio = stringLinha.find(',')+1
			inicio = self.removeSpaceBeginning(stringLinha, inicio)

			aux = ""
		
			i = inicio;
			while i < len(stringLinha):
				if (stringLinha[i] != "."):
					aux += stringLinha[i]
				i += 1
			array.append(aux)
			t += 1

		dataFrameOriginal["BAIRRO"] = pandas.Series(array)


	def main(self, files):
		for file in files:
			dataFrameInicial = pandas.read_csv("./data/" + file + ".csv")
			dataFrameOriginal = dataFrameInicial.copy()
			
			self.extractBairro(dataFrameInicial, dataFrameOriginal)

			dataFrameOriginal.to_csv("./data/" + file + ".csv", index=False)
