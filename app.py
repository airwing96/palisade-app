import streamlit as st
from datetime import datetime
import pandas as pd

# --- 1. 시인성 고정 디자인 (다크모드에서도 완벽한 가독성) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    .stApp { background-color: #0F172A !important; }
    h1, h2, h3, h4, p, span, div, label, li { color: #FFFFFF !important; font-family: 'Pretendard', sans-serif !important; }
    
    /* 고대비 카드 디자인 */
    .premium-card {
        background: rgba(30, 41, 59, 0.9) !important;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .alert-card {
        background: rgba(239, 68, 68, 0.2) !important;
        border: 2px solid #EF4444;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .safe-card {
        background: rgba(16, 185, 129, 0.2) !important;
        border: 2px solid #10B981;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 시스템 데이터 (회원, 일정, 가이드) ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "admin77", "tier": "관리자", "name": "마스터"}}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None
if 'wash_schedule' not in st.session_state: st.session_state.wash_schedule = []

# [복구] 세차 가이드 8단계 상세 내용
detailing_guide = {
    "1단계: 중성 세차": "고압수로 큰 오염물 제거 후, 도장면 손상 없는 중성 카샴푸로 기본 세정",
    "2단계: 2PH 세차": "알칼리성 프리워시로 찌든 때를 불리고 중성 샴푸로 마무리하는 2단계 세정",
    "3단계: 3PH 세차": "산성-알칼리-중성을 순차 사용해 미네랄, 단백질, 유분 오염을 완벽히 박멸",
    "4단계: 유막제거/발수": "산화세륨으로 유리 오염 제거 후 불소계 코팅으로 우천 시 시야 확보",
    "5단계: 휠/타이어": "철분 제거제와 타이어 클리너로 분진 제거 후 전용 드레싱으로 갈변 방지",
    "6단계: 외장 왁스": "고체 왁스 또는 퀵 디테일러(LSP)를 이용해 극강의 광택과 비딩 형성",
    "7단계: 실내 세정": "내장재 전용 클리너로 유분 제거 후 가죽/플라스틱 보습 및 드레싱",
    "8단계: 시트 코팅": "청바지 이염 및 오염 방지를 위해 가죽 전용 코팅제로 내구성 강화"
}

# --- 3. 실시간 기상 정보 및 경보 로직 (오천읍 기준) ---
# 실제 API 연동 전 테스트용 변수 (수정 가능)
temp = 5.2
wind_speed = 7.5  # 테스트를 위해 6m/s 이상으로 설정
weather_condition = "맑음" # '비', '눈' 포함 시 경보

def get_wash_index(w_speed, condition):
    if w_speed >= 6.0: return "alert", f"⚠️ 강풍 주의 (풍속 {w_speed}m/s)! 세차 시 약재가 마르거나 문이 꺾일 수 있습니다."
    if "비" in condition or "눈" in condition: return "alert", f"🚫 {condition} 예보가 있습니다! 오늘 세차는 참으시는 게 좋습니다."
    return "safe", "✨ 세차하기 아주 좋은 날씨입니다! (오천 버블스타로 출발)"

status_type, status_msg = get_wash_index(wind_speed, weather_condition)

# --- 4. 메인 화면 구성 ---
st.markdown("<h1 style='font-size:48px; letter-spacing:-2px;'>APEX <span style='color:#3B82F6;'>PLATFORM</span></h1>", unsafe_allow_html=True)
st.markdown("📍 **경북 포항시 남구 오천읍 문덕로79번길 26 (오천 버블스타)**")

# 기상 경보 알림창
if status_type == "alert":
    st.markdown(f"<div class='alert-card'><h3>🚨 긴급 기상 알림</h3><p style='font-size:18px;'>{status_msg}</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div class='safe-card'><h3>✅ 세차 지수 최고</h3><p style='font-size:18px;'>{status_msg}</p></div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 프리미엄 가이드", "🗓️ 크루 일정", "👤 회원/관리자"])

with tab1:
    st.markdown("### 🧼 전문가 세차 8단계 가이드")
    for step, desc in detailing_guide.items():
        st.markdown(f"""
            <div class="premium-card">
                <h4 style="color:#3B82F6 !important; margin:0;">{step}</h4>
                <p style="margin-top:10px; font-size:15px; opacity:0.9;">{desc}</p>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 🗓️ 세차 벙개 일정")
    if st.session_state.logged_in_user:
        with st.expander("➕ 일정 등록"):
            d = st.date_input("날짜")
            t = st.time_input("시간")
            if st.button("등록하기"):
                st.session_state.wash_schedule.append({"date": str(d), "time": str(t), "user": st.session_state.logged_in_user})
                st.rerun()
    
    for s in reversed(st.session_state.wash_schedule):
        st.markdown(f"<div class='premium-card'>📅 <b>{s['date']} {s['time']}</b> - 주최: {s['user']}</div>", unsafe_allow_html=True)

with tab3:
    if st.session_state.logged_in_user == "admin":
        st.markdown("### ⚙️ 관리자 회원 관리")
        for uid, info in st.session_state.users.items():
            col_u, col_t = st.columns([2, 1])
            col_u.write(f"🆔 {uid} ({info['name']})")
            new_tier = col_t.selectbox("등급 변경", ["일반", "정회원", "실버", "골드"], key=uid)
            st.session_state.users[uid]["tier"] = new_tier
        st.button("변경사항 저장")
    else:
        # 로그인/가입 UI
        if not st.session_state.logged_in_user:
            c1, c2 = st.columns(2)
            with c1:
                u = st.text_input("아이디")
                p = st.text_input("비밀번호", type="password")
                if st.button("로그인"):
                    if u in st.session_state.users and st.session_state.users[u]['pw'] == p:
                        st.session_state.logged_in_user = u
                        st.rerun()
            with c2:
                st.info("회원가입은 관리자 승인 후 등급이 부여됩니다.")
        else:
            st.write(f"현재 접속: **{st.session_state.logged_in_user}** 님")
            if st.button("로그아웃"):
                st.session_state.logged_in_user = None
                st.rerun()

# --- 5. 실시간 유가 (기존 기능 유지) ---
st.sidebar.markdown("### ⛽ 오천읍 유가 정보")
st.sidebar.markdown("""
<div class="premium-card">
<b>GS칼텍스 오천</b>: 1,615원<br>
<b>S-OIL 셀프</b>: 1,598원<br>
<small>반경 5Km 최저가 기준</small>
</div>
""", unsafe_allow_html=True)
