import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 앱 설정 및 고급 폰트/스타일 ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

# 세션 상태 유지
if 'page' not in st.session_state: st.session_state.page = 'HOME'
if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    /* 요즘 유행하는 폰트 및 전체 배경색 개선 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Lexend:wght@700&family=Noto+Sans+KR:wght@400;700&display=swap');

    /* 전체 폰트 적용: 숏츠/유튜브 감성의 깔끔한 산세리프 */
    html, body, [class*="css"] {
        font-family: 'Inter', 'Noto Sans KR', sans-serif;
        background-color: #ffffff !important; /* 배경을 밝게 수정 */
        color: #1e293b;
    }

    /* 메인 컨테이너 배경 */
    .stApp {
        background-color: #ffffff;
    }

    /* 카드 디자인: 그림자를 부드럽게 하고 테두리를 밝게 */
    .card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #f1f5f9;
        margin-bottom: 20px;
    }

    /* 제목 스타일: 인스타/유튜브 숏츠 감성의 볼드한 서체 */
    .brand-title {
        font-family: 'Lexend', sans-serif;
        font-size: 3.2rem;
        font-weight: 800;
        color: #0f172a;
        text-align: center;
        letter-spacing: -2px;
        margin-top: 40px;
    }
    
    .brand-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        letter-spacing: 3px;
        margin-bottom: 40px;
        text-transform: uppercase;
    }

    /* 버튼 스타일: 둥글고 묵직한 요즘 스타일 */
    .stButton>button {
        border-radius: 12px;
        background-color: #0f172a;
        color: white;
        border: none;
        height: 54px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
        transform: translateY(-2px);
    }

    /* 하단 네비게이션 바 고정 */
    .nav-bar {
        position: fixed;
        bottom: 0; left: 0; right: 0;
        background-color: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-top: 1px solid #f1f5f9;
        display: flex;
        justify-content: space-around;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 정의 (내용 그대로 유지) ---
detailing_methods = {
    "중성 세차": "산성/알칼리 없이 도장면 오염물만 안전하게 제거하는 기초 방식",
    "2PH 세차": "알칼리(프리워시) -> 중성(카샴푸) 2단계 오염 제거",
    "3PH 세차": "알칼리 -> 산성 -> 중성 순서. 미네랄과 찌든 때 완벽 제거",
    "유막제거/발수": "산화세륨 오염 제거 후 불소계 코팅제로 시야 확보",
    "휠/타이어": "분진 제거 후 전용 광택제로 갈변 방지 및 코팅",
    "외장 왁스": "고체 왁스 또는 물왁스(LSP)로 광택 및 비딩 형성",
    "실내/시트": "클리너로 유분 제거 후 컨디셔너로 가죽 보습"
}

brands = {
    "라보코스메티카": "이탈리아 하이엔드, 3PH 세차 선두 (프리머스, 퓨리피카)",
    "코흐케미": "독일 프리미엄, 완성차 납품용 고성능 케미컬 (Gsf, Mw)",
    "기온쿼츠": "강력한 성능의 발수 코팅 라인업 (웨트코트, 아이언)",
    "더클래스/파이어볼": "국산 디테일링의 자존심, 극강의 가성비와 슬릭감"
}

# --- 3. 공통 함수 ---
def set_page(name): st.session_state.page = name

# --- 4. 메인 제목 ---
st.markdown("<div class='brand-title'>APEX POHANG</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>High-End Mobility Community</div>", unsafe_allow_html=True)

# --- 5. 페이지별 콘텐츠 ---

# [HOME]
if st.session_state.page == 'HOME':
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<div class='card'><h3>⛽ 실시간 오천읍 유가</h3>"
                    "<p style='font-size:1.1rem;'><b>휘발유:</b> 1,625원 | <b>경유:</b> 1,510원 | <b>고급유:</b> 1,890원</p>"
                    "<small style='color:gray;'>포항 남구 주유소 평균가 기준</small></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><h3>🌥️ 오천읍 기상 현황</h3>"
                    "<p style='font-size:1.1rem;'>현재 풍속: <b style='color:#3b82f6;'>3.2m/s</b> (세차 적합)<br>강수확률: 10% | 현재 온도: 5.2°C</p></div>", unsafe_allow_html=True)
    with col2:
        if st.button("🧪 희석 비율 계산기"): set_page('CALC')
        st.write("")
        if st.button("🧼 디테일링 가이드"): set_page('GUIDE')
        st.write("")
        if st.button("🍔 주변 맛집/카페"): set_page('FOOD')

# [CALC] 
elif st.session_state.page == 'CALC':
    st.subheader("🧪 케미컬 희석 계산기")
    with st.container():
        total_vol = st.number_input("만들고 싶은 총 용량 (ml)", value=1000)
        ratio = st.number_input("희석 비율 (1 : N 에서 N값)", value=10)
        chemical = total_vol / (ratio + 1)
        water = total_vol - chemical
        st.success(f"결과: 원액 {chemical:.1f}ml + 물 {water:.1f}ml를 섞으세요.")
    if st.button("홈으로 돌아가기"): set_page('HOME')

# [GUIDE]
elif st.session_state.page == 'GUIDE':
    st.subheader("📚 디테일링 백과사전")
    tab1, tab2 = st.tabs(["✅ 세차 공법", "🧴 추천 브랜드"])
    with tab1:
        for m, d in detailing_methods.items():
            with st.expander(m): st.write(d)
    with tab2:
        for b, d in brands.items():
            st.markdown(f"**[{b}]** {d}")
    if st.button("홈으로 돌아가기"): set_page('HOME')

# [FOOD]
elif st.session_state.page == 'FOOD':
    st.subheader("🍴 문덕/오천 맛집")
    st.markdown("""
    <div class='card'>
    <b>📍 인더그레이</b>: 문덕 핫플 카페<br>
    <b>📍 뚝배기 주물럭</b>: 오천 현지인 맛집<br>
    <b>📍 미사동커피</b>: 세차 후 커피 한 잔
    </div>
    """, unsafe_allow_html=True)
    if st.button("홈으로 돌아가기"): set_page('HOME')

# [COMMUNITY]
elif st.session_state.page == 'COMMUNITY':
    st.subheader("💬 멤버 자유게시판")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("닉네임")
        content = st.text_area("세차 후기 및 일상 공유")
        rating = st.select_slider("오늘의 만족도", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
        if st.form_submit_button("글 쓰기"):
            st.session_state.posts.append({"name": name, "content": content, "rating": rating, "date": datetime.now().strftime("%m/%d %H:%M")})
    
    for p in reversed(st.session_state.posts):
        st.markdown(f"<div class='card'><b>{p['name']}</b> <small>{p['date']}</small><br>{p['rating']}<br>{p['content']}</div>", unsafe_allow_html=True)
    if st.button("홈으로 돌아가기"): set_page('HOME')

# --- 6. 하단 네비게이션 ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
n1, n2, n3, n4, n5 = st.columns(5)
with n1: st.button("🏠\nHOME", on_click=set_page, args=('HOME',))
with n2: st.button("🧼\nLAB", on_click=set_page, args=('GUIDE',))
with n3: st.button("🧪\nCALC", on_click=set_page, args=('CALC',))
with n4: st.button("💬\nTALK", on_click=set_page, args=('COMMUNITY',))
with n5: st.markdown("<a href='https://naver.me/F6lTwCXz' target='_blank'><button style='width:100%; height:54px; border-radius:12px; background:#00c73c; color:white; border:none; font-weight:700;'>📍\nMAP</button></a>", unsafe_allow_html=True)
