# -*- coding: UTF-8 -*-
import numpy as np
import pandas
import requests

ENTIDADE_VAZIA = "NÃO POSSUI ESSA INFORMAÇÃO"

# - Recebe uma string endereço e retorna a longitude e latitude da mesma
def geocodingLocal(local):
	endereco = local

	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + endereco)
	resp_json_payload = response.json()

	try:
		longitude = resp_json_payload['results'][0]['geometry']['location']['lng']
		latitude = resp_json_payload['results'][0]['geometry']['location']['lat']

		return (longitude, latitude)
	except Exception as e:
		return (ENTIDADE_VAZIA, ENTIDADE_VAZIA)


# - Função principal
def main():
	# - Valores para agilizar no processo de ler vários .CSV's por vez
	mes = "jan"
	listDiasMes = ["01", "02", "03", "04", "05", "06", "07", "08", "10", "12", "14", "15", "16", "17", "19", "20",
					"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
				]

	for dia in listDiasMes:
		dataFrameInicial = pandas.read_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv")

		novoFrame = dataFrameInicial["LOCAL:"]
		listaLongitude = []
		listaLatitude = []

		a = 0
		while a < len(novoFrame):
			longitude, latitude = geocodingLocal(novoFrame[a])
			
			listaLongitude.append(longitude)
			listaLatitude.append(latitude)
			a += 1

		dataFrameInicial["LONGITUDE"] = pandas.Series(listaLongitude)
		dataFrameInicial["LATITUDE"] = pandas.Series(listaLatitude)

		# - Salva, por fim, o novo arquivo
		dataFrameInicial.to_csv("./novo-tabula-" + dia + "-" + mes + "-17.csv")


if __name__ == '__main__':
	main()