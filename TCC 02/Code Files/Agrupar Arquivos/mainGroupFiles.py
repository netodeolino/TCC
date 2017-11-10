# -*- coding: UTF-8 -*-

from groupFiles import Group

if __name__ == '__main__':
	group = Group()
	#group.main(["novo-tabula-01-jan-17", "novo-tabula-02-jan-17", "novo-tabula-03-jan-17"], "crimes-de-janeiro")
	group.main(["crime_1", "crime_2"], "crime_1_and_2", False)