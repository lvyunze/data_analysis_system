# -*- coding: utf-8 -*- 
# @Author : yunze
# 地区分布
import connect_database
import change
import json
from flask import Blueprint
regional_distribution_data = Blueprint("regional_distribution", __name__)
con = connect_database.con_database('127.0.0.1', 'sa', 'root', 'analyze')
connect = con[0]
cur = con[1]


def all_regional():
    all_regional_p = "select count(*) from job_data"
    cur.execute(all_regional_p)
    row = cur.fetchone()
    return row[0]


# 国企
def state_owned_enterprise():
    state_owned_enterprise_p = "select count(*) from job_data where flat like '%国有企业%'"
    cur.execute(state_owned_enterprise_p)
    row = cur.fetchone()
    return row[0]


# 民办
def mass_run_enterprises():
    mass_run_enterprises_p = "select count(*) from job_data where flat like '%[民私]%'"
    cur.execute(mass_run_enterprises_p)
    row = cur.fetchone()
    return row[0]


# 三资企业
def three_kinds_of_investment_enterprise():
    three_kinds_of_investment_enterprise_p = "select count(*) from job_data where flat like '%[有限公司]%'"
    cur.execute(three_kinds_of_investment_enterprise_p)
    row = cur.fetchone()
    return row[0]


state_owned_enterprise = state_owned_enterprise()
mass_run_enterprises = mass_run_enterprises()
three_kinds_of_investment_enterprise = three_kinds_of_investment_enterprise()


# 所有
all_regional = all_regional()


def to(variate):
    variate_p = change.decimal_percent(float(change.decimal_to_two(variate/all_regional)))
    return variate_p


# 统计
def statistics_a():
    state_owned_enterprise_p = to(state_owned_enterprise)
    mass_run_enterprises_p = to(mass_run_enterprises)
    three_kinds_of_investment_enterprise_p = to(three_kinds_of_investment_enterprise)
    return state_owned_enterprise_p, mass_run_enterprises_p, three_kinds_of_investment_enterprise_p


statistics_a = statistics_a()
lst = ("state_owned_enterprise", "mass_run_enterprises", "three_kinds_of_investment_enterprise")
lst_num = (state_owned_enterprise, mass_run_enterprises, three_kinds_of_investment_enterprise)
calculate_dict = {}
cal_pre = {}
cal_num = {}

for i in range(len(statistics_a)):
    cal_pre[lst[i]] = statistics_a[i]

for j in range(len(lst)):
    cal_num[lst[j]] = lst_num[j]

calculate_dict["cal_pre"] = cal_pre
calculate_dict["cal_num"] = cal_num

calculate_dict_json = json.dumps(calculate_dict, indent=4, sort_keys=True)

print(calculate_dict_json)


@regional_distribution_data.route('/regional_data/')
def regional_data():
    return calculate_dict_json

