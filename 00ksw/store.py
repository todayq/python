import pymysql

class store:
    coon = None

    def init():
        store.coon = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'Qing0815!',
            db = 'tomorrow',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
        )
    def save(info):
        try:
            with store.coon.cursor() as cursor:   # 执行完毕返回的结果集默认以元组显示

                cursor.executemany('insert into content (title,text) values(%s,%s)',info) #执行SQL语句
            store.coon.commit()   #提交
            return True
        except:
            return False
            #cursor.close()  #关闭光标对象
            #store.coon.close()    #关闭SQL连接


