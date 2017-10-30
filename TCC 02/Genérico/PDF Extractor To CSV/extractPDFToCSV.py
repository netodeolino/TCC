# -*- coding: UTF-8 -*-
from tabula import convert_into

class Wrapper(object):

	def main(self, fileName, newFileName):
		# convert PDF into CSV
		convert_into(fileName+".pdf", newFileName+".csv", output_format="csv", lattice=True)

if __name__ == '__main__':
	wrp = Wrapper()
	wrp.main("01-abr-17", "output")