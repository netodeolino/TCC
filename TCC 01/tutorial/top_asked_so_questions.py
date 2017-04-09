import scrapy
import urllib.parse
 
class Question(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    excerpt = scrapy.Field()
    tags = scrapy.Field()
 
class StackoverflowTopQuestionsSpider(scrapy.Spider):
    name = 'so-top-questions'
 
    def __init__(self, tag=None):
        questions_url = 'http://pt.stackoverflow.com/questions'
        if tag:
            questions_url += '/tagged/%s' % tag
 
        self.start_urls = [questions_url + '?sort=frequent']
 
    def parse(self, response):
        build_full_url = lambda link: urllib.parse.urljoin(response.url, link)
 
        for qsel in response.css("#questions > div"):
            it = Question()
 
            it['link'] = build_full_url(
                qsel.css('.summary h3 > a').xpath('@href')[0].extract())
            it['title'] = qsel.css('.summary h3 &amp;amp;amp;gt; a::text')[0].extract()
            it['tags'] = qsel.css('a.post-tag::text').extract()
            it['excerpt'] = qsel.css('div.excerpt::text')[0].extract()
 
            yield it
