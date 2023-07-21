import pandas as pd
import re

def text_to_list(persona_str):
    persona_list = re.split("[\n\:]",persona_str)

    #print(pre_process, persona_list)
    persona_name = []
    persona_value = []

    for i in range(len(persona_list)):
        if i%2 == 0:
            persona_name.append(persona_list[i])
        else:
            persona_value.append(persona_list[i].strip(" "))

    return persona_name, persona_value


def make_csvfile(persona_str_list):
    name = ""
    value_list = []

    for i in persona_str_list:
        if i == "error":
            continue

        persona_name, persona_value = text_to_list(i)

        if (persona_name == [] or persona_value == []):
            continue

        if name == "":
            name = persona_name
        value_list.append(persona_value)
    
    if value_list == []:
        print("error")

    if "" in name:
        name.remove("")

    df = pd.DataFrame(data = value_list, columns = name)

    csv = df.to_csv(index=False, encoding="utf-8_sig")  

    return csv


# #ifDEBUG
# print(make_csvfile(["""名前:高田健一
# 性別:男性
# 年齢:22歳
# 国籍:日本
# 家族構成:父、母、姉（25歳）
# """]))
# #endif