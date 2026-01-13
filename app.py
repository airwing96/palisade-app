import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 스타일 설정 (이미지의 깔끔한 화이트/그레이 톤 재현) ---
st.set_page_config(page_title="팰리 당근 모임", page_icon="🥕", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    /* 카드 디자인 */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border: 1px solid #eee;
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #ff8a3d;
        color: white;
        border: none;
        width: 100%;
    }
    /* 타이틀 스타일 */
    .title-text { font-size: 22px; font-weight: bold; color: #333; margin-bottom: 15px; }
    .sub-text { font-size: 14px; color: #666; }
    /* 가이드 리스트 아이템 */
    .guide-item {
        display: flex;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 헤더 (이미지 상단 로고 부분) ---
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/bubbles/100/car.png", width=80)
    st.markdown("<h2 style='margin-bottom:0;'>필시스도 당갈 민임</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray;'>우리 모임 마트</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- 3. 메인 레이아웃 (3열 구성) ---
left_col, mid_col, right_col = st.columns([1, 1, 1])

# --- 왼쪽 열: 벙개 및 날씨 ---
with left_col:
    st.markdown('<p class="title-text">📅 벙개 만오</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="card">
            <p style='font-weight:bold; color:#ff8a3d;'>초보 기스</p>
            <p class="sub-text">진행 중인 벙개 <span style='float:right;'>✅</span></p>
            <hr>
            <p class="sub-text">징게 민로 <span style='float:right;'>진행 뭉룬 미로</span></p>
        </div>
        """, unsafe_allow_html=True)
        st.button("벙개 참여하기")

# --- 가운데 열: 세차 가이드 (이미지의 리스트 형태) ---
with mid_col:
    st.markdown('<p class="title-text">🥕 세차 가이드</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style='font-weight:bold;'>오늘의 세차 지수</p>
        <p class="sub-text">☀️ 맛밤부랄 시 세각식 솔룬</p>
        <p style='color:#007bff; font-size:12px;'>니슨메먼랏른 지민 linke</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab_1, tab_2, tab_3 = st.tabs(["초보 가이드", "무선 세공", "우컴 민 가보"])
    with tab_1:
        guides = [
            ("🧼 임엔 풍설 세차", "조진 유쾌한 세차"),
            ("🚗 무택 커셀의 세 저음비", "태어난 뒤 첫원"),
            ("🧪 3PH 치차뿔", "유복제토 의 밥슬 코로")
        ]
        for title, desc in guides:
            st.markdown(f"""
            <div class="guide-item">
                <div style="margin-right:15px; font-size:24px;">📦</div>
                <div>
                    <div style="font-weight:bold; font-size:14px;">{title}</div>
                    <div style="font-size:12px; color:gray;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- 오른쪽 열: 용품 백과 및 후기 ---
with right_col:
    st.markdown('<p class="title-text">🔍 세차용품 백과소터</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="card">
            <div style="display:flex; justify-content:space-between;">
                <span>🧴 임헬 옹썸 세차</span>
                <span style="color:gray;">조뒷기리</span>
            </div>
            <p class="sub-text" style="margin-top:5px;">조보 범척 세차</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<p class="title-text">📸 세차용품 후위</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div style="display:flex;">
            <div style="background-color:#eee; width:60px; height:60px; border-radius:10px; margin-right:10px;"></div>
            <div>
                <p style="margin-bottom:0; font-weight:bold; font-size:14px;">AI 새뱍 시지칸장</p>
                <p style="font-size:12px; color:gray;">연인올썸 줄 읽기 ⭐⭐⭐⭐(38)</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. 하단 네비게이션 바 (시각적 재현) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="display: flex; justify-content: space-around; background-color: white; padding: 10px; border-top: 1px solid #ddd; position: fixed; bottom: 0; left: 0; right: 0; z-index: 100;">
        <div style="text-align:center; color:#ff8a3d;">🏠<br><span style="font-size:10px;">홈/주방</span></div>
        <div style="text-align:center; color:gray;">📋<br><span style="font-size:10px;">무선산림</span></div>
        <div style="text-align:center; color:gray;">💬<br><span style="font-size:10px;">코판 사싯</span></div>
        <div style="text-align:center; color:gray;">👤<br><span style="font-size:10px;">코판 백일</span></div>
    </div>
    """, unsafe_allow_html=True)
