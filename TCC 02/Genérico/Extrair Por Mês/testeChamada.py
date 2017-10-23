# -*- coding: UTF-8 -*-
from extrairUmMes import Extract

def yourMethodExtractExample(string, ini=0):
	text = ""
	i = ini;

	while i < len(string):
		if (string[i] != " "):
			text += string[i]
		if (string[i] == " "):
			break
		i += 1

	return text

#exct = Extract(["BIBLIOTECA", "Biblioteca"])
#exct.main(["biblioteca-detalhado"], "Nome biblioteca", yourMethodExtractExample)
exct = Extract(["LOCAL:", "VÍTIMA:"])
exct.main(["tabula-01-jan-17", "tabula-02-jan-17", "tabula-03-jan-17"])
