import scrapy

class Item():
    def __init__(self):
        self.titulo = ""
        self.subtitulo = ""
        self.info = ""
        self.texto = ""

class Imprime():

    def imprimir(self, lista):
        for l in lista:
            itemaqui = l


class QuotesSpider(scrapy.Spider):

    imprime = Imprime()
    item = Item()

    listaItem = []

    name = "diario"

    start_urls = [
        'http://diariodonordeste.verdesmares.com.br/cadernos/policia',
    ]

    def parse(self, response):
        for quote in response.css('section.listagem'):
            for test in quote.css('article.item'):
                self.item.info = quote.css('div.info p::text').extract()
                yield {
                    'info': self.item.info,
                }

            '''
            self.item.titulo = quote.css('h1.title a::text').extract()
            self.item.subtitulo = quote.css('p.subtitle::text').extract()

            
            texto_item = quote.css('h1.title a::attr(href)').extract_first()
            if texto_item is not None:
                texto_item = response.urljoin(texto_item)
                self.item.texto = scrapy.Request(texto_item, callback=self.parse2)
            '''

            '''self.listaItem.append(self.item)'''

        '''
        for it in self.listaItem:
            yield {
                'titulo': it.titulo,
                'subtitulo': it.subtitulo,
                'info': it.info,
                'texto': it.texto,
            }
        '''

    def parse2(self, response2):
        for quote2 in response2.css('article.content-noticia'):
            '''for mini_texto in quote2.css('p::text')'''
            listaParagrafo = []
            listaParagrafo.append(quote2.css('p::text').extract())

        return listaParagrafo

