# -*- coding: UTF-8 -*-
from extractMany import Extract
from methodExtract import yourMethodExtractExample

if __name__ == '__main__':
	#-- External Methods --#
	exct = Extract(["BIBLIOTECA", "Biblioteca"])
	exct.main(["biblioteca-detalhado"], "Nome biblioteca", yourMethodExtractExample)

	#-- SSPDS --#
	#exct = Extract(["LOCAL:", "VÍTIMA:"])
	#exct.main(["tabula-01-jan-17", "tabula-02-jan-17", "tabula-03-jan-17"])
