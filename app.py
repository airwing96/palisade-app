import streamlit as st
from datetime import datetime

# --- 1. 독창적 UI/UX 디자인 시스템 (다크모드 간섭 완벽 차단) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    /* 폰트: 가독성 끝판왕 Pretendard */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    /* 전체 배경: 세련된 다크 캔버스 고정 */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
    }

    /* 모든 텍스트: 선명한 화이트/그레이 고정 */
    h1, h2, h3, h4, p, span, div, label, li {
        font-family: 'Pretendard', sans-serif !important;
        color: #f8fafc !important; /* 가독성 확보를 위해 밝은 색으로 강제 */
    }

    /* 독창적 카드 디자인: 유리 질감(Glassmorphism) 적용 */
    .glass-card {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 25px;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(59, 130, 246, 0.5);
    }

    /* 네온 포인트 텍스트 */
    .neon-blue { color: #3b82f6 !important; text-shadow: 0 0 10px rgba(59,130,246,0.5); font-weight: 800; }
    .neon-orange { color: #f59e0b !important; text-shadow: 0 0 10px rgba(245,158,11,0.5); font-weight: 800; }
    .neon-green { color: #10b981 !important; text-shadow: 0 0 10px rgba(16,185,129,0.5); font-weight: 800; }

    /* 탭 메뉴 개성있게 수정 */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 12px 12px 0 0 !important;
        padding: 10px 20px !important;
        color: #94a3b8 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: rgba(59, 130, 246, 0.2) !important;
        color: #3b82f6 !important;
    }

    /* 네이버 버튼 전용 */
    .btn-naver {
        background: #03c75a !important;
        color: white !important;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-weight: 800;
        box-shadow: 0 4px 15px rgba(3,199,90,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 브랜딩 (개성 넘치는 타이틀) ---
st.markdown("""
    <div style="text-align:center; padding: 50px 0;">
        <h1 style="font-size:50px; font-weight:900; background: linear-gradient(to right, #3b82f6, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">APEX POHANG</h1>
        <p style="font-size:18px; color:#94a3b8 !important; letter-spacing:2px; margin-top:10px;">POHANG OHCHEON DETAILING CREW</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. 메인 레이아웃 (세부 내용 유지) ---
l, m, r = st.columns([1, 1.2, 1], gap="large")

with l:
    st.markdown("<h4 class='neon-blue'>🌤️ WEATHER & OIL</h4>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="glass-card">
            <p style="font-size:14px; opacity:0.7;">오천읍 기상</p>
            <h2 style="margin:0; font-size:36px;">5.2°C</h2>
            <p style="font-size:16px; margin-top:5px;">풍속 <span class='neon-blue'>3.2m/s</span> (최적)</p>
            <p style="color:#10b981 !important; font-size:13px; font-weight:700;">✨ 세차하기 매우 좋은 날씨입니다.</p>
        </div>
        <div class="glass-card">
            <p style="font-size:14px; opacity:0.7;">오천읍 평균 유가</p>
            <div style="display:flex; justify-content:space-between; margin-top:10px;"><span>휘발유</span><b class='neon-orange'>1,625원</b></div>
            <div style="display:flex; justify-content:space-between;"><span>경유</span><b class='neon-orange'>1,510원</b></div>
            <div style="display:flex; justify-content:space-between;"><span>고급유</span><b class='neon-orange'>1,890원</b></div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🍔 크루 추천 맛집/카페"):
        st.markdown("- ☕ **인더그레이**: 문덕 드라이브 코스\n- 🥘 **뚝배기 주물럭**: 오천읍 노포 맛집")

with m:
    st.markdown("<h4 class='neon-blue'>🧼 DETAILING LAB</h4>", unsafe_allow_html=True)
    t1, t2, t3 = st.tabs(["가이드", "희석기", "브랜드"])
    
    with t1:
        st.markdown("""
            <div class="glass-card">
                <h5 style="color:#3b82f6 !important;">Premium 8-Step</h5>
                <p style="font-size:14px; line-height:2.1; margin:0;">
                    1. <b>중성 세차</b>: 안전한 기본 세정<br>
                    2. <b>2PH 세차</b>: 알칼리+중성 교차<br>
                    3. <b>3PH 세차</b>: 매니아용 마스터 공법<br>
                    4. <b>유막/발수</b>: 유리 시야 확보 필수<br>
                    5. <b>휠/타이어</b>: 갈변제거 및 코팅<br>
                    6. <b>외장 왁스</b>: 광택 및 비딩 관리<br>
                    7. <b>내장 세정</b>: 실내 정밀 크리닝<br>
                    8. <b>시트 코팅</b>: 가죽 가디언 코팅
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with t2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        vol = st.number_input("용량(ml)", value=1000)
        rat = st.number_input("비율(1:N)", value=10)
        res = vol / (rat + 1)
        st
