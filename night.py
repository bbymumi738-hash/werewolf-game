
import streamlit as st

def run_night():
    st.write("### ช่วงเวลากลางคืน")
    st.write("Mafia กำลังเลือกว่าจะฆ่าใคร...")
    # Logic สำหรับให้ Mafia เลือกเหยื่อ
    target = st.selectbox("เลือกผู้เล่นที่จะกำจัด:", [p for p in st.session_state.players if st.session_state.players[p]["alive"]])
    if st.button("ยืนยันการฆ่า"):
        st.session_state.players[target]["alive"] = False
        st.session_state.phase = "Vote"
        st.rerun()
