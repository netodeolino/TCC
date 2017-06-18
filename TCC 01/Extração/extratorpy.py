# -*- coding: UTF-8 -*-
import numpy as np
import pandas


# - Variáveis globais (global nomeVariavel)
ENTIDADE_NAO_ENCOTRADA = -1
ENTIDADE_VAZIA = "NÃO POSSUI ESSA INFORMAÇÃO"


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
				"MATERIAL APREENDIDO:", "PLACA:", "VÍTIMAS LESIONADAS:", "OBJETOS:", "SUSPEITOS:"
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
	arrayLinha.append(k.values)


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
			aux += string[i]
		if (string[i] == ".") and (string[i-1] != "V"):
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
			aux += string[i]
		if (string[i] == ".") and (string[i-1] != "V"):
			break
		i += 1

	return aux


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


# - Recebe uma entidade e, a partir dos dados HISTÓRICO DA OCORRÊNCIA 'arrayLinha', recupera os dados da entidade e salva
#   em um DataFrame
def inserirValorNoDataFrame(entidade):
	listaValores = []

	t = 0
	while t < len(arrayLinha):
		valo = extrairUmaEntidadeDeUmaLinha(arrayLinha, entidade, t)
		listaValores.append(valo)
		t += 1

	dataFrameOriginal[entidade] = pandas.Series(listaValores)


# - Função que simula a função inicial (def __init__:)
# - Insere os valores nas colunas correspondentes e salva em um arquivo .CSV
def main():	
	e = 0
	while e < len(entidades):
		inserirValorNoDataFrame(entidades[e])
		e += 1
	# - Consertar para salvar de acordo com o dia/mês lido
	dataFrameOriginal.to_csv('./teste.csv')


main()


# ------------------ Teste e Debug -------------------------------

#print(len(arrayLinha))
#print(type(arrayLinha[0]))

#for l in arrayLinha[0]:
#	print (l)

#for i in dataFrameInicial.iterrows():
#	print (i)

#extrairEntrePontos(stringLinha)

#extrair(stringLinha, posicaoIni)

#extrairUmaEntidade(arrayLinha, "SUSPEITO:")

#print (type(listaFinal))

#extrairUmaEntidadeDeUmaLinha(arrayLinha, "ARMA APREENDIDA:", 10)

#extrairTodasEntidades(arrayLinha)
