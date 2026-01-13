import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 정밀 스타일 가이드 (어떤 환경에서도 시인성 100% 보장) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    /* 웹 폰트 로드: Pretendard (가장 트렌디하고 가독성 좋은 폰트) */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    /* [핵심] 배경색 및 모든 글자색 강제 고정 (다크모드 방지) */
    html, body, [class*="css"], .stApp {
        background-color: #F5F7FA !important; /* 부드러운 화이트 그레이 */
        font-family: 'Pretendard', -apple-system, sans-serif !important;
    }

    /* 모든 텍스트 기본색을 아주 진한 네이비로 고정하여 시인성 확보 */
    h1, h2, h3, h4, p, span, div, label {
        color: #1A202C !important;
        letter-spacing: -0.02em !important;
    }

    /* 카드 디자인: Apple 스타일의 둥근 모서리와 미세한 그림자 */
    .app-card {
        background-color: #FFFFFF !important;
        border-radius: 24px !important;
        padding: 24px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.04) !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 20px !important;
    }

    /* 상단 타이틀 섹션 */
    .brand-header {
        text-align: center;
        padding: 40px 0 20px 0;
    }
    .brand-name {
        font-size: 36px !important;
        font-weight: 900 !important;
        color: #0F172A !important;
        margin-bottom: 5px !important;
    }
    .brand-tagline {
        font-size: 15px !important;
        color: #64748B !important;
        font-weight: 500 !important;
    }

    /* 탭 메뉴 스타일링 (선명하게) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        font-weight: 700 !important;
        font-size: 16px !important;
        color: #94A3B8 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #3B82F6 !important;
        border-bottom-color: #3B82F6 !important;
    }

    /* 버튼 스타일 (홍보용 고퀄리티) */
    .stButton > button {
        width: 100%;
        border-radius: 16px !important;
        border: none !important;
        background: #1A202C !important;
        color: white !important;
        font-weight: 700 !important;
        height: 56px !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        background: #3B82F6 !important;
        transform: translateY(-2px);
    }

    /* 인풋 박스 시인성 */
    .stTextInput input, .stTextArea textarea {
        background-color: #F8FAFC !important;
        border-radius: 12px !important;
        border: 1px solid #E2E8F0 !important;
        color: #1A202C !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 브랜딩 섹션 ---
st.markdown("""
    <div class="brand-header">
        <div class="brand-name">APEX POHANG</div>
        <div class="brand-tagline">오천 버블스타 크루 전용 스마트 라운지</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. 메인 레이아웃 (3열 정밀 구성) ---
col1, col2, col3 = st.columns([1, 1.2, 1], gap="large")

# [COLUMN 1: 실시간 정보]
with col1:
    st.markdown("<h4>🌤️ 실시간 오천읍</h4>", unsafe_allow_html=True)
    
    # 날씨 카드
    st.markdown("""
        <div class="app-card">
            <p style="color:#3B82F6 !important; font-weight:800; font-size:13px; margin-bottom:10px;">WEATHER ALERT</p>
            <h2 style="font-size:28px !important; font-weight:800; margin:0;">5.2°C</h2>
            <p style="font-size:16px; margin:5px 0;">풍속: <b>3.2m/s</b> (세차 적합 ✨)</p>
            <p style="font-size:13px; color:#64748B !important;">강수확률 10% | 습도 45%</p>
        </div>
    """, unsafe_allow_html=True)

    # 유가 카드
    st.markdown("""
        <div class="app-card">
            <p style="color:#F59E0B !important; font-weight:800; font-size:13px; margin-bottom:10px;">GAS PRICE</p>
            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <span>휘발유</span><b style="font-size:16px;">1,625원</b>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <span>경유</span><b style="font-size:16px;">1,510원</b>
            </div>
            <div style="display:flex; justify-content:space-between;">
                <span>고급유</span><b style="font-size:16px;">1,890원</b>
            </div>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("📍 주변 추천 핫플레이스"):
        st.markdown("<p style='font-size:14px;'>☕ <b>인더그레이</b>: 문덕 드라이브 코스 카페</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:14px;'>🍱 <b>뚝배기 주물럭</b>: 오천읍 현지인 맛집</p>", unsafe_allow_html=True)

# [COLUMN 2: 디테일링 LAB]
with col2:
    st.markdown("<h4>🧼 디테일링 LAB</h4>", unsafe_allow_html=True)
    
    tabs = st.tabs(["세차 가이드", "희석 계산기", "용품 추천"])
    
    with tabs[0]:
        st.markdown("""
            <div class="app-card">
                <h5 style="margin-top:0;">Premium 8-Step Guide</h5>
                <div style="font-size:15px; line-height:2.0;">
                    1️⃣ <b>중성 세차</b>: 도장면 안전 오염 제거<br>
                    2️⃣ <b>2PH 세차</b>: 알칼리+중성 교차 세정<br>
                    3️⃣ <b>3PH 세차</b>: 산성+알칼리+중성 마스터 공법<br>
                    4️⃣ <b>유막제거/발수</b>: 우천 시 시야 확보<br>
                    5️⃣ <b>휠/타이어</b>: 갈변 제거 및 드레싱 코팅<br>
                    6️⃣ <b>외장 왁스</b>: 광택 및 비딩 형성(LSP)<br>
                    7️⃣ <b>실내 세정</b>: 내장재 크리닝 및 보호<br>
                    8️⃣ <b>시트 코팅</b>: 가죽 가디언 코팅 유지
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("<div class='app-card'>", unsafe_allow_html=True)
        vol = st.number_input("목표 용량 (ml)", value=1000, step=100)
        rat = st.number_input("희석 비율 (1:N)", value=10, step=1)
        res = vol / (rat + 1)
        st.markdown(f"""
            <div style="background:#F1F5F9; padding:15px; border-radius:12px; margin-top:15px; text-align:center;">
                <p style="margin:0; font-size:14px; color:#475569 !important;">필요 원액량</p>
                <h2 style="margin:5px 0; color:#3B82F6 !important;">{res:.1f}ml</h2>
                <p style="margin:0; font-size:13px; color:#64748B !important;">나머지는 물로 채우세요 ({vol-res:.1f}ml)</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("<div class='app-card'>라보코스메티카, 코흐케미, 기온쿼츠, 파이어볼 등 매니아들이 검증한 제품 라인업 안내</div>", unsafe_allow_html=True)

# [COLUMN 3: 소통과 위치]
with col3:
    st.markdown("<h4>💬 커뮤니티</h4>", unsafe_allow_html=True)
    
    # 지도 섹션
    st.markdown("""
        <div class="app-card" style="padding:15px !important;">
            <p style="font-weight:800; font-size:15px; margin-bottom:5px;">오천 버블스타 세차장</p>
            <p style="font-size:13px; color:#64748B !important; margin-bottom:15px;">경북 포항시 남구 오천읍 문덕로79번길 26</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("🗺️ 네이버 지도로 길찾기", "https://naver.me/F6lTwCXz")

    st.write("")
    # 게시판 섹션
    with st.form("guestbook", clear_on_submit=True):
        st.markdown("<p style='font-size:14px; font-weight:700;'>세차 후기 남기기</p>", unsafe_allow_html=True)
        u_name = st.text_input("닉네임", placeholder="이름")
        u_msg = st.text_area("내용", placeholder="오늘 세차 어떠셨나요?")
        if st.form_submit_button("등록하기"):
            if u_name and u_msg:
                st.session_state.posts.append({"name": u_name, "msg": u_msg, "time": datetime.now().strftime("%H:%M")})
                st.rerun()

    for p in reversed(st.session_state.posts[-3:]):
        st.markdown(f"""
            <div style="background:white; padding:12px; border-radius:15px; margin-bottom:10px; border:1px solid #E2E8F0;">
                <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                    <b style="font-size:14px;">{p['name']}</b>
                    <span style="font-size:11px; color:#94A3B8 !important;">{p['time']}</span>
                </div>
                <p style="font-size:13px; margin:0;">{p['msg']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 4. 하단 고정 네비게이션바 (고시인성 디자인) ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
footer_col = st.columns(4)
menu_icons = ["🏠 HOME", "🧪 CALC", "💬 TALK", "👤 MY"]
for i, col in enumerate(footer_col):
    with col:
        st.button(menu_icons[i], key=f"nav_{i}")
