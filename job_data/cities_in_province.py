# -*- coding: utf-8 -*- 
# @Author : yunze
# -*- coding: utf-8 -*-
# @Author : yunze
import connect_database
import change
from flask import Blueprint
import json
cities_in_province_data = Blueprint('cities_in_province', __name__)

con = connect_database.con_database('127.0.0.1', 'sa', 'root', 'analyze')
connect = con[0]
cur = con[1]


def city_all():
    gd_area = "select count(*) from job_data  where unit like '%广东%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 广州
def guangzhou():
    gd_area = "select count(*) from job_data where unit like '%广州%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


def zhanjiang():
    gd_area = "select count(*) from job_data where unit like '%湛江%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 深圳
def shenzhen():
    gd_area = "select count(*) from job_data where unit like '%深圳%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 佛山
def fosan():
    gd_area = "select count(*) from job_data where unit like '%佛山%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 东莞
def dongguan():
    gd_area = "select count(*) from job_data where unit like '%东莞%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 中山
def zhongshan():
    gd_area = "select count(*) from job_data where unit like '%中山市%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 茂名
def maoming():
    gd_area = "select count(*) from job_data where unit like '%茂名市%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 江门
def jiangmen():
    gd_area = "select count(*) from job_data where unit like '%江门市%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 阳江
def yangjiang():
    gd_area = "select count(*) from job_data where unit like '%阳江市%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 肇庆
def zhaoqing():
    gd_area = "select count(*) from job_data where unit like '%肇庆市%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


guangzhou = guangzhou()
zhanjiang = zhanjiang()
shenzhen = shenzhen()
fosan = fosan()
dongguan = dongguan()
zhongshan = zhongshan()
maoming = maoming()
jiangmen = jiangmen()
yangjiang = yangjiang()
zhaoqing = zhaoqing()
city_all = city_all()


def to(variate):
    variate_p = change.decimal_percent(float(change.decimal_to_two(variate/city_all)))
    return variate_p


def statistics():
    guangzhou_p = to(guangzhou)
    zhanjiang_p = to(zhanjiang)
    shenzhen_p = to(shenzhen)
    fosan_p = to(fosan)
    dongguan_p = to(dongguan)
    zhongshan_p = to(zhongshan)
    maoming_p = to(maoming)
    jiangmen_p = to(jiangmen)
    yangjiang_p = to(yangjiang)
    zhaoqing_p = to(zhaoqing)
    return guangzhou_p, zhanjiang_p, shenzhen_p, fosan_p, dongguan_p,\
        zhongshan_p, maoming_p, jiangmen_p, yangjiang_p, zhaoqing_p


lst = ('guangzhou', 'zhanjiang', 'shenzhen', 'fosan', 'dongguan', 'zhongshan', 'maoming', 'jiangmen', 'yangjiang',
       'zhaoqing')

statistics = statistics()
city_data_dict = {}
print(statistics[0])
city_data_dict["guangzhou"] = statistics[0]


for i in range(len(lst)):
    city_data_dict[lst[i]] = statistics[i]


c = json.dumps(city_data_dict, indent=4, sort_keys=True)
print(c)


@cities_in_province_data.route('/city_data/')
def city_data():
    return c


