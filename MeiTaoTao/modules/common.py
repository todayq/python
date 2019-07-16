#公共类
import random,string
class common:

        #取出中间的文本
    def getTextMiddle(text,Left,Right):
        l = text.find(Left) + len(Left)
        r = text.find(Right,l)
        return text[l:r]

        #保存文档
    def saveTxt(text,path):
        with open(path,"a",encoding="utf-8") as f:
            f.write(text+"\r\n")

        #从a - zA - Z0 - 9生成指定数量的随机字符
    def randomStr(num):
        str = ''.join(random.sample(string.ascii_letters + string.digits, num))
        return str