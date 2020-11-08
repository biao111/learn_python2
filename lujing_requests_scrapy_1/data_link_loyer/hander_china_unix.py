#导用三个包，requests包，re正则表达式包。time时间包
import re
import time
import requests

#创建网站的url
index_url = 'http://account.chinaunix.net/login'

#创建请求头，通过浏览器获取，用正则表达式(.*?):(.*)代替为"$1":"$2"，的方法改写
header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"Cookie":"account_chinauni=accountchinauni; Hm_lvt_0ee5e8cdc4d43389b3d1bfd76e83216b=1598251477; __utma=225341893.1355135215.1598251512.1598251512.1598251512.1; __utmc=225341893; __utmz=225341893.1598251512.1.1.utmcsr=chinaunix.net|utmccn=(referral)|utmcmd=referral|utmcct=/; pgv_pvi=8850414654; pgv_info=ssi=s6102824484; reg_referer=account.chinaunix.net; captcha_gee=5f4362db50eef; st_user_token=19f8c177b8e6b1e867420589a9e09647; XSRF-TOKEN=re2eIMXkhhO9HS89en9InuUH0383TZty1DLAfclX; laravel_session=s1wIulXvyyJCZKjEVRDreGK587CFm0nmcM27Enb6; __pts=1266187100; __ptb=1266187100; Hm_lpvt_0ee5e8cdc4d43389b3d1bfd76e83216b=1598274904; __pta=1849242531.1598251478.1598274899.1598274905.2",
"Host":"account.chinaunix.net",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
#构造session
login_session = requests.session()
#创建匹配的token，用正则表达式
token_search = re.compile(r'name="_token" value="(.*?)"')
#返回头，一定要用session获取，否则无法保存cookies
index_response = login_session.get(url=index_url,headers=header)
#获取token
token_value = re.search(token_search,index_response.text).group(1)

#登陆数据
data = {
    "username":"yubiao_123",
    "password":"yb19970329",
    "_token":token_value,
    "-t":time.time()
}
#登陆数据的url
login_url = 'http://account.chinaunix.net/login/login'
login_response = login_session.post(url=login_url,headers=header,data=data)

#目标页面获取数据
phone_url = 'http://account.chinaunix.net/ucenter/user/index'
phone_response = login_session.get(url=phone_url,headers=header)
print(phone_response.text)

#个人思路：
#登录一个网站首页
#1.创建首页url
#2，通过浏览器获取标准的请求头headers
#3.构建网站的session，session与requests区别：前者可以更好地保存cookies
#4._token是跳转到另一个网页的“钥匙🔑”,通过首页的返回的文本中可以获取到，要用正则表达式匹配出
# 为登录做准备
#登录界面
#1.创建data字典：登录名，密码，_token,_t
#2.创建登录时的url
#3.用session.post方法登录
#进入目标网页
#1.创建目标网页的url
#2.目标网页的返回头
#3.输出想要的返回部分