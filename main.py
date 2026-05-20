import streamlit as st

st.title('잠자고싶다 웹앱')
st.write('안녕하세요!!😁')

# 추가 기능 예시
st.header('오늘의 수면 시간')
sleep_time = st.slider('수면 시간을 선택하세요 (시간)', 0, 12, 8)
st.write(f'목표 수면 시간: {sleep_time}시간 😴')
