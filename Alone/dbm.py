
import pymysql
import json
import time
class DBM(object):

    instance = None
    db = None
    def __init__(self):
        self.db = pymysql.connect("localhost","root","123456","LOCATION" )
        print("init DBM")

    @classmethod
    def get_instance(self):
        if self.instance:
            return self.instance
        else:
            objc = self()
            self.instance = objc
            return objc

    def inset_data(self,jsonStr):
        mycursor = self.db.cursor()
        print("接收到的数据", jsonStr)
        dic = json.loads(jsonStr)
        create = time.time()
        sql = "insert into LOCATION (latitude, longitude, altitude, course, speed, hAccuracy, vAccuracy, timestamp, insert_timestamp) \
        values ({},{},{},{},{},{},{},{},{})".format(dic['latitude'],dic["longitude"],dic["altitude"],dic["course"],dic["speed"],dic["hAccuracy"],dic["vAccuracy"],dic["timestamp"],create)
        try:
            mycursor.execute(sql)
            self.db.commit()
        except:
            print("插入失败")
            self.db.rollback()
        finally:
            print("结束")
        print("插入数据成功: ",mycursor.lastrowid)

    def select(self):
        print("查询所有的数据")


