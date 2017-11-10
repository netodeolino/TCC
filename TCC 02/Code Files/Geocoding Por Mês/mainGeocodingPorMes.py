# -*- coding: UTF-8 -*-

from geocodingPorMes import GeocodingAPI

if __name__ == '__main__':
	geoAPI = GeocodingAPI()
	geoAPI.main(["novo-tabula-01-jan-17", "novo-tabula-02-jan-17", "novo-tabula-03-jan-17"], "LOCAL:")