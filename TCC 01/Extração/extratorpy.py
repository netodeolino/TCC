# -*- coding: UTF-8 -*-
import numpy as np
import pandas


# - Variáveis globais (global nomeVariavel)
ENTIDADE_NAO_ENCOTRADA = -1
ENTIDADE_VAZIA = " NÃO POSSUI ESSA INFORMAÇÃO"


# - Valores para agilizar no processo de ler vários .CSV's por vez
mes = "jan"
listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
				"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

dataFrameInicial = pandas.read_csv("./tabula-07-" + mes + "-17.csv")
dataFrameOriginal = dataFrameInicial

lista = []
arrayLinha = []
entidades = [
				"LOCAL:", "SUSPEITO:", "VEÍCULO:", "VÍTIMA:", "VÍTIMAS:", "VÍTIMA FATAL:", "ARMA APREENDIDA:",
				"MATERIAL APREENDIDO:", "PLACA:", "VÍTIMAS LESIONADAS:", "OBJETOS", "SUSPEITOS:"
			]

# - Tirando as outras 2 colunas
del dataFrameInicial["FONTE"]
del dataFrameInicial["NATUREZA DA OCORRÊNCIA"]


# - Salva em 'lista' as linhas de HISTÓRICO DA OCORRÊNCIA
for i, row in dataFrameInicial.iterrows():
	if row['HISTÓRICO DA OCORRÊNCIA']:
		lista.append(dataFrameInicial.loc[i,:])


# - Salva em 'arrayLinha' o conteúdo das linhas de 'lista'
for k in lista:
	#print (k.values)
	arrayLinha.append(k.values)


# - Remover da stringLinha os dados que foram extraídos dela?
def excluirTextoDaString(string, inicio, fim):
	pass


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
	global listaFinal
	aux = ""
	
	i = inicio;
	while i < len(string):
		if (string[i] != "."):
			aux += string[i]
		if ((string[i] == ".") and (string[i-1] == "V")):
			aux += string[i]
		if (string[i] == ".") and (string[i-1] != "V"):
			break
		i += 1

	# - Depois usar um 'return' ao invés de só imprimir
	print (entidade + " " + aux)


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
			inicioDaString = inicioDaString+1
	return inicioDaString


# - Extrai uma entidade, porém tem que tratar o caso de quando a entidade não existe
def extrairUmaEntidade(arrayLinha, entidade):

	t = 0
	while t < len(arrayLinha):
		stringLinha = transformaArrayEmString(arrayLinha[t])
		print (stringLinha)

		posicaoIni = stringLinha.find(entidade)

		# - Se não existe a entidade o valor retornada pelo find é -1
		if (posicaoIni == ENTIDADE_NAO_ENCOTRADA):
			print (entidade + ENTIDADE_VAZIA)
		else:
			posicaoIni = posicaoIni + len(entidade)
		
			posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

			extrair(stringLinha, posicaoIni, entidade)
		t += 1


# - Extrai uma entidade, porém tem que tratar o caso de quando a entidade não existe
def extrairUmaEntidadeEmUmaLinha(arrayLinha, entidade, posicao):

	# - arrayLinha[posicao] é do tipo narray, e anteriormente list, por isso, para facilitar, é feito a conversão para string
	stringLinha = transformaArrayEmString(arrayLinha[posicao])
	print (stringLinha + "\n")

	posicaoIni = stringLinha.find(entidade)

	if (posicaoIni == ENTIDADE_NAO_ENCOTRADA):
		print (entidade + ENTIDADE_VAZIA)
	else:
		posicaoIni = posicaoIni + len(entidade)
	
		# - Tira os espaços desnecessários do início da string antes dela ser extraída
		posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

		extrair(stringLinha, posicaoIni, entidade)


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

				# - Tira os espaços desnecessários do início da string
				posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

				extrair(stringLinha, posicaoIni, entidade)
		print ("\n")
		t += 1


# - Verificando quantidade de linhas
#print(len(arrayLinha))
#print(type(arrayLinha[0]))

#for l in arrayLinha[0]:
#	print (l)


#for i in dataFrameInicial.iterrows():
#	print (i)


#extrairEntrePontos(stringLinha)

# - Faz o processo de extração
#extrair(stringLinha, posicaoIni)

#extrairUmaEntidade(arrayLinha, "SUSPEITO:")

#print (type(listaFinal))

#extrairUmaEntidadeEmUmaLinha(arrayLinha, "ARMA APREENDIDA:", 10)

#extrairTodasEntidades(arrayLinha)


def salvarNovoCSV(dataFrameOriginal, string, entidade):
	
