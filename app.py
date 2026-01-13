import streamlit as st
import pandas as pd

# --- 1. 앱 설정 및 고급 스타일 ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

# 세션 상태 초기화 (페이지 이동 및 게시판 저장용)
if 'page' not in st.session_state: st.session_state.page = 'HOME'
if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { border-radius: 10px; font-weight: 600; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #eee; margin-bottom: 15px; }
    .brand-title { font-size: 2.5rem; font-weight: 800; color: #0f172a; text-align: center; letter-spacing: -1px; }
    .info-label { color: #3b82f6; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 정의 (세차법, 용품, 맛집) ---
detailing_methods = {
    "중성 세차": "산성/알칼리 없이 도장면 오염물만 안전하게 제거하는 가장 기초적인 세차 방식",
    "2PH 세차": "알칼리(프리워시) -> 중성(카샴푸) 2단계로 나누어 오염물 제거 효율을 극대화",
    "3PH 세차": "알칼리 -> 산성 -> 중성 순서로 진행. 미네랄과 찌든 때를 완벽히 제거하는 매니아 공법",
    "유막제거/발수": "산화세륨으로 유리막 오염 제거 후 불소계 코팅제로 빗길 시야 확보",
    "휠/타이어": "철분제거제로 분진 제거 후 타이어 전용 광택제로 갈변 방지 및 광택",
    "외장 왁스": "고체 왁스 또는 물왁스(LSP)를 이용한 광택 및 비딩(Beading) 형성",
    "실내/시트": "가죽 전용 클리너로 유분 제거 후 컨디셔너로 갈라짐 방지 및 보습"
}

brands = {
    "라보코스메티카": "이탈리아 하이엔드, 3PH 세차 공법의 선두주자 (프리머스, 퓨리피카)",
    "코
