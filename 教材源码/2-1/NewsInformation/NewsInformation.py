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
if __name__=='__main__':
    # 接收页面的URL获取页面内容
    htmlpage=getHTML("https://cloud.inspur.com/news-update/")
    print(htmlpage)