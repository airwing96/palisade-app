import streamlit as st
from datetime import datetime
import pandas as pd

# --- 1. UI & 시인성 디자인 시스템 (변경 없이 유지) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    .stApp { background-color: #0F172A !important; }
    h1, h2, h3, h4, p, span, div, label, li { color: #FFFFFF !important; font-family: 'Pretendard', sans-serif !important; }
    
    .premium-card {
        background: rgba(30, 41, 59, 0.9) !important;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .brand-badge { background: #3B82F6; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }
    .alert-card { background: rgba(239, 68, 68, 0.2) !important; border: 2px solid #EF4444; border-radius: 18px; padding: 20px; margin-bottom: 20px; }
    .safe-card { background: rgba(16, 185, 129, 0.2) !important; border: 2px solid #10B981; border-radius: 18px; padding: 20px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 시스템 데이터 (유지) ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "admin77", "tier": "관리자", "name": "마스터"}}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None
if 'wash_schedule' not in st.session_state: st.session_state.wash_schedule = []

# [업데이트] 영상 가이드 매핑 데이터
video_guides = {
    "1. 중성/2. 2PH 세차": "https://www.youtube.com/watch?v=TnZjiAr2eBs",
    "3. 3PH 세차 (라보코스메티카 공식)": "https://www.youtube.com/watch?v=gnlVGVG55uY",
    "4. 유막제거/발수코팅": "https://www.youtube.com/watch?v=vXzD9P5Hnkc",
    "5. 휠/타이어 케어": "https://www.youtube.com/watch?v=4MItZIY09aE"
}

# --- 3. 메인 화면 및 기상 정보 (유지) ---
st.markdown("<h1 style='font-size:45px;'>APEX <span style='color:#3B82F6;'>PLATFORM</span></h1>", unsafe_allow_html=True)
st.markdown("📍 **오천 버블스타 세차장 (포항 남구 오천읍 문덕로79번길 26)**")

# 기상 정보 (테스트 데이터 유지)
wind_speed = 3.5 
weather_condition = "맑음"

if wind_speed >= 6.0 or "비" in weather_condition:
    st.markdown(f"<div class='alert-card'>🚨 강풍/강수 주의보: 풍속 {wind_speed}m/s. 세차 비권장</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='safe-card'>✅ 세차 지수 최고: 풍속 {wind_speed}m/s. 완벽한 디테일링 날씨!</div>", unsafe_allow_html=True)

# --- 4. 메인 탭 구성 ---
main_tabs = st.tabs(["🧼 세차 영상 가이드", "🛒 브랜드 스토어", "🗓️ 크루 일정", "⚙️ 관리자/회원"])

with main_tabs[0]:
    st.markdown("### 🎬 전문가 세차 8단계 영상 가이드")
    st.info("텍스트 가이드와 함께 공식 영상을 시청하여 전문가의 기술을 습득하세요.")
    
    # [복구 및 유지] 8단계 설명 텍스트
    guide_steps = {
        "1. 중성 세차": "고압수로 오염 제거 후 중성 샴푸로 안전하게 미트질",
        "2. 2PH 세차": "알칼리 프리워시와 중성 샴푸의 조화",
        "3. 3PH 세차": "산성-알칼리-중성 순서로 모든 오염물 완벽 제거 (라보코스메티카 표준)",
        "4. 유막/발수": "산화세륨으로 유막 제거 후 발수 코팅 시공",
        "5. 휠/타이어": "철분 제거 및 타이어 갈변 제거 후 드레싱",
        "6. 외장 왁스": "물왁스 또는 고체왁스로 도장면 보호막 형성",
        "7. 실내 세정": "내장재 전용 세정제로 유분 및 먼지 제거",
        "8. 시트 코팅": "가죽 시트 이염 방지 및 신차 상태 유지 코팅"
    }

    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.markdown("<div class='premium-card'><b>기초/2PH 세차 마스터</b>", unsafe_allow_html=True)
        st.video(video_guides["1. 중성/2. 2PH 세차"])
        st.write(guide_steps["1. 중성 세차"])
        st.write(guide_steps["2. 2PH 세차"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='premium-card'><b>유리 관리 (유막/발수)</b>", unsafe_allow_html=True)
        st.video(video_guides["4. 유막제거/발수코팅"])
        st.write(guide_steps["4. 유막/발수"])
        st.markdown("</div>", unsafe_allow_html=True)

    with v_col2:
        st.markdown("<div class='premium-card'><b>3PH 공식 프로세스</b>", unsafe_allow_html=True)
        st.video(video_guides["3. 3PH 세차 (라보코스메티카 공식)"])
        st.write(guide_steps["3. 3PH 세차"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='premium-card'><b>종합 세차 순서 및 꿀팁</b>", unsafe_allow_html=True)
        st.video(video_guides["5. 휠/타이어 케어"])
        st.write("나머지 5~8단계 통합 가이드 영상")
        st.markdown("</div>", unsafe_allow_html=True)

with main_tabs[1]:
    # [유지] 브랜드 스토어 섹션 (라보코스메티카, 메니악 등)
    st.markdown("### 🛒 프리미엄 용품 브랜드")
    brand_data = {
        "라보코스메티카": "프리머스, 퓨리피카 등 3PH 정석",
        "메니악": "마프라 프리미엄 라인업",
        "더클래스": "불렛 등 국산 물왁스 최강자",
        "기온쿼츠": "압도적 성능의 하이엔드 케미컬"
    }
    b_c1, b_c2 = st.columns(2)
    for i, (b, d) in enumerate(brand_data.items()):
        (b_c1 if i%2==0 else b_c2).markdown(f"<div class='premium-card'><span class='brand-badge'>{b}</span><br>{d}</div>", unsafe_allow_html=True)

with main_tabs[2]:
    # [유지] 일정 관리 탭
    st.markdown("### 🗓️ 세차 크루 벙개 일정")
    for s in reversed(st.session_state.wash_schedule):
        st.markdown(f"<div class='premium-card'>📅 {s['date']} - {s['user']}</div>", unsafe_allow_html=True)

with main_tabs[3]:
    # [유지] 회원/관리자 탭
    if st.session_state.logged_in_user == "admin":
        st.markdown("### 👑 관리자 모드")
        st.write("회원 등급 및 권한 설정 대시보드")
    else:
        st.info("로그인 후 등급별 혜택을 확인하세요.")

# --- 5. 사이드바 유가 정보 (유지) ---
st.sidebar.markdown("### ⛽ 오천읍 최저가 유가")
st.sidebar.markdown("<div class='premium-card'><b>GS칼텍스</b>: 1,615원<br><b>S-OIL</b>: 1,598원</div>", unsafe_allow_html=True)
