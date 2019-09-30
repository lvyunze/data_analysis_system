# -*- coding: utf-8 -*- 
# @Author : yunze
# 单位分布
import connect_database
import change
from flask import Blueprint
from flask import jsonify
import json
unit_distribution_data = Blueprint("unit_distribution", __name__)
con = connect_database.con_database('127.0.0.1', 'sa', 'root', 'analyze')
connect = con[0]
cur = con[1]


def all_a():
    all_p = "select count(*) from job_data"
    cur.execute(all_p)
    row = cur.fetchone()
    return row[0]


# 企业
def enterprise():
    enter_num = "select count(*) from job_data where flat like '%[企公]%'"
    cur.execute(enter_num)
    row = cur.fetchone()
    return row[0]


# 中初教育单位
def primary_school_education_unit():
    enter_num = "select count(*) from job_data where flat like '%[中初]%'"
    cur.execute(enter_num)
    row = cur.fetchone()
    return row[0]


# 其他事业单位
def other_institutions():
    other_institutions_num = "select count(*) from job_data where flat like '%事业单位%'"
    cur.execute(other_institutions_num)
    row = cur.fetchone()
    return row[0]


# 国家机关
def state_organs():
    state_organs_num = "select count(*) from job_data where flat like '%国家%'"
    cur.execute(state_organs_num)
    row = cur.fetchone()
    return row[0]


# 科研单位
def scientific():
    scientific_num = "select count(*) from job_data where flat like '%科研%'"
    cur.execute(scientific_num)
    row = cur.fetchone()
    return row[0]


# 部队
def troops():
    troops_num = "select count(*) from job_data where flat like '%部队%'"
    cur.execute(troops_num)
    row = cur.fetchone()
    return row[0]


# 医疗卫生
def health_care():
    health_care_num = "select count(*) from job_data where flat like '%卫生%'"
    cur.execute(health_care_num)
    row = cur.fetchone()
    return row[0]


enterprise = enterprise()
primary_school_education_unit = primary_school_education_unit()
other_institutions = other_institutions()
state_organs = state_organs()
scientific = scientific()
troops = troops()
health_care = health_care()


unit_all = all_a()


def to(variate):
    variate_p = change.decimal_percent(float(change.decimal_to_two(variate/unit_all)))
    return variate_p


def other():
    other_num = unit_all - enterprise - primary_school_education_unit -\
                other_institutions - state_organs - scientific - troops - health_care
    return other_num


other = other()


def calculate():
    enterprise_p = to(enterprise)
    primary_school_education_unit_p = to(primary_school_education_unit)
    other_institutions_p = to(other_institutions)
    state_organs_p = to(state_organs)
    scientific_p = to(scientific)
    troops_p = to(troops)
    health_care_p = to(health_care)
    return enterprise_p, primary_school_education_unit_p, other_institutions_p, state_organs_p,\
        scientific_p, troops_p, health_care_p
    
    
calculate = calculate()

lst = ("enterprise", "primary_school_education_unit", "other_institutions", "state_organs",
       "scientific", "troops", "health_care")
calculate_dict = {}
for i in range(len(calculate)):
    calculate_dict[lst[i]] = calculate[i]

calculate_dict_json = json.dumps(calculate_dict, indent=4, sort_keys=True)
print(calculate_dict_json)


@unit_distribution_data.route('/unit_data/')
def unit_data():
    return jsonify(**calculate_dict), 230


