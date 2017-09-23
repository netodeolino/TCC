# -*- coding: UTF-8 -*-
import numpy as np
import pandas

class Extrator(object):
	def __init__(self):
		self.ENTIDADE_NAO_ENCOTRADA = -1
		self.ENTIDADE_VAZIA = "null"
		self.entidades = [
							"LOCAL:", "SUSPEITO:", "VEÍCULO:", "VÍTIMA:", "VÍTIMAS:", "VÍTIMA FATAL:", "ARMA APREENDIDA:",
							"MATERIAL APREENDIDO:", "PLACA:", "VÍTIMAS LESIONADAS:", "SUSPEITOS:"
						]
	

	def transformaArrayEmString(self, lista):
		aux = ""
		for strCelula in lista:
			for strIterator in strCelula:
				aux += strIterator
		return aux


	def extrairImprime(self, string, inicio, entidade):
		aux = ""
		
		i = inicio;
		while i < len(string):
			if (string[i] != "."):
				aux += string[i]
			
			if ((string[i] == ".") and (string[i-1] == "V")):
				if ((string[i-1] == "V") and (string[i-2] == "A")):
					aux += string[i]
			
			if ((string[i] == ".") and (string[i-1] == "R")):
				if ((string[i-1] == "R") and (string[i-2] == "D")):
					aux += string[i]
			
			if ((string[i] == ".") and (string[i-1] != "V")) and ((string[i] == ".") and (string[i-1] != "R")):
				break
			
			i += 1

		print (entidade + " " + aux)


	def extrairRetornar(self, string, inicio):
		aux = ""
		
		i = inicio;
		while i < len(string):
			if (string[i] != "."):
				aux += string[i]
			
			if ((string[i] == ".") and (string[i-1] == "V")):
				if ((string[i-1] == "V") and (string[i-2] == "A")):
					aux += string[i]
			
			if ((string[i] == ".") and (string[i-1] == "R")):
				if ((string[i-1] == "R") and (string[i-2] == "D")):
					aux += string[i]
			
			if ((string[i] == ".") and (string[i-1] != "V")) and ((string[i] == ".") and (string[i-1] != "R")):
				break
			
			i += 1

		return aux


	def eliminaRuidos(self, string):
		novaString = ""

		i = 0
		while i < len(string):
			if (string[i] == "."):
				novaString += " "
			elif (string[i] == ","):
				novaString += " "
			elif (string[i] == ";"):
				novaString += " "
			else:
				novaString += string[i]
			i += 1

		return novaString


	# - Essa função sempre começa lendo do início da string 'stringLinha', portanto só pega o primeiro ':' e '.'
	def extrairEntrePontos(self, string):
		i = 0;
		while i < len(string):
			if (string[i] == ":"):
				self.extrairImprime(string, i+2) #Pegar o tamanho dos espaços
				break
			i += 1


	# - Função para retirar espaços do início da string que irá ser extraída
	def tirarEspacosDoInicio(self, string, inicio):
		
		inicioDaString = inicio
		if (string[inicioDaString] == " "):
			while (string[inicioDaString] == " "):
				inicioDaString = inicioDaString + 1
		return inicioDaString


	def extrairUmaEntidade(self, arrayLinha, entidade):

		t = 0
		while t < len(arrayLinha):
			stringLinha = self.transformaArrayEmString(arrayLinha[t])
			print (stringLinha)

			posicaoIni = stringLinha.find(entidade)

			if (posicaoIni == self.ENTIDADE_NAO_ENCOTRADA):
				print (entidade + self.ENTIDADE_VAZIA)
			else:
				posicaoIni = posicaoIni + len(entidade)
			
				posicaoIni = self.tirarEspacosDoInicio(stringLinha, posicaoIni)

				self.extrairImprime(stringLinha, posicaoIni, entidade)
				#dadoDaEntidade = extrairRetornar(stringLinha, posicaoIni)

			t += 1


	# - Extrai várias entidades
	def extrairTodasEntidadesDeUmaLinha(self, string):

		listaEntidades = []
		string = self.transformaArrayEmString(string)

		for entidade in entidades:
			posicaoIni = string.find(entidade)

			if (posicaoIni != self.ENTIDADE_NAO_ENCOTRADA):
				posicaoIni = posicaoIni + len(entidade)

				posicaoIni = self.tirarEspacosDoInicio(string, posicaoIni)

				#extrairImprime(stringLinha, posicaoIni, entidade)
				valorDaEntidade = self.extrairRetornar(string, posicaoIni)
				listaEntidades.append(valorDaEntidade)

		return listaEntidades


	# - Extrai uma entidade
	def extrairUmaEntidadeDeUmaLinha(self, arrayLinha, entidade, posicao):

		# - arrayLinha[posicao] é do tipo narray por isso, para facilitar, é feito a conversão para string
		stringLinha = self.transformaArrayEmString(arrayLinha[posicao])

		posicaoIni = stringLinha.find(entidade)

		if (posicaoIni == self.ENTIDADE_NAO_ENCOTRADA):
			return self.ENTIDADE_VAZIA
		else:
			posicaoIni = posicaoIni + len(entidade)
		
			posicaoIni = self.tirarEspacosDoInicio(stringLinha, posicaoIni)

			#extrairImprime(stringLinha, posicaoIni, entidade)
			return self.extrairRetornar(stringLinha, posicaoIni)


	# - Extrai todas entidades
	def extrairTodasEntidades(self, arrayLinha):

		t = 0
		while t < len(arrayLinha):
			# - arrayLinha[t] é do tipo narray, e anteriormente list, por isso, para facilitar, é feito a conversão para string
			stringLinha = self.transformaArrayEmString(arrayLinha[t])
			print (stringLinha  + "\n")

			for entidade in entidades:

				posicaoIni = stringLinha.find(entidade)

				if (posicaoIni == self.ENTIDADE_NAO_ENCOTRADA):
					print (entidade + self.ENTIDADE_VAZIA)
				else:
					posicaoIni = posicaoIni + len(entidade)

					posicaoIni = self.tirarEspacosDoInicio(stringLinha, posicaoIni)

					self.extrairImprime(stringLinha, posicaoIni, entidade)
					#dadoDaEntidade = extrairRetornar(stringLinha, posicaoIni)
			print ("\n")
			t += 1


	# - Função para salvar as datas dos crimes
	def inserirData(self, arrayLinha, dia, mes, dataFrame):
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

		dataFrame["DATA"] = pandas.Series(listaDeDatas)


	# - Recebe uma entidade e, a partir dos dados HISTÓRICO DA OCORRÊNCIA, recupera os dados da entidade e salva
	#   em um DataFrame
	def inserirValorNoDataFrame(self, entidade, arrayLinha, dataFrame):
		listValores = []

		t = 0
		while t < len(arrayLinha):
			valor = self.extrairUmaEntidadeDeUmaLinha(arrayLinha, entidade, t)
			listValores.append(valor)
			t += 1

		dataFrame[entidade] = pandas.Series(listValores)


	def main(self):

		# - Valores para agilizar no processo de ler vários .CSV's por vez
		mes = "jan"
		listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
					"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

		for dia in listDiasMes:
			dataFrameInicial = pandas.read_csv("./tabula-" + dia + "-" + mes + "-17.csv")
			dataFrameOriginal = dataFrameInicial.copy()

			lista = []
			arrayLinha = []

			# - Tirando as outras 2 colunas
			del dataFrameInicial["FONTE"]
			del dataFrameInicial["NATUREZA DA OCORRÊNCIA"]


			# - Salva em 'lista' as linhas de HISTÓRICO DA OCORRÊNCIA
			for i, row in dataFrameInicial.iterrows():
				if row['HISTÓRICO DA OCORRÊNCIA']:
					lista.append(dataFrameInicial.loc[i,:])


			# - Salva em 'arrayLinha' o conteúdo das linhas de 'lista'
			for k in lista:
				arrayLinha.append(k.values)

			# - Para cada entidade insere o valor das linhas no DataFrame que vai, no fim, ser salvo
			e = 0
			while e < len(self.entidades):
				self.inserirValorNoDataFrame(self.entidades[e], arrayLinha, dataFrameOriginal)
				e += 1

			# - Cria uma coluna para data e insere nas linhas os valores correspondentes
			self.inserirData(arrayLinha, dia, mes, dataFrameOriginal)

			# - Última etapa, salvar todas as alterações realizadas em novos arquivos CSVs
			dataFrameOriginal.to_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv", index=False)


if __name__ == '__main__':
	extract = Extrator()
	extract.main()


# ------------------ Teste e Debug -------------------------------
