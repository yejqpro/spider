# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
class PressreleasePipeline:
    # 初始化
    def __init__(self):
        # 连接MySQL数据库
        self.connect=pymysql.connect(host="192.168.0.136", user="root", password="123456", database="mysql", charset='utf8')
        # 创建游标
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        # 容错处理
        title = item.get("title", "N/A")
        content = item.get("content", "N/A")
        day = item.get("day", "N/A")
        year = item.get("year", "N/A")
        url = item.get("url", "N/A")
        # 遍历数据
        for i in range(int(len(title))):
            print(int(len(content)))
            print(int(len(day)))
            print(int(len(year)))
            print(int(len(url)))
            print(i)
            # 插入数据
            sql = "insert into press_release(title,content,day,year,url) values(%s,%s,%s,%s,%s) ON duplicate KEY UPDATE title = title "
            self.cursor.execute(sql, (title[i], content[i], day[i], year[i], url[i]))
            # 提交sql语句
            self.connect.commit()
        return item
    def close_spider(self, spider):
        # 关闭数据库连接
        self.connect.close()
        print("数据库连接已关闭！")