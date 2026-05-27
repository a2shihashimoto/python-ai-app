"""診断用 最小アプリ"""
import sys
import streamlit as st

st.set_page_config(page_title="診断")
st.title("✅ Streamlit 起動確認")
st.write(f"Python バージョン: `{sys.version}`")
st.success("Streamlit は正常に起動しています！")
