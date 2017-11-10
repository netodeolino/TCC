## SSPDS
	- Extract recebe uma lista de entidades para serem extraídas. O texto é extraído desde a entidade
	até o primeiro ponto encontrado. Para usar outra regra de extração é necessário usar um outro método
	para a mesma.
## Outros Dados
	- Para outros dados o método "main()" deve receber, além da lista de arquivos a serem extraídos, o nome
	da coluna e o método com as regras de extração.
	- O método receberá como parâmetros uma string, referente a uma linha/coluna dos dados e a posição
	inicial do texto a partir da entidade repassada para o método "main()".

## Requisitos
* [Python 3.5](https://www.python.org/downloads/release/python-350/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)

### Como executar
No terminal e na pasta onde estão os arquivos execute o comando:
```
python3.5 mainExtractMany.py
```
