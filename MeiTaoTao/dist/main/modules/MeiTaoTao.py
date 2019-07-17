from modules.common import common
from modules.WmOcr import WmOcr
#from urllib.parse import quote,unquote
from urllib.parse import urlencode
import requests,os,json

class MeiTaoTao:
    def __init__(self,user,pwd):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.user = user
        self.pwd = pwd
        self.r    = requests.session()
        self.err = ""
        self.heads = {
            "Host": "www.meitaotao.com",
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "Origin": "https://www.meitaotao.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://www.meitaotao.com/passport-signup.html?mini_passport=1",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        if WmOcr.init() == False:
            self.err = "WmOcr初始化失败"

    def getErr(self):
        return self.err
    def checkName(self):
        url = "https://www.meitaotao.com/passport-signup_ajax_check_name.html"
        str = self.r.post(url = url,data = "pam_account[login_name]="+self.user,headers = self.heads)
        str = str.content.decode(encoding="raw_unicode_escape")
        if str.find("success") == -1:
            self.err = json.loads(str)['error']
            return False
        return True


    def reg(self):
        url  = "https://www.meitaotao.com/index-gen_vcode-LOGINVCODE-4.html?1563174503643"
        byte = self.r.get(url).content
        code = WmOcr.ocr(byte)
        if code == '':
            self.err = "code Null"
            return False
        url = "https://www.meitaotao.com/passport-create.html"
        data ={
            "forward":"",
            "mini": 1,
            "pam_account[login_name]": self.user,
            "pam_account[login_password]": self.pwd,
            "pam_account[psw_confirm]": self.pwd,
            "signupverifycode": code,
            "vcode": "",
            "license": "on",
            "response_json": "true"
        }
        data = urlencode(data)
        str = self.r.post(url = url , data=data,headers = self.heads)
        str = str.content.decode(encoding="raw_unicode_escape")
        if str.find("success") == -1:
            self.err = json.loads(str)['error']
            return False
        return True



    def login(self):
        pass
