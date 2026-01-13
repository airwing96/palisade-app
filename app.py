import streamlit as st
from datetime import datetime
import pandas as pd

# --- 1. 디자인 시스템 및 시인성 고정 ---
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
    .tier-badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
    }
    .tier-gold { background-color: #F59E0B; color: #000 !important; }
    .tier-silver { background-color: #94A3B8; color: #000 !important; }
    .tier-regular { background-color: #3B82F6; color: #fff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 세션 관리 (회원 및 게시판) ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "1234", "tier": "관리자"}, "test": {"pw": "1111", "tier": "GOLD"}}
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None
if 'posts' not in st.session_state:
    st.session_state.posts = []

# --- 3. 세부 기능 데이터 (복구 및 유지) ---
oil_data = [
    {"name": "GS칼텍스 오천주유소", "dist": "1.2km", "gas": "1,615", "diesel": "1,495"},
    {"name": "SK에너지 문덕주유소", "dist": "0.8km", "gas": "1,620", "diesel": "1,505"},
    {"name": "S-OIL 셀프 오천점", "dist": "2.1km", "gas": "1,598", "diesel": "1,480"}
]

# 전문가급 세차 가이드 데이터 (이미지 포함)
guide_detail = {
    "1. 중성 세차": {"desc": "도장면 손상을 최소화하는 기초 공정입니다.", "img": "https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?w=500", "tip": "고압수로 충분히 이물질을 걷어내세요."},
    "2. 2PH 세차": {"desc": "알칼리 프리워시와 중성 샴푸의 조합입니다.", "img": "https://images.unsplash.com/photo-1607860108855-64acf2078ed9?w=500", "tip": "프리워시 약재가 마르기 전 헹구는 것이 핵심!"},
    "3. 3PH 세차": {"desc": "산성-알칼리-중성 순서의 마스터 공법입니다.", "img": "https://images.unsplash.com/photo-1552930294-6b595f4c2974?w=500", "tip": "미네랄 때 제거에는 산성 샴푸가 필수입니다."},
    "4. 유막제거/발수": {"desc": "유리 오염을 제거하고 코팅을 입힙니다.", "img": "https://images.unsplash.com/photo-1601362840469-51e4d8d59085?w=500", "tip": "유막 제거 후 친수 상태 확인이 중요합니다."},
    "5. 휠/타이어": {"desc": "분진 제거와 고무 보호 단계입니다.", "img": "https://images.unsplash.com/photo-1486006920555-c77dcf18193c?w=500", "tip": "갈변 제거제는 타이어에만 사용하세요."},
    "6. 외장 왁스": {"desc": "LSP(최종 보호제) 공정입니다.", "img": "https://images.unsplash.com/photo-1599256621730-535171e28e50?w=500", "tip": "얇게 펴 바르고 버핑 타임을 꼭 지키세요."},
    "7. 실내 세정": {"desc": "내장재 클리닝 및 보습 단계입니다.", "img": "https://images.unsplash.com/photo-1507133311040-ae3ba9412d76?w=500", "tip": "가죽 전용 관리제로 수분 공급이 필요합니다."},
    "8. 시트 코팅": {"desc": "이염 방지를 위한 코팅막 형성입니다.", "img": "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=500", "tip": "코팅 후 충분한 경화 시간이 필요합니다."}
}

# --- 4. 로그인 및 회원가입 섹션 (독창적 구성) ---
def login_sidebar():
    with st.sidebar:
        st.markdown("### 👤 MEMBER CENTER")
        if st.session_state.logged_in_user is None:
            tab_auth = st.tabs(["로그인", "가입"])
            with tab_auth[0]:
                uid = st.text_input("아이디", key="l_id")
                upw = st.text_input("비밀번호", type="password", key="l_pw")
                if st.button("접속하기"):
                    if uid in st.session_state.users and st.session_state.users[uid]["pw"] == upw:
                        st.session_state.logged_in_user = uid
                        st.rerun()
                    else: st.error("정보가 일치하지 않습니다.")
            with tab_auth[1]:
                new_id = st.text_input("아이디 설정", key="s_id")
                new_pw = st.text_input("비밀번호 설정", type="password", key="s_pw")
                if st.button("크루 합류하기"):
                    st.session_state.users[new_id] = {"pw": new_pw, "tier": "일반"}
                    st.success("가입 완료! 로그인 해주세요.")
        else:
            user_info = st.session_state.users[st.session_state.logged_in_user]
            st.markdown(f"**{st.session_state.logged_in_user}** 님 환영합니다!")
            st.markdown(f"<span class='tier-badge tier-regular'>{user_info['tier']} 회원</span>", unsafe_allow_html=True)
            if st.button("로그아웃"):
                st.session_state.logged_in_user = None
                st.rerun()

login_sidebar()

# --- 5. 메인 레이아웃 ---
st.markdown("<h1 style='font-size:45px;'>APEX <span style='color:#3B82F6;'>POHANG</span></h1>", unsafe_allow_html=True)
col_left, col_mid, col_right = st.columns([1, 1.2, 1], gap="large")

with col_left:
    st.markdown("### ⛽ 주변 5Km 유가")
    for oil in oil_data:
        st.markdown(f"""
            <div class="premium-card">
                <div style="display:flex; justify-content:space-between;">
                    <span style="font-weight:700;">{oil['name']}</span>
                    <span style="color:#60A5FA; font-weight:800;">{oil['gas']}원</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

with col_mid:
    st.markdown("### 🧼 EXPERT GUIDE")
    st.info("단계를 클릭하면 전문가용 세부 설명이 나옵니다.")
    for title, content in guide_detail.items():
        with st.expander(f"✨ {title}"):
            st.image(content['img'], use_container_width=True)
            st.markdown(f"**상세 설명:** {content['desc']}")
            st.warning(f"💡 전문가 TIP: {content['tip']}")

with col_right:
    st.markdown("### 💬 LOUNGE")
    # 관리자 기능 (등급 변경 기능 포함)
    if st.session_state.logged_in_user == "admin":
        with st.expander("⚙️ 관리자: 회원 등급 관리"):
            target_user = st.selectbox("회원 선택", list(st.session_state.users.keys()))
            new_tier = st.selectbox("등급 변경", ["일반", "정회원", "SILVER", "GOLD"])
            if st.button("등급 업데이트"):
                st.session_state.users[target_user]["tier"] = new_tier
                st.success("등급이 변경되었습니다.")

    with st.form("guest", clear_on_submit=True):
        msg = st.text_area("크루 소식 남기기")
        if st.form_submit_button("등록"):
            if st.session_state.logged_in_user:
                st.session_state.posts.append({"user": st.session_state.logged_in_user, "msg": msg, "time": datetime.now().strftime("%H:%M")})
                st.rerun()
            else: st.error("로그인이 필요합니다.")

    for p in reversed(st.session_state.posts[-3:]):
        st.markdown(f"<div class='premium-card'><b>{p['user']}</b> <small>{p['time']}</small><br>{p['msg']}</div>", unsafe_allow_html=True)

# 하단 고정바
st.markdown("<div style='margin-top:100px;'></div>", unsafe_allow_html=True)
foot = st.columns(4)
for i, m in enumerate(["HOME", "LAB", "TALK", "MY"]):
    foot[i].button(m, use_container_width=True)
