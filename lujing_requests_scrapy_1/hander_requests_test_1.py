import requests

#用get方法传入
# response = requests.get("http://httpbin.org/ip")
# print(response.text)

#用post方法传入
# data = {"name":"imooc"}
# response = requests.post("http://httpbin.org/post",data=data)
# print(response.text)

#用get访华获取url、请求头
# params = {
#     "key_1":"value1",
#     "key_2":"value2"
# }
# response = requests.get("http://httpbin.org/get",params=params)
# print(response.url)
# print(response.headers)
# print(response.request.headers)

#用get方法获取图片
# response = requests.get("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")
# with open("baidu.png","wb") as f:
#     f.write(response.content)

#用get方法获取json
# response = requests.get("http://httpbin.org/ip")
# data = response.json()
# print(data)

#用get方法获取返回头，请求头（自定义请求头）
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
response = requests.get("http://httpbin.org",headers = header)
print(response.request.headers)