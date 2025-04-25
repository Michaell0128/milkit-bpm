
import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Milkit PM", layout="centered")

st.title("📋 Milkit PM - 프로젝트 등록")

with st.form("project_form"):
    project_name = st.text_input("프로젝트명", placeholder="예: 홍게 브랜딩")
    
    default_due = datetime.date.today() + datetime.timedelta(days=14)
    due_date = st.date_input("마감일", value=default_due)
    
    is_urgent = st.checkbox("⚡ 긴급 작업")
    
    memo = st.text_area("추가 메모", placeholder="프로젝트 관련 메모 입력")
    
    submitted = st.form_submit_button("✅ 등록하기")

if submitted:
    data = {
        "project_name": project_name,
        "due_date": str(due_date),
        "priority": "high" if is_urgent else "normal",
        "memo": memo
    }
    
    webhook_url = "https://hook.eu2.make.com/8arlaihj3oe2kw2xd3js5ehb96v4g2kn"
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 200:
        st.success("프로젝트가 성공적으로 등록되었습니다!")
    else:
        st.error("등록 실패! 다시 시도해주세요.")

st.markdown("---")
st.markdown("### 🎙️ 음성으로 입력하기 (추후 업데이트 예정)")
st.info("버튼을 눌러 음성으로 프로젝트를 등록하는 기능은 다음 버전에 제공됩니다.")
