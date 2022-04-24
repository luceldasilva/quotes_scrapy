from gc import callbacks
from sys import getallocatedblocks
import scrapy

## next page button = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    custom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            },
        },
    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes':quotes})
        else:
            yield {
                'quotes': quotes
            }

    def parse(self, response):

        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()'
            ).getall()
        ranking = response.xpath(
            '//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()'
            ).getall()

        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            ranking = ranking[:top]

        yield {
            'title': title,
            'top_tags': ranking
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes':quotes})