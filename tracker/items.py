import scrapy


class TrackerItem(scrapy.Item):
    product_title = scrapy.Field()
    product_total_number_rating = scrapy.Field()
    product_price = scrapy.Field()
    product_image_link = scrapy.Field()
