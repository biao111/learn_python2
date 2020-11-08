import requests
import re

class Login(object):
    '''登录'''
    def __init__(self):
        self.requests_session = requests.session()
        self.header = {
            "User-Agent":"Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.135Safari / 537.36"
        }
        self.csrf_value = ''

    def headle_csrf_token(self):
        self.index_url = 'http://flask.zhaedu.com/mall/product/list/1'
        crsf_response = self.requests_session.get(url=self.index_url,headers=self.header)
        token_search = re.compile(r'name="csrf_token"\stype="hidden"\svalue="(.*?)">')
        self.csrf_value = token_search.search(crsf_response.text).group(1)
        return self.csrf_value

    def headle_login(self):
        login_url = 'http://flask.zhaedu.com/accounts/login'
        username = input("请输入用户名：")
        password = input("请输入密码：")
        self.headle_csrf_token()
        data = {
            "csrf_token":self.csrf_value,
            "username":username,
            "password":password
        }
        self.requests_session.post(url=login_url,headers=self.header,data=data)
        response = self.requests_session.get(url=self.index_url,headers=self.header)
        print(response.text)

if __name__ == '__main__':
    flask_zhaedu_com = Login()
    #flask_zhaedu_com.headle_csrf_token()
    flask_zhaedu_com.headle_login()