# -*- coding: UTF-8 -*-
import pandas

class Extract(object):
	def __init__(self, entidades):
		self.ENTIDADE_NAO_ENCOTRADA = -1
		self.ENTIDADE_VAZIA = "null"
		self.entidades = entidades


	def arrayToString(self, lista):
		aux = ""
		for strCelula in lista:
			for strIterator in strCelula:
				aux += strIterator
		return aux


	def extractSSPDS(self, string, inicio):
		text = ""
		i = inicio;
		
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


	# - Função para retirar espaços do início da string que irá ser extraída
	def removeSpaceBeginning(self, string, inicio):
		
		inicioDaString = inicio
		if (string[inicioDaString] == " "):
			while (string[inicioDaString] == " "):
				inicioDaString = inicioDaString + 1
		return inicioDaString


	# - Extrai uma entidade
	def extractOneEntityFromRow(self, arrayLinha, entidade, posicao, otherSource=False):
		# - arrayLinha[posicao] é do tipo narray por isso, para facilitar, é feito a conversão para string
		stringLinha = self.arrayToString(arrayLinha[posicao])

		posicaoIni = stringLinha.find(entidade)

		if (posicaoIni == self.ENTIDADE_NAO_ENCOTRADA):
			return self.ENTIDADE_VAZIA
		else:
			posicaoIni = posicaoIni + len(entidade)
			posicaoIni = self.removeSpaceBeginning(stringLinha, posicaoIni)
			
			if (otherSource):
				return otherSource(stringLinha, posicaoIni)
			else:
				return self.extractSSPDS(stringLinha, posicaoIni)


	# - Função para salvar as datas dos crimes
	def inserirData(self, dia, mes, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.drop('HISTÓRICO DA OCORRÊNCIA', 1)
		dataFrame = dataFrame.drop('NATUREZA DA OCORRÊNCIA', 1)

		lista = []
		arrayLinha = []

		for i, row in dataFrame.iterrows():
			if row['FONTE']:
				lista.append(dataFrame.loc[i,:])

		# - Salva em 'arrayLinha' o conteúdo das linhas de 'lista'
		for k in lista:
			arrayLinha.append(k.values)

		listaDeDatas = []
		
		if mes == "jan":
			data = dia + "/01/2017"
		elif mes == "fev":
			data = dia + "/02/2017"
		elif mes == "mar":
			data = dia + "/03/2017"
		else:
			data = dia + "/04/2017"

		for linha in arrayLinha:
			listaDeDatas.append(data)

		dataFrameOriginal["DATA"] = pandas.Series(listaDeDatas)


	# - Recebe uma entidade e, a partir dos dados HISTÓRICO DA OCORRÊNCIA, recupera os dados da entidade e salva
	#   em um DataFrame
	def inserirValorNoDataFrame(self, entidade, arrayLinha, dataFrame, otherSource=False):
		listValores = []
		
		t = 0
		while t < len(arrayLinha):
			if (otherSource):
				valor = self.extractOneEntityFromRow(arrayLinha, entidade, t, otherSource)
				listValores.append(valor)
			else:
				valor = self.extractOneEntityFromRow(arrayLinha, entidade, t)
				listValores.append(valor)
			t += 1

		dataFrame[entidade] = pandas.Series(listValores)
		

	def extrairHistoricoDaOcorrencia(self, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.loc[:, dataFrame.columns == 'HISTÓRICO DA OCORRÊNCIA']
		
		lista = []
		arrayLinha = []

		for i, row in dataFrame.iterrows():
			if row['HISTÓRICO DA OCORRÊNCIA']:
				lista.append(dataFrame.loc[i,:])

		# - Salva em 'arrayLinha' o conteúdo das linhas de 'lista'
		for k in lista:
			arrayLinha.append(k.values)

		# - Para cada entidade insere o valor das linhas no DataFrame que vai, no fim, ser salvo
		e = 0
		while e < len(self.entidades):
			self.inserirValorNoDataFrame(self.entidades[e], arrayLinha, dataFrameOriginal)
			e += 1


	def extrairNaturezaDaOcorrencia(self, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.loc[:, dataFrame.columns == 'NATUREZA DA OCORRÊNCIA']

		listaHorario = []
		arrayLinhaHorario = []

		# - Salva em 'lista' as linhas de NATUREZA DA OCORRÊNCIA
		for i, row in dataFrame.iterrows():
			if row['NATUREZA DA OCORRÊNCIA']:
				listaHorario.append(dataFrame.loc[i,:])

		# - Salva em 'arrayLinhaHorario' o conteúdo das linhas de 'listaHorario'
		for k in listaHorario:
			arrayLinhaHorario.append(k.values)

		self.extractTimeHour(arrayLinhaHorario, dataFrameOriginal)
		self.removeTimeFromRow(arrayLinhaHorario, dataFrameOriginal)


	def extractOtherSource(self, dataFrame, dataFrameOriginal, column, otherSource):
		dataFrame = dataFrame.loc[:, dataFrame.columns == column]
		
		lista = []
		arrayLinha = []
		
		# - Salva em 'lista' as linhas de NATUREZA DA OCORRÊNCIA
		for i, row in dataFrame.iterrows():
			if row[column]:
				lista.append(dataFrame.loc[i,:])

		# - Salva em 'arrayLinha' o conteúdo das linhas de 'lista'
		for k in lista:
			arrayLinha.append(k.values)

		# - Para cada entidade insere o valor das linhas no DataFrame que vai, no fim, ser salvo
		e = 0
		while e < len(self.entidades):
			self.inserirValorNoDataFrame(self.entidades[e], arrayLinha, dataFrameOriginal, otherSource)
			e += 1
		

	def extractTimeHour(self, arrayLinha, dataFrame):
		listaDeHorarios = []
		t = 0

		while t < len(arrayLinha):
			stringLinha = self.arrayToString(arrayLinha[t])
			fim = len(stringLinha)

			aux = ""
			x = 5
			while x > 0:
				aux += stringLinha[fim-x]
				x -= 1
			listaDeHorarios.append(aux)
			t += 1
		
		dataFrame["HORARIO"] = pandas.Series(listaDeHorarios)


	def removeTimeFromRow(self, arrayLinha, dataFrame):
		lista = []
		
		t = 0
		while t < len(arrayLinha):
			stringLinha = self.arrayToString(arrayLinha[t])
			fim = len(stringLinha) - 5

			aux = ""
			x = 0
			while x < fim:
				aux += stringLinha[x]
				x += 1
			lista.append(aux)
			t += 1
		
		dataFrame["NATUREZA DA OCORRÊNCIA"] = pandas.Series(lista)


	def main(self, files, column=False, otherSource=False):
		listFiles = files

		for file in listFiles:
			dataFrameInicial = pandas.read_csv("./" + file + ".csv")
			dataFrameOriginal = dataFrameInicial.copy()
			
			if (otherSource and column):
				self.extractOtherSource(dataFrameInicial, dataFrameOriginal, column, otherSource)
			else:
				self.extrairHistoricoDaOcorrencia(dataFrameInicial, dataFrameOriginal)
				self.extrairNaturezaDaOcorrencia(dataFrameInicial, dataFrameOriginal)

			# - Cria uma coluna para data e insere nas linhas os valores correspondentes
			#self.inserirData(file, mes, dataFrameInicial, dataFrameOriginal)

			# - Última etapa, salvar todas as alterações realizadas em novos arquivos CSVs
			dataFrameOriginal.to_csv("./novo-" + file + ".csv", index=False)
