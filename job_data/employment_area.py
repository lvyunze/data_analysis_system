# -*- coding: utf-8 -*- 
# @Author : yunze
import connect_database
import change
import json
from flask import Blueprint
employment_area_data = Blueprint('employment_area', __name__)
con = connect_database.con_database('127.0.0.1', 'sa', 'root', 'analyze')
connect = con[0]
cur = con[1]


def city_all():
    gd_area = "select count(*) from job_data"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


# 广东地区
def gd_area():
    gd_area_p = "select count(*) from job_data where unit like '%广东%'"
    cur.execute(gd_area_p)
    row = cur.fetchone()
    return row[0]


all_p = city_all()
gd_area_num = gd_area()


# 其他省份地区
def other_area():
    other_area_p = all_p - gd_area_num
    return other_area_p


other_area = other_area()



def to(variate):
    variate_p = change.decimal_percent(float(change.decimal_to_two(variate/all_p)))
    return variate_p


def calculate():
    gd_area_p = to(gd_area_num)
    other_area_p = to(other_area)
    return gd_area_p, other_area_p


calculate = calculate()
lst = ("gd_area", "other_area")
calculate_dict = {}
for i in range(len(calculate)):
    calculate_dict[lst[i]] = calculate[i]

calculate_dict["gd_area_num"] = gd_area_num
calculate_dict["other_area_num"] = other_area
print(type(calculate_dict["other_area_num"]))
calculate_dict_json = json.dumps(calculate_dict, indent=4, sort_keys=True)
print(calculate_dict_json)


@employment_area_data.route('/area_data/')
def area_data():
    return calculate_dict_json
