import scrapy
from proxies_parser.items import ProxiesParserItem
from scrapy_splash import SplashRequest


class ProxySpider(scrapy.Spider):
    name = "proxy"

    start_urls = [
        "http://spys.one/proxies/",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait': 5})

    def parse(self, response):
        rows = response.xpath('//tr/td[1]/font[@class="spy14"][1]')
        for row in rows:
            item = ProxiesParserItem()
            ip = row.re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
            if not ip:
                continue
            item['ip_address'] = ip[0]
            item['port'] = row.re('\d{1,}')[-1]
            yield item
