# -*- coding: utf-8 -*- 
# @Author : yunze
# 职业分布
import connect_database
import change
import json
from flask import Blueprint
con = connect_database.con_database('127.0.0.1', 'sa', 'root', 'analyze')
professional_distriburtion_data = Blueprint("professional_data", __name__)
connect = con[0]
cur = con[1]


def all_regional():
    all_regional_p = "select count(*) from job_data"
    cur.execute(all_regional_p)
    row = cur.fetchone()
    return row[0]


def teaching_staff():
    teaching_staff_p = "select count(*) from job_data where types like '%教%'"
    cur.execute(teaching_staff_p)
    row = cur.fetchone()
    return row[0]


def engineering_technicians():
    teaching_staff_p = "select count(*) from job_data where types like '%工程技术%'"
    cur.execute(teaching_staff_p)
    row = cur.fetchone()
    return row[0]


def business_service_workers():
    business_service_workers_p = "select count(*) from job_data where company like '%工程技术%'"
    cur.execute(business_service_workers_p)
    row = cur.fetchone()
    return row[0]


def worker():
    worker_p = "select count(*) from job_data where types like '%办事%'"
    cur.execute(worker_p)
    row = cur.fetchone()
    return row[0]


# 经济业务
def conomic_personnel():
    conomic_personnel_p = "select count(*) from job_data where types like '%经济业务%'"
    cur.execute(conomic_personnel_p)
    row = cur.fetchone()
    return row[0]


# 金融业务
def financial_service():
    financial_service_p = "select count(*) from job_data where types like '%金融业务%'"
    cur.execute(financial_service_p)
    row = cur.fetchone()
    return row[0]


# 文艺艺术
def literature_art():
    literature_art_p = "select count(*) from job_data where types like '%金融业务%'"
    cur.execute(literature_art_p)
    row = cur.fetchone()
    return row[0]


# 其他专业技术人员
def other():
    other_p = "select count(*) from job_data where types like '%其他专业技术%'"
    cur.execute(other_p)
    row = cur.fetchone()
    return row[0]


# 新闻出版
def press_publications():
    press_publications_p = "select count(*) from job_data where types like '%新闻出版%'"
    cur.execute(press_publications_p)
    row = cur.fetchone()
    return row[0]


# 公务员
def civil_servant():
    civil_servant_p = "select count(*) from job_data where types like '%公务员%'"
    cur.execute(civil_servant_p)
    row = cur.fetchone()
    return row[0]


teaching_staff = teaching_staff()
engineering_technicians = engineering_technicians()
business_service_workers = business_service_workers()
worker = worker()
conomic_personnel = conomic_personnel()
financial_service = financial_service()
literature_art = literature_art()
other = other()
press_publications = press_publications()
civil_servant = civil_servant()

all_pre = teaching_staff+engineering_technicians+business_service_workers+worker+\
          conomic_personnel+financial_service+literature_art+other+press_publications+civil_servant
all_p = all_regional()


def to(variate):
    variate_p = change.decimal_percent(float(change.decimal_to_two(variate/all_pre)))
    return variate_p


def calculate():
    teaching_staff_p = to(teaching_staff)
    engineering_technicians_p = to(engineering_technicians)
    business_service_workers_p = to(business_service_workers)
    worker_p = to(worker)
    conomic_personnel_p = to(conomic_personnel)
    financial_service_p = to(financial_service)
    literature_art_p = to(literature_art)
    other_p = to(other)
    press_publications_p = to(press_publications)
    civil_servant_p = to(civil_servant)
    return teaching_staff_p, engineering_technicians_p,\
        business_service_workers_p, worker_p, conomic_personnel_p,\
        financial_service_p, literature_art_p, other_p,\
        press_publications_p, civil_servant_p


calculate = calculate()
lst = ("teaching_staff", "engineering_technicians", "business_service_workers", "worker", "conomic_personnel",
       "financial_service", "literature_art", "other",
       "press_publications", "civil_servant")
lst_num = (teaching_staff, engineering_technicians, business_service_workers, worker, conomic_personnel,
           financial_service, literature_art, other, press_publications, civil_servant)
calculate_dict = {}
cal_num = {}
cal_pre = {}

for i in range(len(calculate)):
    cal_pre[lst[i]] = calculate[i]

for j in range(len(lst)):
    cal_num[lst[j]] = lst_num[j]

calculate_dict["cal_pre"] = cal_pre
calculate_dict["cal_num"] = cal_num
calculate_dict_json = json.dumps(calculate_dict, indent=4, sort_keys=True)

print(calculate_dict_json)


@professional_distriburtion_data.route('/professional_data/')
def area_data():
    return calculate_dict_json

