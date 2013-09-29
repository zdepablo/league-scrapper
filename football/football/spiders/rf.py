from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from football.items import FootballItem

class RFSpider(CrawlSpider):
    name = "rf"
    allowed_domains = ["resultados-futbol.com"]
    start_urls = [
        "http://www.resultados-futbol.com/premier2013/grupo1/jornada1"
        ]
    
    rules = (
        Rule(SgmlLinkExtractor(allow=('jornada*', )), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('jornada*', ) )),
    )


    def parse_item(self, response):
#        filename = response.url.split("/")[-1]
#        open(filename, 'wb').write(response.body)
        hxs = HtmlXPathSelector(response)
        matches = hxs.select('//table[@id="tabla1"]//tr')
        round = hxs.select('//div[@id="col-resultados"]//ul/li/a/text()').extract();
        season = hxs.select('//div[@id="titular"]//div[@class="titular-data"]//small[@class="temp"]/text()').extract();
        league = hxs.select('//div[@id="titular"]//div[@class="titular-data"]//h1/text()').extract()
        items = []
        for match in matches:
            item = FootballItem()
            item['league']  = league
            item['season']  = season
            item['round']   = round
            item['home']    = match.select('td[@class="equipo1"]//a//text()').extract()
            item['visitor'] = match.select('td[@class="equipo2"]//a//text()').extract()
            item['date']    = match.select('td[@class="rstd"]//span[@class="dtstart"]/@title').extract()
            item['result']  = match.select('td[@class="rstd"]//a//text()').extract()
            items.append(item)
#            print item

        return items
