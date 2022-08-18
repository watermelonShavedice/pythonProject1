import pandas as pd
import re
import os


def read():

    # 读取excel文件
    plan_split = pd.read_excel(r"D:\Desktop\程序匹配专用文件\黑龙江招生计划带选科.xlsx")
    tool_table = pd.read_excel(r"D:\Desktop\程序匹配专用文件\选科标识3+1+2.xlsx")
    # 读取表中对应的列值（values）
    #原始数据表属性创建
    first = plan_split['再选科目'].values
    secound = plan_split['首选科目'].values
    #选考标识属性创建
    tool = tool_table._ixs(0)
    tool_dili = tool_table['地'].values
    tool_huaxue = tool_table['化'].values
    tool_shengwu = tool_table['生'].values
    tool_lishi = tool_table['史'].values
    tool_wuli = tool_table['物'].values
    tool_zhengzhi = tool_table['政'].values

    kemu = ["地", "化", "生", "政"]
    zuhe = ["和", "或", "加", "与"]
    xuanke = []
    for i in range(len(first)):
        # print(first[i])
        zancun = []
        zancun_first = []
        finish = []
        zuhe_pipei = ''
        shouxuan = ''
        # print(first[i])
        if '物理' in str(secound[i]) or str(secound[i]) == '物':
            shouxuan = secound[i]
            if str(first[i]) == '不限':
                zancun_first.append(list(tool_wuli))
            else:
                for j in range(len(first[i])):
                    if first[i][j] in zuhe:
                        zuhe_pipei = first[i][j]
                    if first[i][j] in kemu:
                        weizhi = first[i][j]
                        if kemu.index(weizhi) == 0:
                            zancun_first.append(list(tool_dili))
                        elif kemu.index(weizhi) == 1:
                            zancun_first.append(list(tool_huaxue))
                        elif kemu.index(weizhi) == 2:
                            zancun_first.append(list(tool_shengwu))
                        else:
                            zancun_first.append(list(tool_zhengzhi))
                    # print(zancun_first)
        elif str(secound[i]) == '历史' or str(secound[i]) == '历':
            shouxuan = secound[i]
            if str(first[i]) == '不限':
                zancun_first.append(list(tool_lishi))
            else:
                for j in range(len(first[i])):
                    if first[i][j] in zuhe:
                        zuhe_pipei = first[i][j]
                    if first[i][j] in kemu:
                        weizhi = first[i][j]
                        if kemu.index(weizhi) == 0:
                            zancun_first.append(list(tool_dili))
                            # print(zancun_first)
                        elif kemu.index(weizhi) == 1:
                            zancun_first.append(list(tool_huaxue))
                            # print(zancun_first)
                        elif kemu.index(weizhi) == 2:
                            zancun_first.append(list(tool_shengwu))
                            # print(zancun_first)
                        else:
                            zancun_first.append(list(tool_zhengzhi))
        else:
            # print(zancun_first, i, secound[i], first[i])
            print("大傻子错啦")
        # 如果再选科目
        if zuhe_pipei == "加" or zuhe_pipei == '与' or zuhe_pipei == '和':
            if shouxuan == '物' or shouxuan == '物理':
                zancun_first.append(list(tool_wuli))
                finish.append(list(set(zancun_first[0]).intersection(*zancun_first[1:])))
            else:
                zancun_first.append(list(tool_lishi))
                finish.append(list(set(zancun_first[0]).intersection(*zancun_first[1:])))
        elif zuhe_pipei == "或":
            if shouxuan == '物' or shouxuan == '物理':
                zancun.append(list(set(zancun_first[0]).union(*zancun_first[1:])))
                zancun.append(list(tool_wuli))
                finish.append(list(set(zancun[0]).intersection(*zancun[1:])))
            else:
                zancun.append(list(set(zancun_first[0]).union(*zancun_first[1:])))
                zancun.append(list(tool_lishi))
                finish.append(list(set(zancun[0]).intersection(*zancun[1:])))
        else:
            if shouxuan == '物' or '物理' in shouxuan:
                zancun_first.append(list(tool_wuli))
                finish.append(list(set(zancun_first[0]).intersection(*zancun_first[1:])))
            else:
                zancun_first.append(list(tool_lishi))
                finish.append(list(set(zancun_first[0]).intersection(*zancun_first[1:])))
        # 集合排序
        finish[0].sort()
        xuanke.append(finish[0])
    # print(xuanke)
    # print(xuanke)
    # 用来增加新表属性
    plan_split['选科标识'] = xuanke
    # print(plan_split)
    #
    plan_split.to_excel(r"D:\Desktop\程序匹配专用文件\完成数据.xlsx", index=False)


read()
