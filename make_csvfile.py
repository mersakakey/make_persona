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
        persona_name, persona_value = text_to_list(i)

        print(persona_name,persona_value)

        if name == "":
            name = persona_name
        value_list.append(persona_value)

    df = pd.DataFrame(data = value_list, columns = name)

    csv = df.to_csv(index=False, encoding="utf-8_sig")  

    return csv

    
#make_csvfile(["[名前:] アレックス [性別:] 男性 [年齢:] 22歳 [国籍:] 日本 [住所:] 東京都 [学歴:] 大学卒業 [職業:] エンジニア [役職:] 新卒 [収入:] 時給制 [既婚、未婚:] 未婚 [家族構成:] 両親と2人の兄弟 [友人の数:] 10人","[名前:] アレックス [性別:] 男性 [年齢:] 22歳 [国籍:] 日本 [住所:] 東京都 [学歴:] 大学卒業 [職業:] エンジニア [役職:] 新卒 [収入:] 時給制 [既婚、未婚:] 未婚 [家族構成:] 両親と2人の兄弟 [友人の数:] 10人"])

