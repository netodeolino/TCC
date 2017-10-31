# -*- coding: UTF-8 -*-
from PDFtoCSV import Tabula

if __name__ == '__main__':
	wrp = Tabula()
	wrp.convert(["data"], False)
	#wrp.convert(["08-abr-17", "09-abr-17"])