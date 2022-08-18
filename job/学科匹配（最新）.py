import pandas as pd
import re
import os


def read():
    # 读取excel文件
    plan_excel = pd.read_excel(r"D:\Desktop\程序匹配专用文件\新疆2022招生计划（最新）.xlsx")
    maching_subject = pd.read_excel(r"D:\Desktop\程序匹配专用文件\专业匹配一级学科.xlsx")

    # 读取表中对应的列值（values）
    # 需匹配数据表属性创建
    plan_excel_schoolname = plan_excel['school_name'].values
    plan_excel_major = plan_excel['major_name'].values

    # 专业匹配一级学科数据表属性创建
    maching_subject_1 = maching_subject['专业名称'].values
    maching_subject_2 = maching_subject['一级学科'].values

    # 所需变量
    major = []
    school = []
    school_major = []
    new_major = []
    # 专业匹配一级学科
    for i in range(len(plan_excel_major)):
        major = re.sub(u"（.*$", "", plan_excel_major[i])
        ceshi = '未匹配上'
        for j in range(len(maching_subject_1)):
            if maching_subject_1[j] == major:
                new_major.append(maching_subject_2[j])
                ceshi = '已匹配上'
        if ceshi == '未匹配上':
            new_major.append(major)
    # print(len(new_major))
    # 学校和专业合并
    school_fixed = ["中国地质大学（北京）", "华北电力大学（北京）", "中国矿业大学（北京）", "华北电力大学（保定）", "中国地质大学（武汉）", "中国石油大学（华东）", "中国矿业大学（北京）"]
    for i in range(len(plan_excel_major)):
        major = new_major[i]
        # if school in school_fixed:
        #     school = plan_excel_schoolname[i]
        #     school_major.append(school + major)
        # else:
        school = re.sub(u'\\（.*?）', "", plan_excel_schoolname[i])
        # 江苏省去除专业组的合并方式
        # school = re.sub(u'\_.*组', "", plan_excel_schoolname[i])
        school_major.append(school + major)
    # print(school_major)
    return school_major, plan_excel
    # 用来增加新表属性


def pipei(school_major, plan_excel):
    read_plan = read()
    Dominant_discipline = pd.read_excel(r"D:\Desktop\程序匹配专用文件\优势学科.xlsx")
    Characteristic_discipline = pd.read_excel(r"D:\Desktop\程序匹配专用文件\特色学科.xlsx")
    Evaluation_results = pd.read_excel(r"D:\Desktop\程序匹配专用文件\评估结果.xlsx")

    # 优势学科属性创建
    Dominant_discipline_1 = Dominant_discipline['优势学科'].values

    # 特色学科属性创建
    Characteristic_discipline_1 = Characteristic_discipline['特色学科'].values

    # 评估结果属性创建
    Evaluation_results_1 = Evaluation_results['专业名称'].values
    Evaluation_results_2 = Evaluation_results['评估结果'].values

    # 定义变量
    Dominant_n = []
    Characteristic_n = []
    Evaluation_n = []

    for i in range(len(school_major)):
        cehsi1 = "未匹配上"
        cehsi2 = "未匹配上"
        cehsi3 = "未匹配上"
        # 优势学科
        for j in range(len(Dominant_discipline_1)):
            if Dominant_discipline_1[j] == school_major[i]:
                Dominant_n.append('1')
                cehsi1 = "已匹配上"
        if cehsi1 == '未匹配上':
            Dominant_n.append('0')

        # 特色学科
        for j in range(len(Characteristic_discipline_1)):
            if Characteristic_discipline_1[j] == school_major[i]:
                Characteristic_n.append('1')
                cehsi2 = "已匹配上"
        if cehsi2 == '未匹配上':
            Characteristic_n.append('0')

        # 评估结果
        for j in range(len(Evaluation_results_1)):
            if Evaluation_results_1[j] == school_major[i]:
                Evaluation_n.append(Evaluation_results_2[j])
                cehsi3 = "已匹配上"
        if cehsi3 == '未匹配上':
            Evaluation_n.append('0')
    # print(len(Dominant_n))
    # print(len(Characteristic_n))
    # print(len(Evaluation_n))

    # 用来增加新表属性
    # data = {
    #     '优势学科': Dominant_n, '特色学科': Characteristic_n, '评估结果': Evaluation_n
    # }
    plan_excel['优势学科'] = Dominant_n
    plan_excel['特色学科'] = Characteristic_n
    plan_excel['评估结果'] = Evaluation_n

    # df = pd.DataFrame(data)
    plan_excel.to_excel(r"D:\Desktop\程序匹配专用文件\完成数据.xlsx", index=False)
    # read_plan.plan_excel['优势学科'] = list(Dominant_n)
    # read_plan.plan_excel['特色学科'] = list(Characteristic_n)
    # read_plan.plan_excel['评估结果'] = list(Evaluation_n)
    # read_plan.plan_excel.to_excel(r"C:\Users\cy0007\Desktop\程序匹配专用文件\完成数据.xlsx", index=False)


# 测试合并学校名称和专业名称的合并
# read()
# 整体程序的调用
pipei(read()[0], read()[1])
