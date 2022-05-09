#encoding:utf-8
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings()
# 加这句不会报错(requests证书警告)
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class HTTPRequests():
    def __init__(self):
        self.url="https://ironfist.yuntingai.com"
        self.req=requests.session()  #做接口关联
        # 依据自己公司的请求头默认值配置(经过抓包，发现CEM请求接口，请求头)
        self.head = {
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br"}

    # 封装自己的get请求，获取资源
    def get(self, uri='', params='', data='', headers=None, cookies=None, verify=False):
        if headers is None:
            headers = self.head
            # print("请求头是:{}".format(headers))
        url = self.url + uri
        response = self.req.get(url, params=params, data=data, headers=headers, cookies=cookies, verify=verify)
        return response

    # 封装自己的post请求，获取资源
    def post(self, uri='', params='', data='', headers=None, cookies=None, verify=False):
        if headers is None:
            headers = self.head
        url = self.url + uri
        response = self.req.post(url, params=params, data=data, headers=headers, cookies=cookies, verify=verify)
        return response

    # 封装自己的put请求，获取资源
    def put(self, uri='', params='', data='', headers=None, cookies=None, verify=False):
        if headers is None:
            headers = self.head
        url = self.url + uri
        response = self.req.put(url, params=params, data=data, headers=headers, cookies=cookies, verify=verify)
        return response

    # 封装自己的delete请求，获取资源
    def delete(self, uri='', params='', data='', headers=None, cookies=None, verify=False):
        if headers is None:
            headers = self.head
        url = self.url + uri
        response = self.req.delete(url, params=params, data=data, headers=headers, cookies=cookies, verify=verify)
        return response




if __name__=="__main__":
    pass


