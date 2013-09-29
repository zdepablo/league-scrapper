# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FootballItem(Item):
    # define the fields for your item here like:
    league = Field()
    season = Field()
    round = Field()    
    home = Field()
    visitor = Field()
    result = Field()
    date = Field()
    pass
