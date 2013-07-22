from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from football.items import FootballItem

class RFSpider(BaseSpider):
    name = "rf"
    allowed_domains = ["resultados-futbol.com"]
    start_urls = [
        "http://www.resultados-futbol.com/primera2013/grupo1/jornada1"
        ]
    
    def parse(self, response):
#        filename = response.url.split("/")[-1]
#        open(filename, 'wb').write(response.body)
        hxs = HtmlXPathSelector(response)
        matches = hxs.select('//div[@id="col-resultados"]//tr')
        items = []
        for match in matches:
            item = FootballItem()
            item['home'] = match.select('td[@class="equipo1"]//text()').extract()
            item['visitor'] = match.select('td[@class="equipo2"]//text()').extract()
            item['date'] = match.select('td[@class="fecha"]//text()').extract()
            item['result'] = match.select('td[@class="rstd"]//a//text()').extract()
            items.append(item)
#            print item

        return items
