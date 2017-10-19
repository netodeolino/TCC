# -*- coding: UTF-8 -*-
import pandas

class ExtratorBairro(object):
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


	def tirarEspacosDoInicio(self, string, inicio):
		
		inicioDaString = inicio
		if (string[inicioDaString] == " "):
			while (string[inicioDaString] == " "):
				inicioDaString = inicioDaString + 1
		return inicioDaString


	def extrairBairro(self, dataFrame, dataFrameOriginal):
		dataFrame = dataFrame.drop('FONTE', 1)
		dataFrame = dataFrame.drop('NATUREZA DA OCORRÊNCIA', 1)
		dataFrame = dataFrame.drop('HISTÓRICO DA OCORRÊNCIA', 1)
		dataFrame = dataFrame.drop('SUSPEITO:', 1)
		dataFrame = dataFrame.drop('VEÍCULO:', 1)
		dataFrame = dataFrame.drop('VÍTIMA:', 1)
		dataFrame = dataFrame.drop('VÍTIMAS:', 1)
		dataFrame = dataFrame.drop('VÍTIMA FATAL:', 1)
		dataFrame = dataFrame.drop('ARMA APREENDIDA:', 1)
		dataFrame = dataFrame.drop('MATERIAL APREENDIDO:', 1)
		dataFrame = dataFrame.drop('PLACA:', 1)
		dataFrame = dataFrame.drop('VÍTIMAS LESIONADAS:', 1)
		dataFrame = dataFrame.drop('SUSPEITOS:', 1)
		dataFrame = dataFrame.drop('HORARIO', 1)
		dataFrame = dataFrame.drop('DATA', 1)

		listaHorario = []
		arrayLinhaHorario = []
		array = []

		# - Salva em 'lista' as linhas de NATUREZA DA OCORRÊNCIA
		for i, row in dataFrame.iterrows():
			if row['LOCAL:']:
				listaHorario.append(dataFrame.loc[i,:])

		# - Salva em 'arrayLinhaHorario' o conteúdo das linhas de 'listaHorario'
		for k in listaHorario:
			arrayLinhaHorario.append(k.values)
			#print (k.values)

		t = 0
		while t < len(arrayLinhaHorario):
			stringLinha = self.transformaArrayEmString(arrayLinhaHorario[t])
			inicio = stringLinha.find(',')+1
			inicio = self.tirarEspacosDoInicio(stringLinha, inicio)

			aux = ""
		
			i = inicio;
			while i < len(stringLinha):
				if (stringLinha[i] != "."):
					aux += stringLinha[i]
				i += 1
			array.append(aux)
			t += 1

		dataFrameOriginal["BAIRRO"] = pandas.Series(array)


	def main(self):

		# - Valores para agilizar no processo de ler vários .CSV's por vez
		mes = "jan"
		listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
					"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

		for dia in listDiasMes:
			dataFrameInicial = pandas.read_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv")
			dataFrameOriginal = dataFrameInicial.copy()
			
			self.extrairBairro(dataFrameInicial, dataFrameOriginal)

			# - Última etapa, salvar todas as alterações realizadas em novos arquivos CSVs
			dataFrameOriginal.to_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv", index=False)


if __name__ == '__main__':
	extract = ExtratorBairro()
	extract.main()


# ------------------ Teste e Debug -------------------------------
