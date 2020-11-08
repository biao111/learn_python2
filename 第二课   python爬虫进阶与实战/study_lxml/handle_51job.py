import requests
from lxml import etree
import json

#使我们要请求的URL，地点为北京，岗位包含python的所有岗位,第一页数据
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html'

#里面有空格，要处理一下
header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"Host":"search.51job.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36",
}

response = requests.get(url=url,headers=header)
response.encoding = 'gbk'
# print(response.text)
html_51job = etree.HTML(response.text)
#单引号双引号要注意
all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
info_list = []
for item in all_div:
    info = {}
    #这个.非常的重要，代表我们使用的是item下的xpath语句,不要把.丢了
    #获取数据的时候，要使用列表索引为0的数据
    info['job_name'] = item.xpath("./p/span/a/@title")[0]
    info['company_name'] = item.xpath(".//span[@class='t2']/a/@title")[0]
    #把下面这三个字段补齐
    # info['company_address']
    # info['money']
    # info['date']
    info_list.append(info)
print(json.dumps(info_list))
