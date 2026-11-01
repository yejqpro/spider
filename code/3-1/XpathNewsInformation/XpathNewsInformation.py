from urllib import request
from urllib import error

def getHTML(url):
    try:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
        # 抓取设置
        htmlurl = request.Request(url, headers=header)
        # 提交请求
        reponse = request.urlopen(htmlurl)
        # 读取结果
        html = reponse.read().decode("utf-8")
    #URL 异常处理
    except error.URLError as e:
        # 获取错误原因
        print (e.reason)
    # 返回页面内容
    return (html)

from lxml import etree
import csv
def parser(htmlpage):
    html=etree.HTML(htmlpage)
    NewsList=html.xpath("//div[@class='news-list']/div[@class='news-list-item']")
    # 创建并以追加的方式打开文件
    f=open("NewsInformation.csv","a",encoding="utf-8",newline="")
    for new in NewsList:
        # 获取新闻图片链接
        url = new.xpath("./div[@class='news-list-item-left']/a/img/@src")[0]
        imgUrl = "https://cloud.inspur.com"+url
        print('新闻图片链接：',imgUrl)
        # 获取新闻标题
        title = new.xpath("./div[@class='news-list-item-right']/div[@class='item-right-top']/a/span[@class='news-list-item-title']/text()")[0]
        print('新闻标题：',title)
        # 获取新闻简介
        context = new.xpath("./div[@class='news-list-item-right']/div[@class='item-right-bottom']/p/text()")[0]
        print('新闻简介：', context)
        # 获取发布时间
        date = new.xpath("./div[@class='news-list-item-right']/div[@class='item-right-top']/a/span[@class='date']/text()")[0]
        print('发布时间：', date)
        print('------------------------------')
        # 构建CSV写入对象
        csv_writer=csv.writer(f)
        # 数据写入
        csv_writer.writerow([imgUrl,title,context,date])
    # 关闭文件
    f.close()
    # 获取倒数第二个li标签
    pages=html.xpath("//div[@class='mainbody_page']/ul[@class='pagination']/li[last()-1]")[0]
    # 获取a标签包含文本
    NextPage=pages.xpath("./a/text()")[0]
    # 判断是否存在”»下一页“
    if NextPage=="»下一页":
        # 如果存在，则获取a标签中的href属性值
        page=pages.xpath("./a/@href")[0]
        # 组成下一页的访问路径
        url="https://cloud.inspur.com"+page
        # 调用getHTML函数访问页面获取页面内容
        Nexthtml=getHTML(url)
        # 调用parser函数解析页面内容并提取数据
        parser(Nexthtml)
if __name__=='__main__':
    # 接收页面的URL获取页面内容
    htmlpage = getHTML("https://cloud.inspur.com/news-update/")
    # 解析HTML文档提取数据
    parser(htmlpage)