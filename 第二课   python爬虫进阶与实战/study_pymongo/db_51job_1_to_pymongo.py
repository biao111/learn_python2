import requests
import re
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://10.12.193.215:27017")
mydb = myclient['db_51job']
mycollection = mydb['collection_51job']

# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}

# 请求url
url = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html"

# 请求51job
response = requests.get(url=url, headers=header)

# 正则表达式
re_job_info_search = re.compile(r"window\.__SEARCH_RESULT__\s=\s(.*?)</script>")

# 正则匹配返回数据
job_data = re_job_info_search.search(response.text)
if job_data:
    # 获取岗位数据
    job_data_list = json.loads(job_data.group(1)).get("engine_search_result")
    for job_item in job_data_list:
        print(job_item)

mycollection.insert_many(job_data)
result = mycollection.find()
for item in result:
    print(item)