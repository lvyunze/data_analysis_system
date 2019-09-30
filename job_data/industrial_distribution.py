# -*- coding: utf-8 -*- 
# @Author : yunze
# 行业分布
import connect_database
import change
import json
from flask import Blueprint
con = connect_database.con_database('127.0.0.1', 'sa', 'root', 'analyze')
industrial_distriburtion_data = Blueprint("industrial_distriburtion", __name__)
connect = con[0]
cur = con[1]


def city_all():
    gd_area = "select count(*) from job_data  where unit like '%广东%'"
    cur.execute(gd_area)
    row = cur.fetchone()
    return row[0]


def education():
    education_p = "select count(*) from job_data where company like '%教育%'"
    cur.execute(education_p)
    row = cur.fetchone()
    return row[0]


def commercial_services():
    commercial_services_p = "select count(*) from job_data where company like '%商务服务%'"
    cur.execute(commercial_services_p)
    row = cur.fetchone()
    return row[0]


def software():
    software_p = "select count(*) from job_data where company like '%软件%'"
    cur.execute(software_p)
    row = cur.fetchone()
    return row[0]


def sports():
    sports_p = "select count(*) from job_data where company like '%体育%'"
    cur.execute(sports_p)
    row = cur.fetchone()
    return row[0]


# 批发业
def wholesale():
    wholesale_p = "select count(*) from job_data where company like '%批发%'"
    cur.execute(wholesale_p)
    row = cur.fetchone()
    return row[0]


# 文化艺术
def culture_art():
    culture_art_p = "select count(*) from job_data where company like '%文化%'"
    cur.execute(culture_art_p)
    row = cur.fetchone()
    return row[0]


# 零售业
def retail():
    retail_p = "select count(*) from job_data where company like '%零售%'"
    cur.execute(retail_p)
    row = cur.fetchone()
    return row[0]


# 国家机构
def state_institution():
    state_institution_p = "select count(*) from job_data where company like '%国家机构%'"
    cur.execute(state_institution_p)
    row = cur.fetchone()
    return row[0]


# 专业技术服务类
def professional_skill():
    professional_skill_p = "select count(*) from job_data where company like '%技术%'"
    cur.execute(professional_skill_p)
    row = cur.fetchone()
    return row[0]


# 研究和试验发展
def research():
    research_p = "select count(*) from job_data where company like '%研究%'"
    cur.execute(research_p)
    row = cur.fetchone()
    return row[0]


education = education()
commercial_services = commercial_services()
software = software()
sports = sports()
wholesale = wholesale()
culture_art = culture_art()
retail = retail()
state_institution = state_institution()
professional_skill = professional_skill()
research = research()

all_statistics = city_all()


def to(variate):
    variate_p = change.decimal_percent(float(change.decimal_to_two(variate/all_statistics)))
    return variate_p


def calculate():
    education_p = to(education)
    commercial_services_p = to(commercial_services)
    software_p = to(software)
    sports_p = to(sports)
    wholesale_p = to(wholesale)
    culture_art_p = to(culture_art)
    retail_p = to(retail)
    state_institution_p = to(state_institution)
    professional_skill_p = to(professional_skill)
    research_p = to(research)
    return education_p, commercial_services_p, software_p, sports_p, \
        wholesale_p, culture_art_p, retail_p, state_institution_p, professional_skill_p,\
        research_p


calculate = calculate()
lst = ("education", "commercial_services", "software", "sports", "wholesale", "culture", "retail", "state_institution", 
       "professional_skill", "research")
calculate_dict = {}
for i in range(len(calculate)):
    calculate_dict[lst[i]] = calculate[i]

calculate_dict_json = json.dumps(calculate_dict, indent=4, sort_keys=True)
print(calculate_dict_json)


@industrial_distriburtion_data.route('/industrial_data/')
def area_data():
    return calculate_dict_json








