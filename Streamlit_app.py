
import streamlit as st
from game import initialize_game
from night import run_night
from vote import run_vote

st.title("เกมมนุษย์หมาป่า (werewolf Game)")

if 'players' not in st.session_state:
    players_input = st.text_input("ใส่ชื่อผู้เล่น (คั่นด้วยคอมมา):")
    if st.button("เริ่มเกม"):
        players = [p.strip() for p in players_input.split(",")]
        initialize_game(players)
        st.rerun()
else:
    st.write(f"สถานะเกม: {st.session_state.phase}")
    if st.session_state.phase == "Night":
        run_night()
    else:
        run_vote()
