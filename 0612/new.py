import pandas as pd
import numpy as np

data = pd.read_csv("工作簿1.csv", encoding="gbk")
data = np.array(data)

list_final = []

for b in data:
    json1 = {"q":b[0],"a":b[1]}
    q_list = json1["q"].split("\\n")
    a_list = json1["a"].split(" ")

    indices = []
    for i in q_list:
        # print(i)

        for j in a_list:

            # print(j)
            index = i.find(j)
            if index != -1:
                indices.append({"q": i, "a": j})
    # print(indices)

    merged_dict = {}

    # 遍历原始列表中的每个字典
    for d in indices:
        # 获取字典的key值
        key = d["q"]

        # 如果该key值已经存在于合并后的字典中，则将其对应的value值拼接起来
        if key in merged_dict:
            merged_dict[key]["a"] += " " + d["a"]
            # 如果该key值不存在于合并后的字典中，则将其作为新的字典添加到合并后的字典中
        else:
            merged_dict[key] = d.copy()
            merged_dict[key]["a"] = d["a"]

    merged_lst = list(merged_dict.values())
    # merged_lst = list(set(merged_lst))
    # merged_lst = list(dict.fromkeys(merged_lst))

    for i in merged_lst:
        dat = i["a"].split(" ")
        print("dat",dat)
        dt = list(sorted(set(dat),key=dat.index))
        print(dt)
        data = ""
        for j in dt:
            data += j
        i["a"] = data
        list_final.append(i)

for d in list_final:
    if d["a"] == "":
        d["a"] = "无"
    print(d)

if __name__ == '__main__':
    a = pd.to_csv("train.csv",encoding="utf-8")
