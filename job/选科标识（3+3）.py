import pandas as pd
import re
import os


def read():

    # 读取excel文件
    plan_split = pd.read_excel(r"C:\Users\cy0007\Desktop\新省份需要数据\天津需要数据\天津2021年计划.xlsx")
    tool_table = pd.read_excel(r"C:\Users\cy0007\Desktop\选科标识3+3.xlsx")
    # 读取表中对应的列值（values）
    #原始数据表属性创建
    first = plan_split['选考要求'].values
    #选考标识属性创建
    tool = tool_table._ixs(0)
    tool_dili = tool_table['地'].values
    tool_huaxue = tool_table['化'].values
    tool_shengwu = tool_table['生'].values
    tool_lishi = tool_table['史'].values
    tool_wuli = tool_table['物'].values
    tool_zhengzhi = tool_table['政'].values

    kemu = ["地", "化", "生", "史", "物", "政"]
    zuhe = ["和", "或", "加"]
    xuanke = []
    for i in range(len(first)):
        zancun = []
        zancun_first = []
        zuhe_pipei = ''
        # print(first[i])
        for j in range(len(first[i])):
            if str(first[i]) == '不限':
                zancun_first.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
                break
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
                elif kemu.index(weizhi) == 3:
                    zancun_first.append(list(tool_lishi))
                elif kemu.index(weizhi) == 4:
                    zancun_first.append(list(tool_wuli))
                else:
                    zancun_first.append(list(tool_zhengzhi))


        if zuhe_pipei == "加":
            zancun.append(list(set(zancun_first[0]).intersection(*zancun_first[1:])))
        elif zuhe_pipei == "或":
            zancun.append(list(set(zancun_first[0]).union(*zancun_first[1:])))
        elif zuhe_pipei == "与":
            zancun.append(list(set(zancun_first[0]).intersection(*zancun_first[1:])))
        else:
            zancun.append(zancun_first)

        zancun[0].sort()
        xuanke.append(zancun[0])
    # 用来增加新表属性
    plan_split['选科标识'] = xuanke

    plan_split.to_excel(r"C:\Users\cy0007\Desktop\完成数据.xlsx",index=False)


read()
