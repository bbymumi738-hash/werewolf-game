
import streamlit as st

def initialize_game(players):
    st.session_state.players = {p: {"role": None, "alive": True} for p in players}
    st.session_state.phase = "Night"
    st.session_state.winner = None

def get_alive_players():
    return [p for p, data in st.session_state.players.items() if data["alive"]]
