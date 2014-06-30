from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from football.items import FootballItem

class RFSpider(CrawlSpider):
    name = "rf"
    allowed_domains = ["resultados-futbol.com"]
    start_urls = [
#        "http://www.resultados-futbol.com/premier2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/premier2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/premier2005/grupo1/jornada1"  


#       "http://www.resultados-futbol.com/primera2014/grupo1/jornada1",
#       "http://www.resultados-futbol.com/primera2013/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2012/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2011/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2010/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2009/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2008/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2007/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2006/grupo1/jornada1",
#	"http://www.resultados-futbol.com/primera2005/grupo1/jornada1"  



#        "http://www.resultados-futbol.com/serie_a2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/serie_a2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/serie_a2005/grupo1/jornada1"  




#        "http://www.resultados-futbol.com/bundesliga2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/bundesliga2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/bundesliga2005/grupo1/jornada1"  




#        "http://www.resultados-futbol.com/ligue_12014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/ligue_12013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/ligue_12005/grupo1/jornada1"  





#        "http://www.resultados-futbol.com/portugal2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/portugal2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/portugal2005/grupo1/jornada1"  




#        "http://www.resultados-futbol.com/holanda2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/holanda2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/holanda2005/grupo1/jornada1"  




#        "http://www.resultados-futbol.com/turquia2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/turquia2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/turquia2005/grupo1/jornada1"  




#        "http://www.resultados-futbol.com/grecia2014/grupo1/jornada1",
#        "http://www.resultados-futbol.com/grecia2013/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2012/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2011/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2010/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2009/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2008/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2007/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2006/grupo1/jornada1",
#		"http://www.resultados-futbol.com/grecia2005/grupo1/jornada1"  



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
            #print item

        return items
