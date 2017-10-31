# -*- coding: UTF-8 -*-
from tabula import read_pdf
from tabula import convert_into

class Tabula(object):

	def convert(self, files, SSPDS=True):
		for file in files:
			if (SSPDS):
				dataFrame = read_pdf(file+".pdf", lattice=True, pages=1)
				
				if dataFrame.columns[0] == "FORTALEZA":
					dataFrame.columns = ["FONTE", "NATUREZA DA OCORRÊNCIA", "HISTÓRICO DA OCORRÊNCIA"]
					dataFrame.drop(0, inplace=True)
					try:
						t, = dataFrame.index[dataFrame["FONTE"] == "REGIÃO METROPOLITANA"]
						dataFrame = dataFrame.drop(dataFrame.index[t-1:])
					except Exception as e:
						print ("")
				
				if dataFrame.columns[0] != "FORTALEZA" and dataFrame.columns[0] != "FONTE":
					dataFrame.columns = ["FONTE", "NATUREZA DA OCORRÊNCIA", "HISTÓRICO DA OCORRÊNCIA"]
					dataFrame.drop(0, inplace=True)
					dataFrame.drop(1, inplace=True)
					try:
						t, = dataFrame.index[dataFrame["FONTE"] == "REGIÃO METROPOLITANA"]
						dataFrame = dataFrame.drop(dataFrame.index[t-2:])
					except Exception as e:
						print ("")

				dataFrame.to_csv("./tabula-"+file+".csv", index=False)
			else:
				convert_into(file+".pdf", "tabula-"+file+".csv", output_format="csv")
