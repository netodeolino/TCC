# -*- coding: UTF-8 -*-
import numpy as np
import pandas

arrayDeFrames = []


def main():

	# - Valores para agilizar no processo de ler vários .CSV's por vez
	mes = "jan"
	listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
				"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

	for dia in listDiasMes:
		dataFrame = pandas.read_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv")
		
		arrayDeFrames.append(dataFrame)

	result = pandas.concat(arrayDeFrames)
	result.to_csv("./janeiro-crimes.csv", index=False)

if __name__ == '__main__':
	main()