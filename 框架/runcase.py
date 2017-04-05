__author__ = 'Administrator'
from learnpython.框架.connect_mysql import DataBase
from learnpython.框架.HttpRequest import TestInterface
from learnpython.框架.Mode import Mode


class RunCase:
    def run_case(self, http, cnn, mode, case_list):

        if (mode == 1):  # 判断，如果mode等于1，就跑全部用例
            cursor = cnn.cursor()
            cursor.execute("select count(*) from test_data")  #统计共有多少条用例
            list = cursor.fetchone()
            num = list[0]    #把用例数存下来
            #print("num", num)
            #print("list", list)
            for i in range(1, num + 1):  #循环
                cursor.execute("select * from test_data where case_id =%s"%i)   #一条一条执行所有用例,注意sql语句加变量的写法
                list = cursor.fetchone()
                #将需要的参数分别存起来后面要用
                url = list[3]
                data = eval(list[4])
                http_method = list[1]
                #判断是get请求还是post请求，分别调用不同的方法
                if (http_method == "GET"):
                    http.interface_get(url, data)
                else:
                    http.interface_post(url, data)

            cursor.close()
            cnn.close()

        else:  # 如果mode不等于1，跑case_list里的用例
            cursor = cnn.cursor()
            for i in case_list:
                sql = "select * from test_data where case_id =%s"
                cursor.execute(sql%i)
                list = cursor.fetchone()
                url = list[3]
                data = eval(list[4])
                http_method = list[1]
                if (http_method == "GET"):
                    http.interface_get(url, data)
                else:
                    http.interface_post(url, data)

            cursor.close()
            cnn.close()


http = TestInterface("http.conf")
b = DataBase("database.conf")
cnn = b.get_cnn()
c = Mode("mode.conf")
mode = c.Get_mode()
case_list = c.Get_case_list()
test_1 = RunCase()

test_1.run_case(http, cnn, mode, case_list)

