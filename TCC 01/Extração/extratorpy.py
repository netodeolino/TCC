# -*- coding: UTF-8 -*-
import numpy as np
import pandas

#Global (global nomeVariavel)
tes = pandas.read_csv("./tabula-01-jan-17.csv")
teste = []
list = []


del tes['FONTE']
del tes['NATUREZA DA OCORRÊNCIA']


#for i in tes.iterrows():
#	print (i)


for i, row in tes.iterrows():
	if row['HISTÓRICO DA OCORRÊNCIA']:
		list.append(tes.loc[i,:])


for k in list:
	#print (k.values)
	teste.append(k.values)

print(len(teste))
#print(type(teste[0]))

#for l in teste[0]:
#	print (l)


def transformaListEmString(lista):
	aux = ""
	for strCelula in lista:
		for strIterator in strCelula:
			aux += strIterator
	return aux

def extrair(string, inicio):
	aux = ""
	
	# - Início real da função de extração
	# - Precisa fazer o processo de excluir da string os dados retornados aqui
	i = inicio;
	while i < len(string):
		if (string[i] != "."):
			aux += string[i]
		if (string[i] == "."):
			break
		i += 1
	print ("\n")
	# - Depois usar um 'return' ao invés de só imprimir
	print (aux)


# Recebe a string completa de uma linha do HISTÓRICO DA OCORRÊNCIA
def extrairEntrePontos(string):
	i = 0;
	while i < len(string):
		# - Se encontrar dois pontos chamar 'extrair()' passando a string e a posição que deve começar a extrair
		# - Essa função sempre começa lendo do início da string 'stringLinha', portanto só pega o primeiro ':' e '.'
		if (string[i] == ":"):
			extrair(string, i+2) #Pegar o tamanho dos espaços
			break
		i += 1


# - Função para retirar espaços do início da string que irá ser extraída
def tirarEspacosDoInicio(string, inicio):
	
	inicioDaString = inicio
	if (string[inicioDaString] == " "):
		while (string[inicioDaString] == " "):
			inicioDaString = inicioDaString+1
	return inicioDaString


stringLinha = transformaListEmString(teste[0])
print (stringLinha)

posicaoIni = stringLinha.find("ARMA APREENDIDA:")
posicaoIni = posicaoIni + len("ARMA APREENDIDA:")
#print (posicaoIni)

#extrairEntrePontos(stringLinha)

# - Teste da função para tirar espaços desnecessários do início da string
posicaoIni = tirarEspacosDoInicio(stringLinha, posicaoIni)

extrair(stringLinha, posicaoIni)
