# -*- coding: UTF-8 -*-
import pandas
import requests

class GeocodingAPI(object):
	def __init__(self):
		self.ENTITY_NULL = "nulo"


	# - Recebe uma string endereço e retorna a longitude e latitude da mesma
	def geocodingLocal(self, local, cidade):
		endereco = str(local)

		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + endereco + " " + cidade)
		resp_json_payload = response.json()

		try:
			longitude = resp_json_payload['results'][0]['geometry']['location']['lng']
			latitude = resp_json_payload['results'][0]['geometry']['location']['lat']

			return (longitude, latitude)
		except Exception as e:
			return (self.ENTITY_NULL, self.ENTITY_NULL)


	# - Função principal
	def main(self, files, column):

		# Variável para deixar a busca mais precisa
		cidade = input("Digite o nome da cidade ou estado ao qual os dados serão buscados!\n")

		for file in files:
			dataFrameInicial = pandas.read_csv("./data/" + file + ".csv")

			novoFrame = dataFrameInicial[column]
			listaLongitude = []
			listaLatitude = []

			a = 0
			while a < len(novoFrame):
				longitude, latitude = self.geocodingLocal(novoFrame[a], cidade)
				
				listaLongitude.append(longitude)
				listaLatitude.append(latitude)
				a += 1

			dataFrameInicial["LATITUDE"] = pandas.Series(listaLatitude)
			dataFrameInicial["LONGITUDE"] = pandas.Series(listaLongitude)
			
			# - Salva, por fim, o novo arquivo
			dataFrameInicial.to_csv("./data/" + file + ".csv", index=False)
