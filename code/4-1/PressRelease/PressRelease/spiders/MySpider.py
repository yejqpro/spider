import scrapy
# 从scrapy.selector中导入Selector
from scrapy.selector import Selector
# 导入items.py文件中定义的类
from PressRelease.items import PressreleaseItem
class MyspiderSpider(scrapy.Spider):
    name = 'MySpider'
    allowed_domains = ['www.inspur.com']
    start_urls = ['https://www.inspur.com/lcjtww/445068/445237/']
    def parse(self, response):
        # 构造Selector实例
        sel = Selector(response)
        # 构造Item容器对象
        item = PressreleaseItem()
        # 新闻标题
        item["title"] = sel.xpath('//div[@class="g_anno2_lifl fl"]/h5/text() | //div[@class="g_anno2bot_li"]/a[@class="clearfix"]/div[@class="g_anno2bot_lifl fl"]/h4/text()').extract()
        print(item["title"])
        # 新闻内容
        item["content"] = sel.xpath('//div[@class="g_anno2_lifl fl"]/p/text() | //div[@class="g_anno2bot_li"]/a[@class="clearfix"]/div[@class="g_anno2bot_lifl fl"]/p/text()').extract()
        print(item["content"])
        # 新闻链接
        item["url"] = sel.css('a.clearfix::attr(href)').extract()
        print(item["url"])
        # 新闻日期
        smDate = []
        day = sel.css('p.smDate::text').extract()
        for i in day:
            smDate.append(i[5:])
        item["day"] = smDate
        print(item["day"])
        # 发布年份
        tsDate = []
        for i in day:
            tsDate.append(i[0:4])
        item["year"] = tsDate
        print(item["year"])
        # 交给管道文件
        yield item

        # 获取下一页的url地址
        next_url = sel.css('div.Pagination_x a.Pagination_sa::attr(tagname)').extract_first()
        # 判断若不是最后一页
        if next_url!="[NEXTPAGE]":
            # 构造下一页url
            url="https://www.inspur.com"+next_url
            # 构造下一页招聘列表信息的爬取
            yield scrapy.Request(url=url, callback=self.parse)