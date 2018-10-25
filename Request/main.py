
import _thread
import requests
import json

def read_time(thread_name,count):
    print("输出线程成功", thread_name, count);
    # r = requests.get("http://localhost:8888")
    dic = { "latitude" : 1.1,"longitude" : 1.1,"altitude" : 1.1,"course" : 1.1,"speed" : 1.1,"hAccuracy" : 1.1,"vAccuracy" : 1.1,"timestamp" : 1.1,"insert_timestamp" : 1.1}
    jsonstr = json.dumps(dic)
    print(jsonstr)
    r = requests.post("http://localhost:8888",data=jsonstr)
    body = '请求成功{} ,age {}'.format(thread_name, r.text);
    print(body)

if __name__ == '__main__':
    print("IM IS REQUEST");
    # read_time("2312",3);
    count = 10000
    while count > 0:
        print("request i = ", count)
        name = "thread_name = {}".format(count);
        try:
            _thread.start_new_thread(read_time,(name,count))
        except:
            print("线程错误")

        count -= 1

    name = input()
    print(name);