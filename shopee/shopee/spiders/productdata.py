import scrapy


class ProductdataSpider(scrapy.Spider):
    name = "productdata"
    # allowed_domains = ["s"]
    start_urls = ["http://s/"]

    def parse(self, response):
        pass
