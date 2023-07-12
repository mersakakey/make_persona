from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import re


class make_persona:
  def __init__(_self,  openai_api_key, transcription_temperature=0):

    _self.llm = OpenAI(
      temperature=transcription_temperature,
      openai_api_key=openai_api_key,
    )

  def predict(_self, target, persona):

    promptSubject = PromptTemplate(input_variables=["target", "persona"], template="""
# 命令書
あなたはプロのクラウドワーカーです。​下記の # ターゲット について調査しています。下記の # 制約条件 で # 出力形式 に忠実に従って[ペルソナ]を出力してください。

# ターゲット
[ターゲット]: "{target}"

# 制約条件
・[ペルソナ]は、[ターゲット]の属性を考慮して挙げてください。
・[ペルソナ]は、性別など人口統計学的属性や心理学的属性や行動学的属性や地理学的属性を考慮して挙げてください。
・[ペルソナ]の各項目は、論理矛盾や論理飛躍のないものにしてください。
・名前は一般的になりすぎないように注意してください。

# 出力形式
・出力の際には、下記の形式に従ってください。

—–

"{persona}"

""")

    chain = LLMChain(llm=_self.llm, prompt=promptSubject)

    result = chain.run(target = target, persona = persona)

    result = re.findall('"([^"]*)"',result)

    if result:
      return result[0]
    else:
      return "error"