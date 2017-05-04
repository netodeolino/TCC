'''
	Neto Deolino, Sistemas de Informação, UFC-Quixadá
'''

import scrapy

class ImprimeMan():
    def __init__(self):
        self.titulo = ""
        self.subtitulo = ""
        self.info = ""
        self.texto = ""

class QuotesSpider(scrapy.Spider):

    imp = ImprimeMan()

    name = "diario"

    start_urls = [
        'http://diariodonordeste.verdesmares.com.br/cadernos/policia',
    ]

    def parse(self, response):
        for quote in response.css('section.listagem article.item'):
            self.imp.info = quote.css('div.info p::text').extract()
            self.imp.titulo = quote.css('h1.title a::text').extract_first()
            self.imp.subtitulo = quote.css('p.subtitle::text').extract_first()

            next_page = quote.css('h1.title a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse2)


    def parse2(self, response2):
        for quote2 in response2.css('article.content-noticia'):
            yield {
                'texto': quote2.css('p::text').extract(),
                'info': self.imp.info,
                'titulo': self.imp.titulo,
                'subtitulo': self.imp.subtitulo,
            }
            

