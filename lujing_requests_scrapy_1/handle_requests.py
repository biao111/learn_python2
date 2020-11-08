import requests

# # #get请求数据，requests.get,url传入
# response = requests.get(url="http://www.qq.com")
# print(response.text)

#post方法
#构造发送的数据，字典的格式
# data = {"name":"imooc"}
# #发送的是post请求，data关键字，data参数
# response = requests.post("http://httpbin.org/post",data=data)
# print(response.text)

# data = {"key1":"value1","key2":"value2"}
# response = requests.get("http://httpbin.org/get",params=data)
# 返回url
# print(response.url)
#返回url header
# print(response.headers)
#返回url体
#print(response.text)

#返回图片
# response = requests.get("https://www.imooc.com/static/img/index/logo.png")
# with open("imooc.png","wb") as f:
#     f.write(response.content)


# #自定义请求头
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
# }
# #返回json格式
# response = requests.get("http://httpbin.org/ip",headers=header)
# #状态码,200正常
# # print(response.status_code)
# # data = response.json()
# # print(data)
# # print(data["origin"])
# #返回：返回头
# print(response.headers)
# #返回：请求头
# print(response.request.headers)

#请求超时,如果时间超时，会报timeout错误
# response = requests.get("http://www.github.com",timeout=2)
# print(response.text)

# 请求cookies
# url = "https://www.baidu.com"
# #定制请求头，使用标准的浏览器UA
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
# }
# response = requests.get(url=url,headers=header)
# print(response.cookies)
# print(response.cookies["BAIDUID"])

# 设置cookies
#可以查看当前cookies的url
url = "http://httpbin.org/cookies"
# cookies = dict(cookies_are="hello imooc")
#使用字典构造了cookies
cookies = {"cookies":"hello"}
response = requests.get(url=url,cookies=cookies)
print(response.text)
