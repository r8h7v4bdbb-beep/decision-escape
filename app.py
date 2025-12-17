import streamlit as st

st.set_page_config(page_title="Decision Escape", page_icon="🎮")

st.title("🎮 Decision Escape")
st.write("결정장애를 게임처럼 해결하는 웹앱입니다.")

st.subheader("🍽 오늘 점심 뭐 먹지?")
choice = st.selectbox(
    "하나만 골라!",
    ["김치볶음밥", "제육덮밥", "돈까스", "냉면", "마라탕"]
)

if st.button("결정 완료"):
    st.success(f"👉 오늘의 선택: {choice}")
