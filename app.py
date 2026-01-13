import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 스타일 설정 (이미지의 화이트 UI & 3열 레이아웃 재현) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'HOME'
if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 배경 및 기본 폰트 설정 */
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        background-color: #f8f9fa !important;
        color: #1e293b;
    }

    /* 카드 디자인 (이미지처럼 둥글고 깨끗하게) */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.03);
        margin-bottom: 20px;
        border: 1px solid #eef0f2;
    }

    /* 텍스트 시인성 확보 */
    h1, h2, h3, p { color: #1e293b !important; }
    .label-blue { color: #3b82f6; font-size: 12px; font-weight: 700; margin-bottom: 5px; }
    .label-orange { color: #ff8a3d; font-size: 12px; font-weight: 700; margin-bottom: 5px; }

    /* 버튼 스타일 (트렌디한 볼드 스타일) */
    .stButton>button {
        border-radius: 12px;
        background-color: #ffffff;
        color: #1e293b;
        border: 1px solid #e2e8f0;
        font-weight: 700;
        height: 54px;
        width: 100%;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #f1f5f9;
        border-color: #3b82f6;
    }

    /* 이미지 상단 로고 영역 */
    .brand-area { display: flex; align-items: center; gap: 15px; padding: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 헤더 (이미지 왼쪽 상단 재현) ---
st.markdown("""
    <div class="brand-area">
        <img src="https://img.icons8.com/bubbles/100/car.png" width="60">
        <div>
            <h1 style='margin:0; font-size:24px; font-weight:800;'>APEX POHANG</h1>
            <p style='margin:0; color:#64748b !important; font-size:14px;'>오천 버블스타 크루 전용 스마트 라운지</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. 메인 콘텐츠 (이미지처럼 3분할) ---
left, mid, right = st.columns([1, 1, 1])

# [왼쪽 열: 날씨/유가/맛집]
with left:
    st.markdown("### 🌤️ 실시간 정보")
    # 날씨 카드
    st.markdown("""
        <div class="card">
            <p class="label-blue">Weather Alert</p>
            <p style="font-size:20px; font-weight:800; margin:0;">포항 오천읍 5.2°C</p>
            <p style="font-size:14px; margin:0;">풍속: 3.2m/s (세차 적합 ✨)</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 유가 카드
    st.markdown("""
        <div class="card">
            <p class="label-orange">Oil Price</p>
            <p style="font-size:14px; margin:5px 0;">⛽ 휘발유: 1,625원</p>
            <p style="font-size:14px; margin:5px 0;">⛽ 경유: 1,510원</p>
            <p style="font-size:14px; margin:5px 0;">⛽ 고급유: 1,890원</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 맛집 가이드
    with st.expander("🍴 주변 맛집/카페 소개"):
        st.write("📍 **인더그레이**: 문덕 핫플레이스 카페")
        st.write("📍 **뚝배기 주물럭**: 오천읍 현지인 맛집")
        st.write("📍 **미사동커피**: 세차 후 휴식 추천")

# [가운데 열: 세차 가이드 및 계산기]
with mid:
    st.markdown("### 🧼 디테일링 LAB")
    tab1, tab2, tab3 = st.tabs(["세차 공법", "희석 계산기", "추천 용품"])
    
    with tab1:
        st.markdown("""
        **1. 3PH 세차**: 알칼리-산성-중성 3단계 케어<br>
        **2. 유막제거/발수**: 시야 확보 필수 공정<br>
        **3. 휠/타이어**: 갈변 제거 및 드레싱 코팅<br>
        **4. 실내/시트**: 가죽 세정 및 보습 관리<br>
        **5. 외장 왁스**: 고체왁스/LSP 광택 마무리
        """, unsafe_allow_html=True)

    with tab2:
        total = st.number_input("목표 용량(ml)", value=1000, step=100)
        ratio = st.number_input("희석 비율 (1:N)", value=10, step=1)
        res = total / (ratio + 1)
        st.success(f"원액 **{res:.1f}ml** + 물 **{total-res:.1f}ml**")

    with tab3:
        st.info("라보코스메티카, 코흐케미, 기온쿼츠 등 메니아 추천 용품 수록")

# [오른쪽 열: 지도 및 게시판]
with right:
    st.markdown("### 💬 소통과 위치")
    # 지도 카드
    st.markdown("""
        <div class="card">
            <p style="font-weight:800; margin-bottom:5px;">오천 버블스타 세차장</p>
            <p style="color:#64748b !important; font-size:13px;">경북 포항시 남구 오천읍 문덕로79번길 26</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<a href='https://naver.me/F6lTwCXz' style='text-decoration:none;'><div style='background-color:#00c73c; color:white; text-align:center; padding:12px; border-radius:12px; font-weight:bold;'>N 네이버 지도로 보기</div></a>", unsafe_allow_html=True)
    
    st.write("")
    # 실시간 게시판 미리보기
    st.markdown("<b>최신 후기</b>", unsafe_allow_html=True)
    for p in reversed(st.session_state.posts[-2:]):
        st.markdown(f"<div class='card' style='padding:10px; font-size:13px;'><b>{p['name']}</b>: {p['content']} {p['rating']}</div>", unsafe_allow_html=True)

# --- 4. 하단 네비게이션 (이미지 하단바 재현) ---
st.markdown("<div style='margin-top:50px;'></div>", unsafe_allow_html=True)
n1, n2, n3, n4 = st.columns(4)
with n1: 
    if st.button("🏠\n홈"): st.session_state.page = 'HOME'
with n2: 
    if st.button("💬\n라운지"): st.session_state.page = 'BOARD'
with n3: 
    if st.button("🧪\n계산기"): st.session_state.page = 'HOME' # 홈의 탭으로 이동
with n4: 
    st.button("👤\n마이")

# 자유게시판 섹션 (라운지 클릭 시 하단에 등장)
if st.session_state.page == 'BOARD':
    st.divider()
    st.subheader("💬 자유게시판")
    with st.form("board_form"):
        u_name = st.text_input("닉네임")
        u_content = st.text_area("세차 결과 및 일상 공유")
        u_rate = st.select_slider("오늘의 만족도", options=["⭐","⭐⭐","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"])
        if st.form_submit_button("등록하기"):
            st.session_state.posts.append({"name":u_name, "content":u_content, "rating":u_rate})
            st.rerun()
