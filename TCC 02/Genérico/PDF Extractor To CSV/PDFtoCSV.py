# -*- coding: UTF-8 -*-
from tabula import convert_into

class Tabula(object):

	def convert(self, files, SSPDS=True):
		for file in files:			
			# convert PDF into CSV
			if (SSPDS):
				convert_into(file+".pdf", "tabula-"+file+".csv", output_format="csv", lattice=True)
			else:
				convert_into(file+".pdf", "tabula-"+file+".csv", output_format="csv")
