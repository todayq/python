from modules.ksw import ksw
from store import store
from multiprocessing.dummy import Pool as ThreadPool
import os

contentmany = []
def main():
    print(os.getcwd())
    store.init()
    href = ksw.getlist("https://www.00ksw.net/html/72/72692/") #获取列表
    #使用多线程
    pool = ThreadPool(10) #10个线程
    pool.map(handle,href)
    pool.close()
    pool.join()
    #for x in href:
        #handle(x)
    if store.save(contentmany):
        print("全部插入数据库成功" )
    else:
        print("插入数据库失败")

def handle(url):
    content = ksw.getContent(url) #获取正文
    contentmany.append((content['title'],content['text']))
    with open("./resources/%s.txt" % (content['title']),"w",encoding="UTF-8") as f:
        f.write(content["text"])
        print(content['title']+'抓取成功')




if __name__ == '__main__':
    main()



