import streamlit as st
from datetime import datetime

# --- 1. 시인성 보장 정밀 스타일링 ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    /* 1. 폰트 및 전체 배경 강제 고정 */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 전체 앱 배경을 밝은 그레이로 고정 */
    .stApp {
        background-color: #F8FAFC !important;
    }

    /* 모든 글자색을 진한 검정색(#1A202C)으로 강제 고정 */
    h1, h2, h3, h4, h5, p, span, div, label, li {
        color: #1A202C !important;
        font-family: 'Pretendard', sans-serif !important;
    }

    /* 2. 카드 디자인: 입체감 있고 선명하게 */
    .app-card {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 24px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05) !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 20px !important;
    }

    /* 3. 탭(Tab) 메뉴 시인성 강화 */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #64748B !important; /* 비활성 탭 */
        font-weight: 700 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #3B82F6 !important; /* 활성 탭 (블루) */
        border-bottom-color: #3B82F6 !important;
    }

    /* 4. 입력창 및 버튼 디자인 고도화 */
    input, textarea {
        background-color: #FFFFFF !important;
        color: #1A202C !important;
        border: 1px solid #CBD5E1 !important;
    }
    
    /* 하단 네비게이션용 버튼 스타일 */
    .nav-btn > div > button {
        background-color: #1A202C !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        height: 50px !important;
        font-weight: 700 !important;
    }

    /* 5. 네이버 지도 버튼 전용 스타일 */
    .map-btn {
        background-color: #03C75A !important;
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-weight: 800;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 타이틀 ---
st.markdown("""
    <div style="text-align:center; padding: 30px 0;">
        <h1 style="font-size:40px; font-weight:900; letter-spacing:-1.5px; margin:0;">APEX POHANG</h1>
        <p style="font-size:16px; color:#64748B !important; font-weight:500; margin-top:5px;">오천 버블스타 크루 전용 스마트 라운지</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. 3열 레이아웃 ---
left_col, mid_col, right_col = st.columns([1, 1.2, 1], gap="large")

# [COLUMN 1: 실시간 정보]
with left_col:
    st.markdown("### ☀️ 실시간 정보")
    
    st.markdown("""
        <div class="app-card">
            <p style="color:#3B82F6 !important; font-weight:800; font-size:12px; margin-bottom:10px;">WEATHER</p>
            <h2 style="margin:0; font-size:32px;">5.2°C</h2>
            <p style="font-size:16px; font-weight:600; margin-top:5px;">포항 오천읍: 풍속 3.2m/s</p>
            <p style="font-size:14px; color:#059669 !important; font-weight:700;">✨ 현재 세차하기 아주 좋은 날씨입니다!</p>
        </div>
        <div class="app-card">
            <p style="color:#F59E0B !important; font-weight:800; font-size:12px; margin-bottom:10px;">GAS PRICE</p>
            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                <span>휘발유</span><b>1,625원</b>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                <span>경유</span><b>1,510원</b>
            </div>
            <div style="display:flex; justify-content:space-between;">
                <span>고급유</span><b>1,890원</b>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📍 주변 추천 맛집/카페"):
        st.markdown("""
            - ☕ **인더그레이**: 문덕 드라이브 코스 카페
            - 🥘 **뚝배기 주물럭**: 오천읍 현지인 맛집
        """)

# [COLUMN 2: 디테일링 LAB]
with mid_col:
    st.markdown("### 🧼 디테일링 LAB")
    
    lab_tabs = st.tabs(["세차 가이드", "희석 계산기", "추천 용품"])
    
    with lab_tabs[0]:
        st.markdown("""
            <div class="app-card">
                <h4 style="margin-top:0; border-bottom:2px solid #F1F5F9; padding-bottom:10px;">Premium 8-Step</h4>
                <div style="line-height:2.2; font-size:15px;">
                    1️⃣ <b>중성 세차</b>: 안전한 기본 오염 제거<br>
                    2️⃣ <b>2PH 세차</b>: 알칼리+중성 교차 세정<br>
                    3️⃣ <b>3PH 세차</b>: 산성+알칼리+중성 마스터 공법<br>
                    4️⃣ <b>유막제거/발수</b>: 우천 시 시야 확보<br>
                    5️⃣ <b>휠/타이어</b>: 갈변 제거 및 보호 코팅<br>
                    6️⃣ <b>외장 왁스</b>: 극강의 광택 및 비딩(LSP)<br>
                    7️⃣ <b>내장재 세정</b>: 실내 정밀 크리닝<br>
                    8️⃣ <b>시트 코팅</b>: 가죽 보호 및 색상 유지
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with lab_tabs[1]:
        st.markdown("<div class='app-card'>", unsafe_allow_html=True)
        vol = st.number_input("목표 용량 (ml)", value=1000, step=100)
        rat = st.number_input("희석 비율 (1:N)", value=10, step=1)
        res = vol / (rat + 1)
        st.markdown(f"""
            <div style="background:#F1F5F9; padding:20px; border-radius:15px; text-align:center; margin-top:15px;">
                <p style="margin:0; font-size:14px; color:#64748B !important;">필요 원액량</p>
                <h2 style="margin:5px 0; color:#3B82F6 !important; font-size:36px;">{res:.1f}ml</h2>
                <p style="margin:0; font-size:13px; color:#94A3B8 !important;">물은 {vol-res:.1f}ml를 채우세요.</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with lab_tabs[2]:
        st.markdown("<div class='app-card'>라보코스메티카, 코흐케미, 기온쿼츠, 파이어볼 등 디테일러 추천 제품 정보를 업데이트 중입니다.</div>", unsafe_allow_html=True)

# [COLUMN 3: 커뮤니티]
with right_col:
    st.markdown("### 💬 커뮤니티")
    
    st.markdown("""
        <div class="app-card" style="padding:18px !important;">
            <p style="font-weight:800; font-size:16px; margin-bottom:5px;">오천 버블스타 세차장</p>
            <p style="font-size:13px; color:#64748B !important; margin-bottom:15px;">경북 포항시 남구 오천읍 문덕로79번길 26</p>
            <a href="https://naver.me/F6lTwCXz" target="_blank" class="map-btn">🗺️ 네이버 지도로 길찾기</a>
        </div>
    """, unsafe_allow_html=True)

    with st.form("guestbook", clear_on_submit=True):
        st.markdown("<p style='font-size:15px; font-weight:700; margin-bottom:10px;'>실시간 세차 후기</p>", unsafe_allow_html=True)
        u_name = st.text_input("닉네임", placeholder="이름")
        u_msg = st.text_area("내용", placeholder="오늘 세차 결과는 어떠신가요?")
        if st.form_submit_button("등록하기"):
            if u_name and u_msg:
                st.session_state.posts.append({"name": u_name, "msg": u_msg, "time": datetime.now().strftime("%H:%M")})
                st.rerun()

    for p in reversed(st.session_state.posts[-3:]):
        st.markdown(f"""
            <div style="background:white; padding:15px; border-radius:16px; margin-bottom:12px; border:1px solid #E2E8F0; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                    <b style="font-size:14px;">{p['name']}</b>
                    <span style="font-size:11px; color:#94A3B8 !important;">{p['time']}</span>
                </div>
                <p style="font-size:14px; margin:0; line-height:1.4;">{p['msg']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 4. 하단 고정 네비게이션바 ---
st.markdown("<div style='margin-top:50px;'></div>", unsafe_allow_html=True)
nav_col = st.columns(4)
nav_icons = ["🏠 HOME", "🧪 CALC", "💬 TALK", "👤 MY"]
for i, col in enumerate(nav_col):
    with col:
        st.markdown(f'<div class="nav-btn">', unsafe_allow_html=True)
        st.button(nav_icons[i], key=f"nav_btn_{i}", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
