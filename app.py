import streamlit as st
from datetime import datetime
import pandas as pd

# --- 1. 시인성 최적화 디자인 시스템 ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    .stApp { background-color: #0F172A !important; }
    h1, h2, h3, h4, p, span, div, label, li { color: #FFFFFF !important; font-family: 'Pretendard', sans-serif !important; }
    
    /* 카드 디자인 */
    .premium-card {
        background: rgba(30, 41, 59, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    /* 등급 배지 스타일 */
    .tier-badge {
        padding: 3px 10px; border-radius: 6px; font-weight: 800; font-size: 11px; margin-right: 5px;
    }
    .tier-admin { background: #EF4444; color: white !important; }
    .tier-gold { background: #F59E0B; color: black !important; }
    .tier-silver { background: #94A3B8; color: black !important; }
    .tier-pro { background: #3B82F6; color: white !important; }
    .tier-normal { background: #475569; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 관리 시스템 (DB 역할) ---
if 'users' not in st.session_state:
    st.session_state.users = {
        "admin": {"pw": "admin77", "tier": "관리자", "name": "마스터세차"},
        "test": {"pw": "1234", "tier": "실버 회원", "name": "포항광쟁이"}
    }
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None
if 'wash_schedule' not in st.session_state: st.session_state.wash_schedule = []

# --- 3. 로그인 및 회원가입 로직 (사이드바) ---
with st.sidebar:
    st.markdown("<h2 style='color:#3B82F6 !important;'>🏔️ MEMBERSHIP</h2>", unsafe_allow_html=True)
    
    if st.session_state.logged_in_user is None:
        auth_mode = st.radio("접속 모드", ["로그인", "회원가입"])
        if auth_mode == "로그인":
            u_id = st.text_input("아이디")
            u_pw = st.text_input("비밀번호", type="password")
            if st.button("접속", use_container_width=True):
                if u_id in st.session_state.users and st.session_state.users[u_id]["pw"] == u_pw:
                    st.session_state.logged_in_user = u_id
                    st.rerun()
                else: st.error("정보가 틀렸습니다.")
        else:
            new_id = st.text_input("희망 아이디")
            new_name = st.text_input("활동 닉네임")
            new_pw = st.text_input("비밀번호 설정", type="password")
            if st.button("가입신청", use_container_width=True):
                st.session_state.users[new_id] = {"pw": new_pw, "tier": "일반회원", "name": new_name}
                st.success("환영합니다! 이제 로그인하세요.")
    else:
        user = st.session_state.users[st.session_state.logged_in_user]
        st.success(f"{user['name']}님 환영합니다!")
        st.info(f"현재 등급: {user['tier']}")
        if st.button("로그아웃"):
            st.session_state.logged_in_user = None
            st.rerun()

# --- 4. 메인 콘텐츠 ---
st.markdown("<h1 style='font-size:42px;'>APEX <span style='color:#3B82F6;'>PLATFORM</span></h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 대시보드", "🗓️ 세차 일정(벙개)", "⚙️ 관리자 센터"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### ⛽ 실시간 유가 (반경 5km)")
        # 유가 데이터 카드 시각화 (기존 코드 유지)
        st.markdown("""<div class='premium-card'><b>GS칼텍스 오천주유소</b> | 휘발유 1,615원</div>""", unsafe_allow_html=True)
        st.markdown("""<div class='premium-card'><b>S-OIL 셀프 오천점</b> | 휘발유 1,598원</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("### 🫧 세차 가이드 8단계")
        steps = ["1. 중성 세차", "2. 2PH 세차", "3. 3PH 세차", "4. 유막제거", "5. 휠/타이어", "6. 외장 왁스", "7. 실내 세정", "8. 시트 코팅"]
        st.markdown(f"<div class='premium-card'>{'<br>'.join(steps)}</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### 🗓️ 세차 크루 일정 관리")
    if st.session_state.logged_in_user:
        with st.expander("➕ 새 세차 일정 만들기"):
            w_date = st.date_input("날짜")
            w_time = st.time_input("시간")
            w_loc = st.text_input("장소", value="오천 버블스타")
            if st.button("일정 등록"):
                st.session_state.wash_schedule.append({
                    "date": str(w_date), "time": str(w_time), "loc": w_loc, 
                    "host": st.session_state.users[st.session_state.logged_in_user]['name']
                })
                st.rerun()
    
    if not st.session_state.wash_schedule:
        st.write("등록된 세차 일정이 없습니다.")
    else:
        for s in st.session_state.wash_schedule:
            st.markdown(f"""
                <div class="premium-card">
                    <span style="color:#3B82F6; font-weight:800;">{s['date']} {s['time']}</span><br>
                    <b>장소:</b> {s['loc']} | <b>주최:</b> {s['host']}
                </div>
            """, unsafe_allow_html=True)

with tab3:
    if st.session_state.logged_in_user == "admin":
        st.markdown("### 👑 회원 등급 마스터 제어")
        # 회원 목록 데이터프레임
        user_list = []
        for uid, info in st.session_state.users.items():
            user_list.append({"ID": uid, "닉네임": info['name'], "현재 등급": info['tier']})
        
        df = pd.DataFrame(user_list)
        st.table(df)
        
        target_uid = st.selectbox("등급을 변경할 회원 선택", df['ID'])
        new_tier = st.selectbox("부여할 등급", ["일반회원", "정회원", "실버 회원", "골드 회원"])
        
        if st.button("등급 즉시 변경"):
            st.session_state.users[target_uid]["tier"] = new_tier
            st.success(f"{target_uid}님의 등급이 {new_tier}로 변경되었습니다!")
            st.rerun()
    else:
        st.warning("관리자 권한이 필요한 메뉴입니다.")

# 하단 푸터 (기존 디자인 유지)
st.markdown("<br><br><div style='text-align:center; color:#475569;'>© 2024 APEX POHANG CAR CLUB</div>", unsafe_allow_html=True)
