import scrapy
import re
from ..items import TrackerItem


class TrackerSpiderSpider(scrapy.Spider):
    name = 'tracker_spider'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/gp/product/B07XVMDRZY/ref=s9_acss_bw_cg_Budget_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=K1GJZ6HJCPQ90MCHDS0P&pf_rd_t=101&pf_rd_p=ac3235bd-aa25-433c-b15a-07f0f2c7eb2e&pf_rd_i=1389401031']

    def parse(self, response):
        items = TrackerItem()

        product_name = response.css('#productTitle::text').extract()
        product_sold_by = response.css('#sellerProfileTriggerId::text').extract()
        product_price = response.css('#priceblock_dealprice::text').extract()
        product_image_link = response.css('#landingImage').extract()
        text = str(product_image_link)
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        items['product_name'] = product_name
        items['product_sold_by'] = product_sold_by
        items['product_price'] = product_price
        items['product_image_link'] = urls

        yield items

