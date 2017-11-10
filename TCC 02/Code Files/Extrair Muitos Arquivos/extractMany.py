# -*- coding: UTF-8 -*-
import pandas

class Extract(object):
	def __init__(self, entities):
		self.ENTITY_NOT_FOUND = -1
		self.ENTITY_NULL = "nulo"
		self.entities = entities


	def arrayToString(self, lista):
		text = ""
		for strCell in lista:
			for strIterator in strCell:
				text += strIterator
		return text


	def extractSSPDS(self, string, start):
		text = ""
		i = start;
		
		while i < len(string):
			if (string[i] != "."):
				text += string[i]
			if ((string[i] == ".") and (string[i-1] == "V")):
				if ((string[i-1] == "V") and (string[i-2] == "A")):
					text += string[i]
			if ((string[i] == ".") and (string[i-1] == "R")):
				if ((string[i-1] == "R") and (string[i-2] == "D")):
					text += string[i]
			if ((string[i] == ".") and (string[i-1] != "V")) and ((string[i] == ".") and (string[i-1] != "R")):
				break
			i += 1

		return text


	def removeSpaceBeginning(self, string, start):
		
		i = start
		if (string[i] == " "):
			while (string[i] == " "):
				i = i + 1
		return i


	def extractOneEntityFromRow(self, arrayRow, entity, position, externalMethod=False):
		stringRow = self.arrayToString(arrayRow[position])

		startingPosition = stringRow.find(entity)

		if (startingPosition == self.ENTITY_NOT_FOUND):
			return self.ENTITY_NULL
		else:
			startingPosition = startingPosition + len(entity)
			startingPosition = self.removeSpaceBeginning(stringRow, startingPosition)
			
			if (externalMethod):
				return externalMethod(stringRow, startingPosition)
			else:
				return self.extractSSPDS(stringRow, startingPosition)


	def inserirDate(self, file, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.loc[:, dataFrame.columns == "FONTE"]

		dateArray = file.split("-")

		listAux = []
		arrayRow = []
		
		for i, row in dataFrame.iterrows():
			if row["FONTE"]:
				listAux.append(dataFrame.loc[i,:])

		for k in listAux:
			arrayRow.append(k.values)

		dateList = []

		if dateArray[2] == "jan":
			data = dateArray[1] + "/01/" + dateArray[3]
		elif dateArray[2] == "fev":
			data = dateArray[1] + "/02/" + dateArray[3]
		elif dateArray[2] == "mar":
			data = dateArray[1] + "/03/" + dateArray[3]
		elif dateArray[2] == "abr":
			data = dateArray[1] + "/04/" + dateArray[3]
		elif dateArray[2] == "mai":
			data = dateArray[1] + "/05/" + dateArray[3]
		elif dateArray[2] == "jun":
			data = dateArray[1] + "/06/" + dateArray[3]
		elif dateArray[2] == "jul":
			data = dateArray[1] + "/07/" + dateArray[3]
		elif dateArray[2] == "ago":
			data = dateArray[1] + "/08/" + dateArray[3]
		elif dateArray[2] == "set":
			data = dateArray[1] + "/09/" + dateArray[3]
		elif dateArray[2] == "out":
			data = dateArray[1] + "/10/" + dateArray[3]
		elif dateArray[2] == "nov":
			data = dateArray[1] + "/11/" + dateArray[3]
		elif dateArray[2] == "dez":
			data = dateArray[1] + "/12/" + dateArray[3]
		else:
			data = self.ENTITY_NULL

		for linha in arrayRow:
			dateList.append(data)

		dataFrameOriginal["DATA"] = pandas.Series(dateList)


	def insertDataFrameValues(self, entity, arrayRow, dataFrame, externalMethod=False):
		valuesList = []
		
		t = 0
		while t < len(arrayRow):
			if (externalMethod):
				valor = self.extractOneEntityFromRow(arrayRow, entity, t, externalMethod)
				valuesList.append(valor)
			else:
				valor = self.extractOneEntityFromRow(arrayRow, entity, t)
				valuesList.append(valor)
			t += 1

		dataFrame[entity] = pandas.Series(valuesList)
		

	def extractHistoricoDaOcorrencia(self, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.loc[:, dataFrame.columns == 'HISTÓRICO DA OCORRÊNCIA']
		
		lista = []
		arrayRow = []

		for i, row in dataFrame.iterrows():
			if row['HISTÓRICO DA OCORRÊNCIA']:
				lista.append(dataFrame.loc[i,:])

		for k in lista:
			arrayRow.append(k.values)

		e = 0
		while e < len(self.entities):
			self.insertDataFrameValues(self.entities[e], arrayRow, dataFrameOriginal)
			e += 1


	def extractNaturezaDaOcorrencia(self, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.loc[:, dataFrame.columns == 'NATUREZA DA OCORRÊNCIA']

		listaHorario = []
		arrayRowHorario = []

		for i, row in dataFrame.iterrows():
			if row['NATUREZA DA OCORRÊNCIA']:
				listaHorario.append(dataFrame.loc[i,:])

		for k in listaHorario:
			arrayRowHorario.append(k.values)

		self.extractTimeHour(arrayRowHorario, dataFrameOriginal)
		self.removeTimeFromRow(arrayRowHorario, dataFrameOriginal)
		self.extractFlagrante(arrayRowHorario, dataFrameOriginal)


	def extractFlagrante(self, arrayRow, dataFrame):
		lista = []
		t = 0
		while t < len(arrayRow):
			strRow = self.arrayToString(arrayRow[t])
			start = strRow.find('(FLAGRANTE)')
			if start == -1:
				lista.append('FALSE')
			else:
				lista.append('TRUE')
			t += 1
		dataFrame["FLAGRANTE"] = pandas.Series(lista)


	def extractExternalMethod(self, dataFrame, dataFrameOriginal, column, externalMethod):
		dataFrame = dataFrame.loc[:, dataFrame.columns == column]
		
		lista = []
		arrayRow = []
		
		for i, row in dataFrame.iterrows():
			if row[column]:
				lista.append(dataFrame.loc[i,:])

		for k in lista:
			arrayRow.append(k.values)

		e = 0
		while e < len(self.entities):
			self.insertDataFrameValues(self.entities[e], arrayRow, dataFrameOriginal, externalMethod)
			e += 1
		

	def extractTimeHour(self, arrayRow, dataFrame):
		listaDeHorarios = []
		t = 0

		while t < len(arrayRow):
			strRow = self.arrayToString(arrayRow[t])
			fim = len(strRow)

			aux = ""
			x = 5
			while x > 0:
				aux += strRow[fim-x]
				x -= 1
			listaDeHorarios.append(aux)
			t += 1
		
		dataFrame["HORARIO"] = pandas.Series(listaDeHorarios)


	def removeTimeFromRow(self, arrayRow, dataFrame):
		listAux = []
		
		t = 0
		while t < len(arrayRow):
			strRow = self.arrayToString(arrayRow[t])
			strRow = strRow.replace("(FLAGRANTE)", "")
			fim = len(strRow) - 5

			text = ""
			x = 0
			while x < fim:
				text += strRow[x]
				x += 1
			listAux.append(text)
			t += 1
		
		dataFrame["NATUREZA DA OCORRÊNCIA"] = pandas.Series(listAux)


	def main(self, files, column=False, externalMethod=False):
		listFiles = files

		for file in listFiles:
			dataFrameInicial = pandas.read_csv("./data/" + file + ".csv")
			dataFrameOriginal = dataFrameInicial.copy()
			
			if (externalMethod and column):
				self.extractExternalMethod(dataFrameInicial, dataFrameOriginal, column, externalMethod)
			else:
				self.extractHistoricoDaOcorrencia(dataFrameInicial, dataFrameOriginal)
				self.extractNaturezaDaOcorrencia(dataFrameInicial, dataFrameOriginal)
				self.inserirDate(file, dataFrameInicial, dataFrameOriginal)

			dataFrameOriginal.to_csv("./data/novo-" + file + ".csv", index=False)
