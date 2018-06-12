import scrapy

from targetmol_lib.items import TML_Item

class Targetmol_lib(scrapy.Spider):
    name = 'TML_lib_scr'  # Spiderの名前。
    # クロールを開始するURLのリスト。
    start_urls = ['http://www.targetmol.com/']

    def parse(self, response):
        """
        トップページからカテゴリページへのリンクを抜き出してたどる。
        """
        for url in response.css('ul li a::attr("href")').re('.*/screening2/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        """
        トップページからライブラリのページに飛び、タイトル、カタログ番号、製品詳細を抜き出す。
        """
        item = TML_Item() 
        item['catno'] = response.css('div.lbytitle > span::text').extract() # カタログ番号
        item['title'] = response.css('div.lbytitle::text').extract_first().replace(" \xa0", "") # タイトル
        item['description'] = response.css('div.lbydspt::text').extract() #製品詳細
        yield item

