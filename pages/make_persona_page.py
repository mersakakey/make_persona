import streamlit as st
from make_persona import make_persona
from make_csvfile import make_csvfile
import base64

if "outputs" not in st.session_state: 
  st.session_state.outputs = []

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')
  making_temperature= st.slider('要約のtemperature', 0.0, 2.0, 1.0,step=0.1)

with st.form("元情報からペルソナを作成"):
  persona = st.text_area(label="ペルソナ", height = 350, value =
"""[名前:]
[性別:]
[年齢:]
[国籍:]日本
[住所:]
[学歴:]
[職業:]
[趣味:]
[特技:]
[収入:]
[既婚、未婚:]
[家族構成:]
""")
  target = st.text_input(label = "ターゲット", placeholder = "例：22歳の新卒エンジニア")

  making_num= st.slider('作成数', 1, 5, 1,step=1)
  submitted = st.form_submit_button("ペルソナ作成")

csv = st.button(label = "csv出力")

if csv:
  if not st.session_state.outputs:
    st.warning('データがありません', icon='⚠')
  else:
    b64 = base64.b64encode(make_csvfile(st.session_state.outputs).encode()).decode()
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
    make_persona = make_persona(openai_api_key, transcription_temperature = making_temperature)
    for i in range(making_num):

      output = make_persona.predict(target = target, persona = persona)
      st.session_state.outputs.append(output)
    st.write(st.session_state.outputs)

st.write("outputs:" , len(st.session_state.outputs))
