# -*- coding: UTF-8 -*-
import numpy as np
import pandas

class Grupo(object):
	def __init__(self):
		self.arrayDeFrames = []
		self.ENTIDADE_VAZIA = "null"


	def removerEntidadesVazias(self, dataFrame):
		return dataFrame[dataFrame.LATITUDE.astype(str) != self.ENTIDADE_VAZIA]


	def main(self):

		# - Valores para agilizar no processo de ler vários .CSV's por vez
		mes = "jan"
		listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
					"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

		for dia in listDiasMes:
			dataFrame = pandas.read_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv")
			
			# - Remover LATITUDE/LOGINTUDE nulos
			dataFrame = self.removerEntidadesVazias(dataFrame)

			self.arrayDeFrames.append(dataFrame)

		novoDataFrame = pandas.concat(self.arrayDeFrames)

		# Cria o indice e preenche (ID)
		novoDataFrame['ID'] = range(1, len(novoDataFrame) + 1)

		# Reestrutura as colunas
		novoDataFrame = novoDataFrame[['ID', 'FONTE', 'NATUREZA DA OCORRÊNCIA', 'HISTÓRICO DA OCORRÊNCIA', 'LOCAL:', 'SUSPEITO:',
				'VEÍCULO:', 'VÍTIMA:', 'VÍTIMAS:', 'VÍTIMA FATAL:', 'ARMA APREENDIDA:', 'MATERIAL APREENDIDO:',
				'PLACA:', 'VÍTIMAS LESIONADAS:', 'SUSPEITOS:', 'HORARIO', 'DATA', 'LATITUDE', 'LONGITUDE']]

		# - Salva frame
		novoDataFrame.to_csv("./"+mes+"-crimes.csv", index=False)


if __name__ == '__main__':
	grupo = Grupo()
	grupo.main()