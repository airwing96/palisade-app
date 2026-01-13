import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 스타일 설정 (이미지의 화이트 UI 재현) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'HOME'
if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    /* 폰트: 요즘 유행하는 Pretendard 스타일 */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, sans-serif;
        background-color: #f2f4f7 !important; /* 이미지의 연한 그레이 배경 */
    }

    /* 카드 디자인 (이미지의 둥근 모서리 재현) */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02);
        margin-bottom: 15px;
        border: 1px solid #e9ecef;
    }

    /* 제목 스타일 (숏츠 감성 볼드) */
    .header-text {
        font-size: 24px;
        font-weight: 800;
        color: #1a1a1a;
        margin-bottom: 10px;
    }

    /* 하단 네비게이션 (이미지의 하단바 재현) */
    .stButton>button {
        border-radius: 12px;
        background-color: #ffffff;
        color: #495057;
        border: 1px solid #e9ecef;
        font-weight: 700;
        height: 50px;
    }
    
    /* 강조 버튼 (세차장 길찾기 등) */
    .highlight-button {
        background-color: #3b82f6 !important;
        color: white !important;
        border: none !important;
    }

    /* 아이콘 스타일 */
    .icon-box {
        font-size: 24px;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 브랜딩 영역 ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://img.icons8.com/bubbles/100/car.png", width=70)
with col_title:
    st.markdown("<h1 style='margin:0; font-size:28px;'>APEX POHANG</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray; font-size:14px; margin:0;'>오천 버블스타 크루 전용 스마트 라운지</p>", unsafe_allow_html=True)

st.write("") # 간격 조절

# --- 3. 메인 레이아웃 (이미지처럼 3열 구성) ---
left_col, mid_col, right_col = st.columns([1, 1, 1])

# [왼쪽 열: 홈 및 유가 정보]
with left_col:
    st.markdown('<p class="header-text">🌤️ 실시간 오천읍</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <p style="color:#3b82f6; font-size:12px; font-weight:700;">Weather Alert</p>
            <p style="font-size:18px; font-weight:800; margin:0;">풍속 3.2m/s | 5.2°C</p>
            <p style="color:gray; font-size:12px;">세차 지수: 매우 좋음 ✨</p>
        </div>
        <div class="card">
            <p style="color:#ff8a3d; font-size:12px; font-weight:700;">Oil Price</p>
            <p style="font-size:15px; margin:0;">휘발유: 1,625원</p>
            <p style="font-size:15px; margin:0;">경유: 1,510원</p>
        </div>
    """, unsafe_allow_html=True)

# [가운데 열: 세차 가이드 및 계산기]
with mid_col:
    st.markdown('<p class="header-text">🧼 디테일링 LAB</p>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["세차 공법", "희석 계산기"])
    
    with tab1:
        methods = ["3PH 세차 (알칼리/산성/중성)", "유막제거 및 발수코팅", "휠/타이어 정밀 케어", "실내 가죽 시트 코팅"]
        for m in methods:
            st.markdown(f"<div class='card' style='padding:12px; font-size:14px; font-weight:600;'>{m}</div>", unsafe_allow_html=True)
            
    with tab2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        total = st.number_input("총량(ml)", value=1000, step=100)
        ratio = st.number_input("비율(1:N)", value=10, step=1)
        st.info(f"원액: {total/(ratio+1):.1f}ml 필요")
        st.markdown("</div>", unsafe_allow_html=True)

# [오른쪽 열: 커뮤니티 및 지도]
with right_col:
    st.markdown('<p class="header-text">💬 소통과 지도</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <p style="font-weight:800; margin-bottom:5px;">오천 버블스타 세차장</p>
            <p style="color:gray; font-size:12px;">경북 포항시 남구 오천읍 문덕로79번길 26</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<a href='https://naver.me/F6lTwCXz' style='text-decoration:none;'><div style='background-color:#00c73c; color:white; text-align:center; padding:12px; border-radius:12px; font-weight:bold; margin-bottom:20px;'>N 네이버 지도로 보기</div></a>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:14px; font-weight:700;'>최신 후기</p>", unsafe_allow_html=True)
    for p in reversed(st.session_state.posts[-2:]): # 최근 2개만 노출
        st.markdown(f"<div class='card' style='font-size:12px;'><b>{p['name']}</b>: {p['content']} {p['rating']}</div>", unsafe_allow_html=True)

# --- 4. 하단 네비게이션바 (이미지 하단 메뉴 재현) ---
st.markdown("<div style='margin-top:100px;'></div>", unsafe_allow_html=True)
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button("🏠\n홈"): st.session_state.page = 'HOME'
with nav_col2:
    if st.button("🧪\n계산기"): st.session_state.page = 'CALC'
with nav_col3:
    if st.button("💬\n라운지"): st.session_state.page = 'COMMUNITY'
with nav_col4:
    if st.button("👤\n마이"): st.session_state.page = 'MY'

# 페이지 이동 처리
if st.session_state.page == 'COMMUNITY':
    st.divider()
    with st.form("board"):
        u_name = st.text_input("닉네임")
        u_content = st.text_area("내용")
        u_rate = st.select_slider("만족도", options=["⭐","⭐⭐","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"])
        if st.form_submit_button("등록"):
            st.session_state.posts.append({"name":u_name, "content":u_content, "rating":u_rate})
            st.rerun()
