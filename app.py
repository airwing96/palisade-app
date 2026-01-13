import streamlit as st
from datetime import datetime
import pandas as pd

# --- 1. 시인성 고정 디자인 시스템 ---
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
    .brand-badge {
        background: #3B82F6; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;
    }
    .price-text { color: #60A5FA !important; font-weight: 800; font-size: 14px; }
    .alert-card { background: rgba(239, 68, 68, 0.2) !important; border: 2px solid #EF4444; border-radius: 18px; padding: 20px; margin-bottom: 20px; }
    .safe-card { background: rgba(16, 185, 129, 0.2) !important; border: 2px solid #10B981; border-radius: 18px; padding: 20px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 브랜드 및 제품 데이터 (신규 추가) ---
brand_products = {
    "라보코스메티카": {"best": "프리머스(알칼리), 퓨리피카(산성)", "desc": "3PH 세차의 표준, 이탈리아 하이엔드 케미컬"},
    "메니악": {"best": "휠&타이어 클리너, 블랙라인 샴푸", "desc": "마프라의 프리미엄 라인, 강력한 세정력과 퍼포먼스"},
    "더클래스": {"best": "불렛(물왁스), 데드아이(철분제거)", "desc": "국산 프리미엄의 자존심, 극강의 슬릭감과 광택"},
    "파이어볼": {"best": "이지커트, 탈지제, 고체왁스 시리즈", "desc": "전 세계로 수출되는 국산 하이테크 디테일링 브랜드"},
    "기온쿼츠": {"best": "웨트코트(발수), 아이언(철분제거)", "desc": "세련된 패키징과 압도적인 발수 성능의 대명사"},
    "코흐케미": {"best": "Gsf(스노우폼), Mw(마운틴워시)", "desc": "독일 완성차 브랜드가 공식 사용하는 검증된 성능"},
    "보닉스": {"best": "블렌드(왁스), 네이티브(천연카나우바)", "desc": "브라질 카나우바의 정수, 깊고 맑은 광택감"},
    "카티바": {"best": "글로스 부스터, 타이어 드레싱", "desc": "최근 매니아들 사이에서 급부상 중인 고성능 브랜드"}
}

# --- 3. 기상 로직 및 시스템 설정 (기존 유지) ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "admin77", "tier": "관리자", "name": "마스터"}}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None
if 'wash_schedule' not in st.session_state: st.session_state.wash_schedule = []

# 기상 변수 (오천읍 기준)
wind_speed = 3.5 
weather_condition = "맑음"

# --- 4. 메인 UI 구성 ---
st.markdown("<h1 style='font-size:45px;'>APEX <span style='color:#3B82F6;'>PLATFORM</span></h1>", unsafe_allow_html=True)
st.markdown("📍 **오천 버블스타 세차장 (포항 남구 오천읍 문덕로79번길 26)**")

# 기상 경보 시스템
if wind_speed >= 6.0 or "비" in weather_condition:
    st.markdown(f"<div class='alert-card'>🚨 강풍/강수 주의보: 현재 풍속 {wind_speed}m/s. 세차를 권장하지 않습니다.</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='safe-card'>✅ 세차 지수 맑음: 풍속 {wind_speed}m/s. 디테일링하기 완벽한 날씨입니다!</div>", unsafe_allow_html=True)

# 메인 탭 구성
main_tabs = st.tabs(["🛍️ 브랜드 스토어", "🧼 세차 가이드", "🗓️ 크루 일정", "⚙️ 관리자/회원"])

with main_tabs[0]:
    st.markdown("### 🛒 프리미엄 용품 추천 & 판매 정보")
    st.info("각 브랜드를 클릭하면 인기 제품과 특징을 확인할 수 있습니다.")
    
    # 2열로 브랜드 배치
    b_col1, b_col2 = st.columns(2)
    for i, (name, info) in enumerate(brand_products.items()):
        target_col = b_col1 if i % 2 == 0 else b_col2
        with target_col:
            st.markdown(f"""
                <div class="premium-card">
                    <span class="brand-badge">{name}</span>
                    <h4 style="margin:10px 0 5px 0;">{name} 인기 라인업</h4>
                    <p style="font-size:14px; color:#60A5FA !important; font-weight:bold;">🏆 BEST: {info['best']}</p>
                    <p style="font-size:13px; opacity:0.8;">{info['desc']}</p>
                    <hr style="border:0.1px solid rgba(255,255,255,0.1);">
                    <p style="font-size:12px; text-align:right;">📦 공식 판매처 및 크루 공구 협의 중</p>
                </div>
            """, unsafe_allow_html=True)

with main_tabs[1]:
    st.markdown("### 🧼 전문가 세차 8단계 (상세)")
    guide = {
        "1. 중성 세차": "고압수로 오염 제거 후 중성 샴푸로 안전하게 미트질",
        "2. 2PH 세차": "알칼리 프리워시와 중성 샴푸의 조화",
        "3. 3PH 세차": "산성-알칼리-중성 순서로 모든 오염물 완벽 제거",
        "4. 유막/발수": "산화세륨으로 유막 제거 후 발수 코팅 시공",
        "5. 휠/타이어": "철분 제거 및 타이어 갈변 제거 후 드레싱",
        "6. 외장 왁스": "물왁스 또는 고체왁스로 도장면 보호막 형성",
        "7. 실내 세정": "내장재 전용 세정제로 유분 및 먼지 제거",
        "8. 시트 코팅": "가죽 시트 이염 방지 및 신차 상태 유지 코팅"
    }
    for step, desc in guide.items():
        st.markdown(f"<div class='premium-card'><b>{step}</b><br><small style='opacity:0.8;'>{desc}</small></div>", unsafe_allow_html=True)

with main_tabs[2]:
    st.markdown("### 🗓️ 세차 벙개 및 일정")
    if st.session_state.logged_in_user:
        with st.expander("일정 등록하기"):
            d = st.date_input("날짜 선택")
            if st.button("벙개 등록"):
                st.session_state.wash_schedule.append({"date": str(d), "user": st.session_state.logged_in_user})
                st.success("등록 완료!")
    for s in reversed(st.session_state.wash_schedule):
        st.markdown(f"<div class='premium-card'>📅 {s['date']} - 주최: {s['user']}</div>", unsafe_allow_html=True)

with main_tabs[3]:
    if st.session_state.logged_in_user == "admin":
        st.markdown("### ⚙️ 회원 등급 관리")
        for uid, info in st.session_state.users.items():
            st.write(f"👤 {uid} ({info['name']}) - 현재 등급: {info['tier']}")
            st.selectbox("등급 변경", ["일반", "정회원", "실버", "골드"], key=f"tier_{uid}")
    else:
        st.markdown("### 👤 회원 로그인")
        u_id = st.text_input("아이디", key="login_id")
        u_pw = st.text_input("비밀번호", type="password", key="login_pw")
        if st.button("로그인"):
            if u_id in st.session_state.users and st.session_state.users[u_id]['pw'] == u_pw:
                st.session_state.logged_in_user = u_id
                st.rerun()

# --- 5. 사이드바 (실시간 유가 정보 유지) ---
st.sidebar.markdown("### ⛽ 오천읍 실시간 유가")
st.sidebar.markdown("""
<div class="premium-card">
<b>GS칼텍스 오천</b>: 1,615원<br>
<b>S-OIL 셀프</b>: 1,598원<br>
<small style="opacity:0.6;">반경 5Km 최저가 정보</small>
</div>
""", unsafe_allow_html=True)
