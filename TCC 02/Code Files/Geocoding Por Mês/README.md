## SSPDS e Outros Dados
	- Ao chamar o método "main()" deve ser passado para o mesmo a lista de arquivos e o nome da
	coluna que contém os dados de endereço para ser encontrado suas respectivas latitudes e longitudes.

## Requisitos
* [Python 3.5](https://www.python.org/downloads/release/python-350/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)

### Como executar
No terminal e na pasta onde estão os arquivos execute o comando:
```
python3.5 mainGeocodingPorMes.py
```

### Duração do Geocoding
A API tem um limite de 10 requisições por segundo. Portanto, o tempo de processamento dos dados
dependerá da quantidade de arquivos e linhas por arquivo você possui.
