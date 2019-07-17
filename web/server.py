
import tornado.ioloop
import tornado.web
import random
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open("./all.txt","a+",encoding="utf-8") as f:
            all = f.read()
            while True:
                MEID = "A000006D" + "".join(random.sample('ABCDEF0123456789', 6))
                if all.find(MEID) == -1:
                    break
            while True:
                IMEI1 = "864113036" + "".join(random.sample('0123456789', 6))
                if all.find(IMEI1) == -1:
                    break
            while True:
                IMEI2 = "864113036" + "".join(random.sample('0123456789', 6))
                if all.find(IMEI2) == -1:
                    break
            while True:
                IMEI3 = "864113036" + "".join(random.sample('0123456789', 6))
                if all.find(IMEI3) == -1:
                    break
            while True:
                PCBSN = "XPUDU171" + "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 7)) + "".join(random.sample('0123456789', 1))
                if all.find(PCBSN) == -1:
                    break
            while True:
                SN = "DU3SDH17" + "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 7)) + "".join(random.sample('0123456789', 1))
                if all.find(SN) == -1:
                    break
            while True:
                BLMAC = "50:01:D9:%s:%s:%s" % ("".join(random.sample('ABCDEF0123456789', 2)), "".join(random.sample('ABCDEF0123456789', 2)),"".join(random.sample('ABCDEF0123456789', 2)))
                if all.find(BLMAC) == -1:
                    break
            while True:
                WIMAC = "50:01:D9:%s:%s:%s" % ("".join(random.sample('ABCDEF0123456789', 2)), "".join(random.sample('ABCDEF0123456789', 2)),"".join(random.sample('ABCDEF0123456789', 2)))
                if all.find(WIMAC) == -1:
                    break
            req = {"MEID": MEID, "IMEI1": IMEI1, "IMEI2": IMEI2,"IMEI3": IMEI3, "PCBSN": PCBSN, "SN": SN, "BLMAC": BLMAC,"WIMAC": WIMAC}
            f.write(str(req)+"\n")
            self.write(req)
        #MEID = "A000006D" + "".join(random.sample('ABCDEF0123456789', 6))
        #IMEI1 = "864113036" + "".join(random.sample('0123456789', 6))
        #IMEI2 = "864113036" + "".join(random.sample('0123456789', 6))
        #IMEI3 = "864113036" + "".join(random.sample('0123456789', 6))
        #SN = "KWG5T1710" + "".join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 6)) + "".join(random.sample('0123456789', 1))
        #BLMAC = "50:01:D9:%s:%s:%s" % ("".join(random.sample('ABCDEF0123456789', 2)), "".join(random.sample('ABCDEF0123456789', 2)),"".join(random.sample('ABCDEF0123456789', 2)))
        #WIMAC = "50:01:D9:%s:%s:%s" % ("".join(random.sample('ABCDEF0123456789', 2)), "".join(random.sample('ABCDEF0123456789', 2)),"".join(random.sample('ABCDEF0123456789', 2)))
        #str = {"MEID":MEID,"IMEI1":IMEI1,"IMEI2":IMEI2,"IMEI3":IMEI3,"SN":SN,"BLMAC":BLMAC,"WIMAC":WIMAC}
        #STR = "MEID:%s<br>IMEI1:%s\nIMEI2:%s\nIMEI3:%s\nSN:%s\nBLMAC:%s\nWIMAC:%s" % (MEID, IMEI1, IMEI2, IMEI3, SN, BLMAC, WIMAC)
        #self.write(str)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9408)
    print("I'm Tomorrow\nServing HTTP on Port:9408...")
    tornado.ioloop.IOLoop.current().start()
