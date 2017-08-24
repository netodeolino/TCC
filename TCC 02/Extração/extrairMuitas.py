# -*- coding: UTF-8 -*-
import numpy as np
import pandas


# - Variáveis globais
ENTIDADE_NAO_ENCOTRADA = -1
ENTIDADE_VAZIA = "NÃO POSSUI ESSA INFORMAÇÃO"

entidades = [
				"LOCAL:", "SUSPEITO:", "VEÍCULO:", "VÍTIMA:", "VÍTIMAS:", "VÍTIMA FATAL:", "ARMA APREENDIDA:",
				"MATERIAL APREENDIDO:", "PLACA:", "VÍTIMAS LESIONADAS:", "OBJETOS:", "SUSPEITOS:"
			]

# - arrayLinha[posicao] é do tipo narra, por isso, para facilitar, é feito a conversão para string
def transformaArrayEmString(lista):
	aux = ""
	for strCelula in lista:
		for strIterator in strCelula:
			aux += strIterator
	return aux


# - Início real da função de extração
# - Precisa fazer o processo de excluir da string os dados retornados aqui
def extrair(string, inicio, entidade):
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


# - Início real da função de extração
# - Precisa fazer o processo de excluir da string os dados retornados aqui
def extrairRetornar(string, inicio):
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


# - Função para retirar os ruidos de uma string
def eliminarRuidos(string):
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


# - Recebe a string completa de uma linha do HISTÓRICO DA OCORRÊNCIA e extrai a partir do primeiro ':'
# - Essa função sempre começa lendo do início da string 'stringLinha', portanto só pega o primeiro ':' e '.'
def extrairEntrePontos(string):
	i = 0;
	while i < len(string):
		if (string[i] == ":"):
			extrair(string, i+2) #Pegar o tamanho dos espaços
			break
		i += 1


# - Função para retirar espaços do início da string que irá ser extraída. Depois tratar caso de dois pontos ':'
def tirarEspacosDoInicio(string, inicio):
	
	inicioDaString = inicio
	if (string[inicioDaString] == " "):
		while (string[inicioDaString] == " "):
			inicioDaString = inicioDaString + 1
	return inicioDaString


# - Extrai uma entidade, porém tem que tratar o caso de quando a entidade não existe
def extrairUmaEntidade(arrayLinha, entidade):

	t = 0
	while t < len(arrayLinha):
		stringLinha = transformaArrayEmString(arrayLinha[t])
		print (stringLinha)

		posicaoIni = stringLinha.find(entidade)

		if (posicaoIni == ENTIDADE_NAO_ENCOTRADA):
			print (entidade + ENTIDADE_VAZIA)
		else:
			posicaoIni = posicaoIni + len(entidade)
		
			posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

			extrair(stringLinha, posicaoIni, entidade)
			#dadoDaEntidade = extrairRetornar(stringLinha, posicaoIni)

		t += 1


# - Extrai várias entidades, porém tem que tratar o caso de quando a entidade não existe
def extrairTodasEntidadesDeUmaLinha(string):

	listaEntidades = []
	string = transformaArrayEmString(string)

	for entidade in entidades:
		posicaoIni = string.find(entidade)

		if (posicaoIni != ENTIDADE_NAO_ENCOTRADA):
			posicaoIni = posicaoIni + len(entidade)

			posicaoIni = tirarEspacosDoInicio(string, posicaoIni)

			#extrair(stringLinha, posicaoIni, entidade)
			valorDaEntidade = extrairRetornar(string, posicaoIni)
			listaEntidades.append(valorDaEntidade)

	return listaEntidades


# - Extrai uma entidade, porém tem que tratar o caso de quando a entidade não existe
def extrairUmaEntidadeDeUmaLinha(arrayLinha, entidade, posicao):

	# - arrayLinha[posicao] é do tipo narray, e anteriormente list, por isso, para facilitar, é feito a conversão para string
	stringLinha = transformaArrayEmString(arrayLinha[posicao])

	posicaoIni = stringLinha.find(entidade)

	if (posicaoIni == ENTIDADE_NAO_ENCOTRADA):
		return ENTIDADE_VAZIA
	else:
		posicaoIni = posicaoIni + len(entidade)
	
		posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

		#extrair(stringLinha, posicaoIni, entidade)
		return extrairRetornar(stringLinha, posicaoIni)


# - Extrai todas entidades, porém tem que tratar o caso de quando a entidade não existe, por enquanto imprime um texto
def extrairTodasEntidades(arrayLinha):

	t = 0
	while t < len(arrayLinha):
		# - arrayLinha[t] é do tipo narray, e anteriormente list, por isso, para facilitar, é feito a conversão para string
		stringLinha = transformaArrayEmString(arrayLinha[t])
		print (stringLinha  + "\n")

		for entidade in entidades:

			posicaoIni = stringLinha.find(entidade)

			if (posicaoIni == ENTIDADE_NAO_ENCOTRADA):
				print (entidade + ENTIDADE_VAZIA)
			else:
				posicaoIni = posicaoIni + len(entidade)

				posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

				extrair(stringLinha, posicaoIni, entidade)
				#dadoDaEntidade = extrairRetornar(stringLinha, posicaoIni)
		print ("\n")
		t += 1


# - Função para salvar as datas dos crimes
def inserirData(arrayLinha, dia, mes, dataFrameOriginal):
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


# - Recebe uma entidade e, a partir dos dados HISTÓRICO DA OCORRÊNCIA 'arrayLinha', recupera os dados da entidade e salva
#   em um DataFrame
def inserirValorNoDataFrame(entidade, arrayLinha, dataFrameOriginal):
	listaValores = []

	t = 0
	while t < len(arrayLinha):
		valor = extrairUmaEntidadeDeUmaLinha(arrayLinha, entidade, t)
		listaValores.append(valor)
		t += 1

	dataFrameOriginal[entidade] = pandas.Series(listaValores)


# - Insere os valores nas colunas correspondentes e salva nos arquivos .CSV
def main():

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
		while e < len(entidades):
			inserirValorNoDataFrame(entidades[e], arrayLinha, dataFrameOriginal)
			e += 1

		
		# - Cria uma coluna para data e insere nas linhas os valores correspondentes
		inserirData(arrayLinha, dia, mes, dataFrameOriginal)


		# - Última etapa, salvar todas as alterações realizadas em novos arquivos CSVs
		dataFrameOriginal.to_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv", index=False)


if __name__ == '__main__':
	main()


# ------------------ Teste e Debug -------------------------------


