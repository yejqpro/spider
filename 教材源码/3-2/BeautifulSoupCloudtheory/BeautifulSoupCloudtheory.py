import requests
def getHTML(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    text=response.text
    return text

import bs4
titleList=[]
dateList=[]
contentList=[]
def parser(text):
    soup=bs4.BeautifulSoup(text,"html.parser")
    # 定位都所有的云说标题节点
    title=soup.find_all("span",attrs={"class":"news-list-item-title"})
    # 遍历节点获取节点包含内容
    for i in title:
        titleList.append(i.string)
    # 定位都所有的发布时间节点
    date=soup.find_all("span",attrs={"class":"date"})
    # 遍历节点获取节点包含内容
    for i in date:
        dateList.append(i.string)
    # 定位都所有的云说内容节点
    content=soup.select('div[class="item-right-bottom"] p')
    # 遍历节点获取节点包含内容
    for i in content:
        contentList.append(i.string)
    # 获取下一页区域倒数第二个a标签
    pages=soup.select('ul[class="pagination"] li:nth-last-child(2) a')[0]
    # 获取a标签包含内容
    NextPage=pages.string
    # 判断是否存储”»下一页“
    if NextPage=="»下一页":
        # 如果存在则获取a标签的href路径
        page=pages.attrs['href']
        # 组成完整路径
        url="https://cloud.inspur.com"+page
        # 调用页面获取函数getHTML
        Nexthtml=getHTML(url)
        # 调用文档解析与数据提取函数parser
        parser(Nexthtml)

import csv
if __name__=='__main__':
    # 浪潮云说页面地址
    url = 'https://cloud.inspur.com/1635/'
    text = getHTML(url)
    parser(text)
    # 创建并以追加的方式打开文件
    f=open("Cloudtheory.csv","a",encoding="utf-8",newline="")
    # 构建CSV写入对象
    csv_writer = csv.writer(f)
    for i in range(0, len(titleList)):
        print(i)
        # 数据写入
        csv_writer.writerow([titleList[i], dateList[i], contentList[i]])
    # 关闭文件
    f.close()