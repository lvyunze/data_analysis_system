# -*- coding: utf-8 -*-
# @Author : yunze
# 连接sq server数据库
import pymssql


def con_database(server, user, password, database):
    # 数据库服务器信息
    server = server
    user = user
    password = password
    database = database

    connect = pymssql.connect(server, user, password, database)
    cur = connect.cursor()
    # 返回三个参数（连接，游标，关闭数据库）
    return connect, cur
