import requests
def getHTML(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    text=response.text
    return text
if __name__=='__main__':
    # 浪潮云说页面地址
    url = 'https://cloud.inspur.com/1635/'
    text = getHTML(url)
    print(text)