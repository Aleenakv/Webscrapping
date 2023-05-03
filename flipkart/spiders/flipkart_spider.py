import scrapy
from ..items import FlipkartItem

class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    start_urls = ['https://www.flipkart.com/adrenex-flipkart-big-bang-6-inch-x-26-5-skateboard/p/itmdcbb9d36e4198?pid=SKDFPMH7SAMXCSHY&lid=LSTSKDFPMH7SAMXCSHY0OC6GA&marketplace=FLIPKART&store=abc%2Fmgq&srno=b_1_21&otracker=browse&fm=organic&iid=6e9eeaf9-6b9c-4aa1-862d-96fa0fb210dc.SKDFPMH7SAMXCSHY.SEARCH&ppt=browse&ppn=browse']

    def parse(self, response):
        items = FlipkartItem()

        product_name = response.css('.B_NuCI').css('::text').extract()[0]
        product_description = response.css('._2cM9lP').css('::text').extract()
        product_price = response.css('._16Jk6d').css('::text').extract()[0]
        product_rating = response.css('._2_R_DZ span span:nth-child(1)').css('::text').extract()[0]


        items['product_name'] = product_name
        items['product_description'] = product_description
        items['product_price'] = product_price
        items['product_rating'] = product_rating


        yield items