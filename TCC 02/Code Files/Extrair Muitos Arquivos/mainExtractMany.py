# -*- coding: UTF-8 -*-
from extractMany import Extract
from methodExtract import yourMethodExtractExample

if __name__ == '__main__':
	#-- External Methods --#
	#exct = Extract(["BIBLIOTECA", "Biblioteca"])
	#exct.main(["biblioteca-detalhado"], "Nome biblioteca", yourMethodExtractExample)

	#-- SSPDS --#
	exct = Extract([
					"LOCAL:", "SUSPEITO:", "VEÍCULO:", "VÍTIMA:", "VÍTIMAS:", "VÍTIMA FATAL:", "ARMA APREENDIDA:",
					"MATERIAL APREENDIDO:", "PLACA:", "VÍTIMAS LESIONADAS:", "SUSPEITOS:"
				  ])
	exct.main([
				"tabula-01-jan-17", "tabula-02-jan-17", "tabula-03-jan-17",
				"tabula-04-jan-17", "tabula-05-jan-17", "tabula-06-jan-17",
				"tabula-07-jan-17", "tabula-08-jan-17", "tabula-10-jan-17",
				"tabula-12-jan-17", "tabula-14-jan-17", "tabula-15-jan-17",
				"tabula-16-jan-17", "tabula-17-jan-17", "tabula-19-jan-17",
				"tabula-20-jan-17", "tabula-21-jan-17", "tabula-22-jan-17",
				"tabula-23-jan-17", "tabula-24-jan-17", "tabula-25-jan-17",
				"tabula-26-jan-17", "tabula-27-jan-17", "tabula-28-jan-17",
				"tabula-29-jan-17", "tabula-30-jan-17", "tabula-31-jan-17"
			])