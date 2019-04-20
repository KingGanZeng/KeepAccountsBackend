import pdb
import math
import sqlite3
import json


class RecommendController:
    # 用户-类别矩阵
    user_category = dict()
    # 用户-账本类型矩阵
    user_book = dict()
    # 账本类型-账单类别矩阵
    book_category = dict()
    # 账单类别-账本类型矩阵
    category_book = dict()

    def addValueToMat(mat, key, value):
        if key not in mat:
            mat[key] = dict()
            mat[key][value] = 1
        else:
            if value not in mat[key]:
                mat[key][value] = 1
            else:
                mat[key][value] += 1

    def InitStat(self):
        db_data = sqlite3.connect("../db.sqlite3")
        # 创建游标
        c = db_data.cursor()
        # 获取user表中所有的记录
        c.execute("select * from api_record")
        # 获取结果，这里需要优化，相当于每次都跑全量数据
        result = c.fetchall()
        # 关闭连接
        db_data.close()
        for record_item in result:
            user = record_item[2]
            category = record_item[7]
            book = record_item[10]
            # 将数据存入矩阵
            RecommendController.addValueToMat(RecommendController.user_category, user, category)
            RecommendController.addValueToMat(RecommendController.user_book, user, book)
            RecommendController.addValueToMat(RecommendController.book_category, book, category)
            RecommendController.addValueToMat(RecommendController.category_book, category, book)

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
    def CategoryPopularity(selft):
        bookFreq = {}
        for book in RecommendController.book_category.keys():
            categoryFreq = {}
            for category, value in RecommendController.book_category[book].items():
                categoryFreq[category] = value
            bookFreq[book] = sorted(categoryFreq.items(), key=lambda a: a[1], reverse=True)
        return bookFreq

    # 将热门账单分类填充至数据库
    def UpdatePopularity(self, book_categoryFreq):
        db_data = sqlite3.connect("../db.sqlite3")
        c = db_data.cursor()
        for item in book_categoryFreq:
            json_record_recommend = json.dumps(book_categoryFreq[item])
            print(item)
            print(json_record_recommend)
            sql = "update api_recordrecommend set record_recommend = '%s' where book_type = '%s'"
            c.execute(sql % (json_record_recommend, item))
        c.execute("select * from api_recordrecommend")
        result = c.fetchall()
        print(result)
        db_data.close()


recommend = RecommendController()
recommend.InitStat()

categoryFreq = recommend.CategoryPopularity()
print("热门标签：%s" % categoryFreq)
recommend.UpdatePopularity(categoryFreq)
print("热门标签：%s" % categoryFreq)