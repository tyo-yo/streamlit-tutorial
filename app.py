import time

import numpy as np
import pandas as pd
import streamlit as st

st.title("タイトル")

st.write("st.writeを使えばなんでもいい感じに表示できる")
st.write(pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}))

"""
# マークダウンでタイトル書ける
## サブタイトル
Jupyterみたいにただ値を返すだけでいい感じに表示してくれる
"""

df = pd.DataFrame({"first column": [1, 2, 5, 8], "second column": [10, 20, 20, 40]})

df

"## st.line_chart(df)でグラフ"

st.line_chart(df)


"## if st.checkbox でチェックボックス"
if st.checkbox("チェックすると中身が表示されるよ"):
    st.write(df)


"## リストから何かを選ぶにはst.selectbox"
option = st.selectbox("Which number do you like best?", df["first column"])

"You selected: ", option

"## st.sidebar.selectboxでサイドバーで選択"
option = st.sidebar.selectbox("Which number do you like best?", [1, 2, 3])

"サイドバーで選んだ数字の2倍は？:", option * 2


"## ベータの機能だけど2カラムとかexpandとかできる"
left_column, right_column = st.beta_columns(2)
pressed = left_column.button("Press me?")
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


"## 長い計算の進捗はst.progressで簡単表示"


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

"...and now we're done!"


with st.echo():
    st.write("This code will be printed")


with st.spinner("Wait for it..."):
    time.sleep(5)
st.success("Done!")
st.balloons()
