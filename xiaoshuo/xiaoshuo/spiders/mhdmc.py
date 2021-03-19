import scrapy


class MhdmcSpider(scrapy.Spider):
    name = 'mhdmc'
    allowed_domains = ['81zw.com']
    # start_urls = ['https://www.81zw.com/book/45056/19947407.html']
    start_urls = ['https://www.81zw.com/book/45056/19947407.html']

    def parse(self, response):
        try:
            title = response.xpath('//h1/text()').extract_first()
            # content = response.xpath('//div[@id="content"]/text()').extract()  #使用extract() 返回的时list 类型
            content = ''.join(
                (response.xpath('//div[@id="content"]/text()').extract()
                 )) # ''.join() 将 list 转为 str 类型， 这个要常用 , 熟记

            # print(type(content))
            # 推送 内容和 Pipline, 进行文件的保存
            yield {'title': title, 'content': content}

            # 下一章的URL
            new_url = response.xpath(
                '//div[@class="bottem1"]/a[3]/@href').extract_first()
            basr_url = 'https://www.81zw.com' + new_url
            # 响应, 使用 在下载器中的 Request模块，callable = self.parse ：表示使用parse 进行解析
            if basr_url.find('.html') != -1: # 判断尾页
                yield scrapy.Request(basr_url, callback=self.parse)
        except:
            pass

        pass
