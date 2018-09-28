# codeing = utf-8
import json

# 定义函数
def jq_print(ajq):
    print(ajq["UnitID"], ajq["UnitName"], ajq["Zone"], ajq["Address"])

##############################################################

# 遍历字典 函数
def dict_print(dict):
    # 遍历所有属性
    for key, val in dict.items():
        print(key, "=", val)
        # print(key, "\t=", val)

    # 遍历所有key
    for key in dict.keys():
        print(key, " is ", dict[key])

    # 遍历所有的值
    for val in dict.values():
        print(val)

##############################################################

print("编号", "景区名", "区号", "地址")
filename = "zjAjq_id_info.json"

# json对象读出
with open(filename, "r", encoding="utf-8") as myfile:
    myjson = json.load(myfile)
    for ajq in myjson:
        jq_print(ajq)

    # dict_print(myjson[0])