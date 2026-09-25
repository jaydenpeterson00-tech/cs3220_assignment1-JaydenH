import streamlit as st
import streamlit.components.v1 as components

st.title("War of 5 Kings - Battle Network")

st.header("Task1. Building Interactive Network of battles of the War of 5 Kings")

with open("Lab1-task1-net5kings.html", "r", encoding="utf-8") as file:
    graph_html = file.read()

components.html(graph_html, height=1000, scrolling=True)