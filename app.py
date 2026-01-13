import streamlit as st
from datetime import datetime

# --- 1. 독창적 디자인 시스템 (시인성 100% 고정) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* [핵심] 배경과 글자색을 강제로 고정하여 시인성 확보 */
    .stApp {
        background-color: #0F172A !important; /* 깊은 네이비 배경 */
    }
    
    /* 모든 텍스트 기본색을 화이트로 고정 */
    h1, h2, h3, h4, p, span, div, label, li {
        color: #FFFFFF !important;
        font-family: 'Pretendard', sans-serif !important;
    }

    /* 독창적인 '네온 보더' 카드 디자인 */
    .premium-card {
        background: rgba(30, 41, 59, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left: 5px solid #3B82F6; /* 포인트 컬러 */
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }

    /* 유가 정보 전용 텍스트 강조 */
    .price-main { font-size: 20px; font-weight: 800; color: #60A5FA !important; }
    .station-title { font-size: 16px; font-weight: 700; color: #F8FAFC !important; }

    /* 탭 메뉴 디자인 커스텀 */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background: #1E293B !important;
        border-radius: 8px 8px 0 0 !important;
        color: #94A3B8 !important;
        padding: 10px 20px !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: #3B82F6 !important;
        color: white !important;
    }

    /* 입력창 시인성 (검정 배경에서도 잘 보이게) */
    input, textarea {
        background-color: #1E293B !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 브랜딩 (독창적 헤더) ---
st.markdown("""
    <div style="text-align:left; border-bottom: 2px solid #3B82F6; padding-bottom: 20px; margin-bottom: 40px;">
        <h1 style="font-size:48px; font-weight:900; letter-spacing:-2px; margin:0;">APEX <span style="color:#3B82F6 !important;">POHANG</span></h1>
        <p style="font-size:16px; color:#94A3B8 !important; margin:0;">오천 버블스타 크루 전용 스마트 라운지</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. 데이터 및 세부 기능 (요청하신 코드 그대로 유지) ---
oil_data = [
    {"name": "GS칼텍스 오천주유소", "dist": "1.2km", "gas": "1,615", "diesel": "1,495"},
    {"name": "SK에너지 문덕주유소", "dist": "0.8km", "gas": "1,620", "diesel": "1,505"},
    {"name": "S-OIL 셀프 오천점", "dist": "2.1km", "gas": "1,598", "diesel": "1,480"},
    {"name": "현대오일뱅크 포항스틸호", "dist": "3.5km", "gas": "1,635", "diesel": "1,520"}
]

detailing_steps = [
    "1. 중성 세차: 도장면 안전 오염 제거",
    "2. 2PH 세차: 알칼리+중성 교차 세정",
    "3. 3PH 세차: 산성+알칼리+중성 마스터",
    "4. 유막제거/발수: 시야 확보 및 코팅",
    "5. 휠/타이어: 갈변 제거 및 드레싱",
    "6. 외장 왁스: 광택 및 비딩 형성",
    "7. 실내 세정: 정밀 크리닝 및 보호",
    "8. 시트 코팅: 이염 방지 및 유지"
]

# --- 4. 메인 레이아웃 (3열 매거진 스타일) ---
l, m, r = st.columns([1.1, 1, 0.9], gap="large")

with l:
    st.markdown("### ⛽ 반경 5Km 최적 유가")
    for oil in oil_data:
        st.markdown(f"""
            <div class="premium-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="station-title">{oil['name']} <small style="color:#64748B !important;">({oil['dist']})</small></span>
                    <span class="price-main">{oil['gas']}원</span>
                </div>
                <p style="margin:5px 0 0 0; font-size:13px; color:#94A3B8 !important;">디젤 {oil['diesel']}원</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🌤️ WEATHER")
    st.markdown("""
        <div class="premium-card" style="border-left-color: #F59E0B;">
            <h2 style="margin:0; color:#F59E0B !important;">5.2°C</h2>
            <p style="margin:5px 0;">풍속 <b>3.2m/s</b> | 세차 지수: <b>매우 좋음 ✨</b></p>
        </div>
    """, unsafe_allow_html=True)

with m:
    st.markdown("### 🧼 DETAILING LAB")
    lab_tabs = st.tabs(["세차 가이드", "희석 계산기", "맛집/카페"])
    
    with lab_tabs[0]:
        st.markdown("<div class='premium-card' style='border-left-color:#10B981;'>", unsafe_allow_html=True)
        for step in detailing_steps:
            st.write(step)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with lab_tabs[1]:
        st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
        vol = st.number_input("목표 용량(ml)", value=1000)
        rat = st.number_input("희석 비율(1:N)", value=10)
        res = vol / (rat + 1)
        st.markdown(f"<div style='text-align:center; padding:20px; background:#0F172A; border-radius:12px;'><p style='margin:0;'>필요 원액량</p><h2 style='color:#3B82F6 !important; margin:0;'>{res:.1f}ml</h2></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with lab_tabs[2]:
        st.markdown("<div class='premium-card'>☕ <b>인더그레이</b>: 문덕 드라이브 카페<br>🥘 <b>뚝배기 주물럭</b>: 오천읍 맛집</div>", unsafe_allow_html=True)

with r:
    st.markdown("### 💬 COMMUNITY")
    st.markdown("""
        <div class="premium-card" style="border-left-color:#03C75A;">
            <p style="font-weight:800; margin-bottom:10px;">오천 버블스타 세차장</p>
            <p style="font-size:13px; color:#94A3B8 !important; margin-bottom:15px;">포항 남구 오천읍 문덕로79번길 26</p>
            <a href="https://naver.me/F6lTwCXz" target="_blank" style="text-decoration:none; display:block; background:#03C75A; color:white; text-align:center; padding:15px; border-radius:12px; font-weight:800;">N 네이버 지도</a>
        </div>
    """, unsafe_allow_html=True)

    with st.form("guestbook", clear_on_submit=True):
        u_name = st.text_input("닉네임")
        u_msg = st.text_area("후기")
        if st.form_submit_button("등록"):
            if u_name and u_msg:
                st.session_state.posts.append({"name": u_name, "msg": u_msg, "time": datetime.now().strftime("%H:%M")})
                st.rerun()

    for p in reversed(st.session_state.posts[-2:]):
        st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:15px; border-radius:12px; margin-bottom:10px;'><b>{p['name']}</b> <small style='color:#64748B;'>{p['time']}</small><br>{p['msg']}</div>", unsafe_allow_html=True)

# --- 5. 하단 메뉴 ---
st.markdown("<div style='margin-top:60px;'></div>", unsafe_allow_html=True)
f_cols = st.columns(4)
f_menus = ["🏠 HOME", "🧪 CALC", "💬 TALK", "👤 MY"]
for i, c in enumerate(f_cols):
    c.button(f_menus[i], key=f"f_{i}", use_container_width=True)
