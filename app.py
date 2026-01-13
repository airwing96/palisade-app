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
        background: linear-gradient(135deg, #3B82F6, #1D4ED8); 
        color: white; padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 800;
    }
    .best-item-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 12px;
        border-radius: 10px;
        margin-top: 10px;
        border-left: 4px solid #3B82F6;
    }
    .alert-card { background: rgba(239, 68, 68, 0.2) !important; border: 2px solid #EF4444; border-radius: 18px; padding: 20px; margin-bottom: 20px; }
    .safe-card { background: rgba(16, 185, 129, 0.2) !important; border: 2px solid #10B981; border-radius: 18px; padding: 20px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 브랜드 상세 데이터 (Best 라인업 & 사진 링크) ---
brand_data = {
    "라보코스메티카": {
        "best": "프리머스(알칼리), 퓨리피카(산성), 베네레",
        "desc": "이탈리아 하이엔드 케미컬의 정점. 3PH 세차 시스템의 기준입니다.",
        "shop": "공식 수입원: 엔공구 / 슬릭핸즈",
        "img": "https://images.unsplash.com/photo-1607860108855-64acf2078ed9?w=400"
    },
    "기온쿼츠": {
        "best": "웨트코트(발수), 아이언(철분), 캔코트",
        "desc": "전 세계 디테일러가 선호하는 압도적인 퍼포먼스와 세련된 패키징.",
        "shop": "기온쿼츠 코리아 공식 스토어",
        "img": "https://images.unsplash.com/photo-1552933529-e359b2477262?w=400"
    },
    "더클래스": {
        "best": "불렛(물왁스), 데드아이, 클린앤코트",
        "desc": "국산 프리미엄의 자존심. 극강의 슬릭감과 한국 기후에 최적화된 성능.",
        "shop": "더클래스 네이버 공식 스토어",
        "img": "https://images.unsplash.com/photo-1601362840469-51e4d8d59085?w=400"
    },
    "코흐케미": {
        "best": "Gsf(스노우폼), Mw(메르세데스 인증), Pw",
        "desc": "독일 화학 기술의 정수. Benz, BMW 등 제조사가 공식 승인한 케미컬.",
        "shop": "독특닷컴 / 공식 수입사",
        "img": "https://images.unsplash.com/photo-1599256621730-535171e28e50?w=400"
    }
}

# --- 3. 세션 및 기상 설정 ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "admin77", "tier": "관리자", "name": "마스터"}}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None
if 'wash_schedule' not in st.session_state: st.session_state.wash_schedule = []

wind_speed = 3.5 
weather_condition = "맑음"

# --- 4. 메인 UI ---
st.markdown("<h1 style='font-size:45px;'>APEX <span style='color:#3B82F6;'>PLATFORM</span></h1>", unsafe_allow_html=True)
st.markdown("📍 **오천 버블스타 (포항 남구 오천읍 문덕로79번길 26)**")

# 기상 알람
if wind_speed >= 6.0:
    st.markdown(f"<div class='alert-card'>🚨 강풍 주의: 현재 풍속 {wind_speed}m/s. 세차를 권장하지 않습니다.</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='safe-card'>✅ 세차 지수 맑음: 풍속 {wind_speed}m/s. 최상의 세차 조건입니다.</div>", unsafe_allow_html=True)

main_tabs = st.tabs(["🛍️ 브랜드 스토어", "🧼 세차 가이드", "🗓️ 크루 일정", "⚙️ 관리자/회원"])

with main_tabs[0]:
    st.markdown("### 🏷️ 프리미엄 용품 추천 & 공식 판매처")
    for name, info in brand_data.items():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(info['img'], use_container_width=True, caption=f"{name} Line-up")
        with col2:
            st.markdown(f"""
                <div class="premium-card">
                    <span class="brand-badge">{name}</span>
                    <p style="margin-top:10px; font-size:15px; opacity:0.9;">{info['desc']}</p>
                    <div class="best-item-box">
                        <span style="color:#60A5FA; font-weight:bold;">🏆 BEST 라인업:</span> {info['best']}
                    </div>
                    <p style="font-size:13px; margin-top:10px; color:#94A3B8 !important;">🛒 공식 판매처: {info['shop']}</p>
                </div>
            """, unsafe_allow_html=True)

with main_tabs[1]:
    st.markdown("### 🧼 전문가 세차 8단계 (상세)")
    guide = {
        "1. 중성 세차": "고압수로 큰 오염물 제거 후 중성 샴푸 기본 세정",
        "2. 2PH 세차": "알칼리 프리워시와 중성 샴푸의 조화",
        "3. 3PH 세차": "산성-알칼리-중성 순서로 모든 오염물 완벽 제거",
        "4. 유막/발수": "산화세륨 유막 제거 후 유리 발수 코팅",
        "5. 휠/타이어": "분진 제거 및 타이어 갈변 제거 후 드레싱",
        "6. 외장 왁스": "물왁스 또는 고체왁스 도장면 보호막 형성",
        "7. 실내 세정": "내장재 전용 세정제로 유분 및 먼지 제거",
        "8. 시트 코팅": "가죽 시트 이염 방지 및 신차 상태 유지"
    }
    for k, v in guide.items():
        st.markdown(f"<div class='premium-card'><b>{k}</b><br><small>{v}</small></div>", unsafe_allow_html=True)

# 이하 크루 일정 및 관리자 탭은 기존 로직 유지 (생략 가능하나 코드 안정성을 위해 유지 권장)
with main_tabs[2]:
    st.write("🗓️ 크루 일정 관리 섹션")
    if st.session_state.logged_in_user:
        d = st.date_input("날짜 선택")
        if st.button("일정 등록"):
            st.session_state.wash_schedule.append({"date": str(d), "user": st.session_state.logged_in_user})
            st.success("등록되었습니다.")

with main_tabs[3]:
    if st.session_state.logged_in_user == "admin":
        st.markdown("### ⚙️ 회원 권한 관리")
        for uid, info in st.session_state.users.items():
            st.write(f"👤 {uid} ({info['tier']})")
    else:
        u = st.text_input("ID")
        p = st.text_input("PW", type="password")
        if st.button("로그인"):
            if u in st.session_state.users and st.session_state.users[u]['pw'] == p:
                st.session_state.logged_in_user = u
                st.rerun()

# 사이드바
st.sidebar.markdown("### ⛽ 실시간 유가")
st.sidebar.markdown("<div class='premium-card'>GS: 1,615원<br>S-OIL: 1,598원</div>", unsafe_allow_html=True)
