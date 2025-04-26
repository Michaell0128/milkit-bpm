
import streamlit as st
import requests
import datetime

st.title("Milkit BPM 프로젝트 등록 폼")

# 입력 폼 생성
with st.form("bpm_form"):
    project_name = st.text_input("프로젝트명")
    due_date = st.date_input("마감일", min_value=datetime.date.today())
    priority = st.checkbox("긴급 여부")

    submitted = st.form_submit_button("등록하기")

    if submitted:
        data = {
            "projectName": project_name,
            "dueDate": due_date.strftime("%Y-%m-%d"),
            "priority": priority
        }
        response = requests.post(
            'https://hook.eu2.make.com/p82nvibohha7zv1nzojlssfcryzmer3q',
            json=data
        )
        if response.status_code == 200:
            st.success("프로젝트가 성공적으로 등록되었습니다!")
        else:
            st.error("등록 실패. 다시 시도해주세요.")

st.markdown("---")
st.button("🎤 음성인식으로 입력 (준비중)")
st.caption("버전2에 업데이트 예정")
