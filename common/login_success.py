#encoding:utf-8
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings()
# 加这句不会报错(requests证书警告)
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Login_Success():
    def __init__(self):
        self.url="https://ironfist.yuntingai.com/api/login"
        self.data={"username":"liudongqin1@skieer.com","password":"Aa123456"}

    def get_Authorization(self):
        self.re=requests.post(url=self.url,data=self.data,verify=False)
        self.Authorization="Bearer"+" "+self.re.headers["Authorization"]
        print(self.re)
        return self.Authorization

if __name__=="__main__":
    print(Login_Success().get_Authorization())
