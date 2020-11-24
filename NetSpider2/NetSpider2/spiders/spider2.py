import scrapy


class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    # allowed_domains = ['huoche.8684.cn']
    start_urls = ['https://huoche.8684.cn/h_G588']

    def parse(self, response):
        # div_list = response.xpath('/html/body/div[6]/div[3]/div[1]/div[1]/div')
        p_list = response.xpath('/html/body//div[@class="depth"]/div[3]/div[1]/div[1]/div[1]/p')
        div_list = response.xpath('/html/body//div[@class="depth"]/div[3]/div[1]/div[1]/div[1]/div')
        print(p_list)
