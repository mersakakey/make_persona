import pandas as pd
import re

def text_to_list(persona_str):
    tmp = persona_str.replace("\n","").replace(':', '').replace(' ', '')
    persona_list = re.split("[\[\]]",tmp)[1:]

    #print(pre_process, persona_list)
    persona_name = []
    persona_value = []

    for i in range(len(persona_list)):
        if i%2 == 0:
            persona_name.append(persona_list[i])
        else:
            persona_value.append(persona_list[i])

    return persona_name, persona_value


def make_csvfile(persona_str_list):
    name = ""
    value_list = []

    for i in persona_str_list:
        if i == "error":
            continue

        persona_name, persona_value = text_to_list(i)

        
        print(persona_name,persona_value)

        if (persona_name == [] or persoma_value == []):
            continue

        if name == "":
            name = persona_name
        value_list.append(persona_value)
    
    if value_list == []:
        print("error")
        return 0

    df = pd.DataFrame(data = value_list, columns = name)

    csv = df.to_csv(index=False, encoding="utf-8_sig")  

    return csv


# make_csvfile(["""名前:高田健一
# 性別:男性
# 年齢:22歳
# 国籍:日本
# 住所:東京都渋谷区
# 学歴:名古屋大学 工学部情報工学科卒業
# 職業:エンジニア（AI系）
# 趣味:プログラミング、アウトドア活動、スポーツ観戦
# 特技:アルゴリズム設計、言語学習
# 収入:500万
# 既婚、未婚:未婚
# 家族構成:父、母、姉（25歳）
# """])
