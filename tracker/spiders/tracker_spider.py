import scrapy
import re
from ..items import TrackerItem


class TrackerSpiderSpider(scrapy.Spider):
    name = 'tracker_spider'
    allowed_domains = ['amazon.com']
    search_term = input("Enter Keyword to scrap: ")
    start_urls = [f'https://www.amazon.in/s?k={search_term}']

    def parse(self, response):
        items = TrackerItem()

        product_title = response.css('.a-color-base.a-text-normal::text').extract()
        product_total_number_rating = response.css('.a-size-small .a-size-base::text').extract()
        product_price = response.css('.a-price-whole::text').extract()
        product_image_link = response.css('.s-image::attr(src)').extract()

        for i in range(len(product_title)):
            try:
                items['product_title'] = product_title[i].strip()

                if product_total_number_rating[i]:
                    items['product_total_number_rating'] = product_total_number_rating[i].strip()

                else:
                    items['product_total_number_rating'] = 0

                if product_price[i]:
                    items['product_price'] = product_price[i].strip()
                else:
                    items['product_price'] = 0

                items['product_image_link'] = product_image_link[i].strip()

            except IndexError:
                pass
            yield items

