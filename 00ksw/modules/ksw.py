import requests
from lxml import etree

class ksw:
    "ksw爬虫操作类"

    def request(url):
        req = requests.get(url)
        req.encoding = "gbk"
        return req.text

    #获取小说列表
    def getlist(url):
        str=ksw.request(url)
        ele = etree.HTML(str)
        href = ele.xpath('//div[1]/div[3]/ul/li/a')
        kswUrl=[]
        for x in href:
            kswUrl.append( "%s%s" %(url[:21] ,x.attrib["href"]))
        return kswUrl

    #获取小说正文
    def getContent(url):
        str=ksw.request(url)
        ele = etree.HTML(str)
        div = ele.xpath('//*[@id="articlecontent"]/p/text()')
        title = ele.xpath('//*[@class="nr_title"]/h3/text()')
        return {
            "title":title[0],
            "text":"\r\n".join(div)
        }