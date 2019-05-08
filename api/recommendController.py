import pdb
import math
import sqlite3
import json
import time
from apscheduler.schedulers.blocking import BlockingScheduler


class RecommendController:
    def __init__(self):
        print("MyClass类的构造方法被调用！")

    def addValueToMat(self, mat, key, value):
        if key not in mat:
            mat[key] = dict()
            mat[key][value] = 1
        else:
            if value not in mat[key]:
                mat[key][value] = 1
            else:
                mat[key][value] += 1

    def InitStat(self):
        # 用户-类别矩阵
        user_category = dict()
        # 用户-账本类型矩阵
        user_book = dict()
        # 账本类型-账单类别矩阵
        book_category = dict()
        # 账单类别-账本类型矩阵
        category_book = dict()
        db_data = sqlite3.connect("../db.sqlite3")
        # 创建游标
        c = db_data.cursor()
        # 获取user表中所有的记录
        c.execute("select * from api_record")
        # 获取结果，这里需要优化，相当于每次都跑全量数据
        result = c.fetchall()
        for record_item in result:
            user = record_item[2]
            category = record_item[7]
            book = record_item[10]
            self.addValueToMat(user_category, user, category)
            self.addValueToMat(user_book, user, book)
            self.addValueToMat(book_category, book, category)
            self.addValueToMat(category_book, category, book)
        # 关闭连接
        db_data.close()
        return book_category

    # 计算推荐列表
    def Recommend(user):
        recommend_list = dict()
        tagged_item = RecommendController.user_category[user]
        for book, wu in RecommendController.user_book[user].items():
            for category, wi in RecommendController.book_category[book].items():
                if category not in tagged_item:
                    if category not in recommend_list:
                        recommend_list[category] = wu * wi
                    else:
                        recommend_list[category] += wu * wi

        return sorted(recommend_list.items(), key=lambda a: a[1], reverse=True)

    # 统计每个账本类别的热门账单
    def CategoryPopularity(self, book_category):
        bookFreq = {}
        for book in book_category.keys():
            categoryFreq = {}
            for category, value in book_category[book].items():
                categoryFreq[category] = value
            bookFreq[book] = sorted(categoryFreq.items(), key=lambda a: a[1], reverse=True)
        return bookFreq

    # 将热门账单分类填充至数据库
    def UpdatePopularity(self, book_categoryFreq):
        db_data = sqlite3.connect("../db.sqlite3")
        c = db_data.cursor()
        for item in book_categoryFreq:
            print(book_categoryFreq[item])
            json_record_recommend = json.dumps(book_categoryFreq[item])
            sql = "update api_recordrecommend set record_recommend = '%s' where book_type = '%s'"
            c.execute(sql % (json_record_recommend, item))
            db_data.commit()
        c.execute("select * from api_recordrecommend")
        result = c.fetchall()
        print('*******')
        print(result)
        db_data.close()


    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


def my_job():
    recommend = RecommendController()
    book_category = recommend.InitStat()
    categoryFreq = recommend.CategoryPopularity(book_category)
    # print("热门标签：%s" % categoryFreq)
    recommend.UpdatePopularity(categoryFreq)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    del recommend


sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()