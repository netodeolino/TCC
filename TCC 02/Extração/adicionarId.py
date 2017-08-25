# -*- coding: UTF-8 -*-
import numpy as np
import pandas

arrayDeFrames = []


def main():
	# Ler arquivo e salva no frame
	dataFrame = pandas.read_csv("./janeiro-crimes.csv")

	# Cria o indice e preenche (ID)
	dataFrame['ID'] = range(1, len(dataFrame) + 1)

	# Reestrutura as colunas
	dataFrame = dataFrame[['ID', 'FONTE', 'NATUREZA DA OCORRÊNCIA', 'HISTÓRICO DA OCORRÊNCIA', 'LOCAL:', 'SUSPEITO:',
				'VEÍCULO:', 'VÍTIMA:', 'VÍTIMAS:', 'VÍTIMA FATAL:', 'ARMA APREENDIDA:', 'MATERIAL APREENDIDO:',
				'PLACA:', 'VÍTIMAS LESIONADAS:', 'SUSPEITOS:', 'DATA', 'LATITUDE', 'LONGITUDE']]

	# Salva o novo arquivo CSV
	dataFrame.to_csv("./janeiro-crimes.csv", index=False)

if __name__ == '__main__':
	main()