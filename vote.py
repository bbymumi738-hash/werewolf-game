
import streamlit as st

def run_vote():
    st.write("### ช่วงเวลาโหวต")
    # Logic สำหรับโหวตคนออก
    vote = st.selectbox("ใครคือคนร้าย?", [p for p in st.session_state.players if st.session_state.players[p]["alive"]])
    if st.button("โหวต"):
        st.write(f"คุณโหวต {vote}")
        st.session_state.phase = "Night"
        st.rerun()
