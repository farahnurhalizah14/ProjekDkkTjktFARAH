import streamlit as st
import time

st.title("⏱️ Timer")

m = st.number_input("Masukkan menit:", min_value=0, value=0)
d = st.number_input("Masukkan detik:", min_value=0, value=10)

if st.button("Mulai Timer"):
    total_seconds = m * 60 + d

    placeholder = st.empty()

    for i in range(total_seconds, -1, -1):
        mins, secs = divmod(i, 60)
        timer_text = f"{mins:02d}:{secs:02d}"

        placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 80px;'>{timer_text}</h1>",
            unsafe_allow_html=True
        )

        time.sleep(1)

    st.success("⏰ Waktu Habis!")
