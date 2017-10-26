# -*- coding: UTF-8 -*-
from extractBairros import ExtractBairro

if __name__ == '__main__':
	extract = ExtractBairro()
	extract.main(["novo-tabula-01-jan-17", "novo-tabula-02-jan-17", "novo-tabula-03-jan-17"])