# -*- coding: UTF-8 -*-
import numpy as np
import pandas
import requests

ENTIDADE_VAZIA = "null"


def main():
	# - Valores para agilizar no processo de ler vários .CSV's por vez
	mes = "jan"
	listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
					"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
				]

	for dia in listDiasMes:
		dataFrameInicial = pandas.read_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv")

		teste = dataFrameInicial[dataFrameInicial.LATITUDE.astype(str) != ENTIDADE_VAZIA]

		#print(dataFrameInicial.LATITUDE.astype(str))

		# - Salva, por fim, o novo arquivo
		teste.to_csv("./teste-novo-tabula-" + dia + "-" + mes + "-17.csv", index=False)


if __name__ == '__main__':
	main()
