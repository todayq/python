from modules.MeiTaoTao import MeiTaoTao
import os
from multiprocessing.dummy import Pool as ThreadPool
from modules.common import common
path = os.path.dirname(os.path.realpath(__file__))
def main():

    text=[]
    num = input("请输入注册个数：")
    for x in range(int(num)):
        user = common.randomStr(8) + "@666email.com"
        pwd = common.randomStr(8)
        text.append({"user": user, "pwd": pwd})
    pool = ThreadPool(1)  # 10个线程
    pool.map(tomorrow, text)
    pool.close()
    pool.join()

def tomorrow(text):
    r = MeiTaoTao(text["user"],text["pwd"])
    if r.checkName() == False:
        print(r.getErr())
    elif r.reg() == False:
        print(r.getErr())
    else:
        common.saveTxt(text["user"] + "|" + text["pwd"], path + "/resources/register.txt")
        print("注册成功："+text["user"]+"|"+text["pwd"])








if __name__ == '__main__':
    main()