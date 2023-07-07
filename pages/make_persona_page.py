import streamlit as st
from make_persona import make_persona
from make_csvfile import make_csvfile
import base64

outputs = []

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')
  making_temperature= st.slider('要約のtemperature', 0.0, 2.0, 0.0,step=0.1)

with st.form("元情報からペルソナを作成"):
  persona = st.text_area(label="ペルソナ", height = 350, value =
"""[名前:]
[性別:]
[年齢:]
[国籍:]
[住所:]
[学歴:]
[職業:]
[役職:]
[収入:]
[既婚、未婚:]
[家族構成:]
[友人の数:]""")
  target = st.text_input(label = "ターゲット", placeholder = "例：22歳の新卒エンジニア")

  submitted = st.form_submit_button("ペルソナ作成")

csv = st.button(label = "csv出力")

if csv:
    print(outputs)
    b64 = base64.b64encode(make_csvfile(outputs).encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="result_utf-8.csv">Download Link</a>'
    st.markdown(f"CSVファイルのダウンロード(utf-8):  {href}", unsafe_allow_html=True)

if submitted:
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API keyを入力してください', icon='⚠')
  if not persona:
    st.warning('作成したいペルソナのテンプレートを入力してください', icon='⚠')
  if not target:
    st.warning('ターゲットを入力してください', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    print(target , persona)
    make_persona = make_persona(openai_api_key, transcription_temperature = making_temperature)

    output = make_persona.predict(target = target, persona = persona)
    print(output)
    st.write(output)
    outputs.append(output)
