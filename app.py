import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 앱 설정 및 커스텀 디자인 (귀엽고 세련된 느낌) ---
st.set_page_config(page_title="팰리 당근 모임", page_icon="🥕", layout="wide")

st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .main { background-color: #fdfcfb; }
    div.stButton > button:first-child {
        background-color: #ff8a3d;
        color: white;
        border-radius: 10px;
        border: none;
        height: 3em;
        font-weight: bold;
    }
    /* 카드 형태의 게시글 스타일 */
    .wash-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #ff8a3d;
        margin-bottom: 10px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 데이터 저장소 초기화 (세션 동안 유지)
if 'posts' not in st.session_state: st.session_state.posts = []
if 'meets' not in st.session_state: st.session_state.meets = []

# --- 2. 사이드바 (접이식 메뉴 구성) ---
with st.sidebar:
    st.image("https://img.icons8.com/bubbles/200/car.png")
    st.title("🥕 팰리 당근 모임")
    st.markdown("---")
    menu = st.radio(
        "메뉴를 선택하세요",
        ["🏠 홈 & 세차 지수", "📅 벙개 일정 모집", "📚 세차 고수 대백과", "📸 세차 인증 & 평가", "💬 자유게시판 & 용품"]
    )
    st.markdown("---")
    st.caption("© 2024 팰리세이드 당근 동호회")

# --- 3. 홈 & 실시간 날씨 알람 ---
if menu == "🏠 홈 & 세차 지수":
    st.title("✨ 팰리세이드 당근 모임 매니저")
    
    # 날씨 데이터 로직 (추후 API 연동 가능)
    wind_speed = 4.5  # 가상 데이터
    rain_prob = 10    # 가상 데이터
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🌦️ 오늘 우리동네 세차 예보")
        inner_col1, inner_col2 = st.columns(2)
        inner_col1.metric("현재 풍속", f"{wind_speed} m/s")
        inner_col2.metric("강수 확률", f"{rain_prob} %")
        
        if wind_speed >= 6.0:
            st.error(f"🚫 **세차 금지!** 풍속이 {wind_speed}m/s로 강합니다. 팰리 덩치에 바람 맞으면 스크래치 나요!")
        elif rain_prob > 40:
            st.warning("☁️ **세차 비추천!** 비 예보가 있어 기껏 낸 광이 사라질 수 있어요.")
        else:
            st.success("✅ **세차하기 최적의 날!** 지금 바로 아지트로 출발하세요.")
            
    with col2:
        st.subheader("📍 아지트 정보")
        st.info("**워시존 팰리점**")
        st.link_button("네이버 지도 보기", "https://naver.me/F6lTwCXz")

# --- 4. 벙개 일정 모집 ---
elif menu == "📅 벙개 일정 모집":
    st.header("🤝 이번 주 벙개 모집")
    
    with st.form("meet_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        m_title = c1.text_input("벙개 제목", placeholder="밤 세차 하실 분?")
        m_type = c2.selectbox("종류", ["세차 벙개", "커피/식사", "DIY/나눔"])
        m_date = st.date_input("날짜")
        m_content = st.text_area("상세 내용")
        if st.form_submit_button("벙개 등록"):
            st.session_state.meets.append({"title": m_title, "type": m_type, "date": m_date, "content": m_content})
            st.balloons()

    st.markdown("### 📌 현재 진행 중인 벙개")
    for m in reversed(st.session_state.meets):
        st.markdown(f"""
        <div class="wash-card">
            <h4>[{m['type']}] {m['title']}</h4>
            <p>🗓 일시: {m['date']} | 내용: {m['content']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("참여하기", key=m['title']):
            st.toast("참여 신청이 완료되었습니다!")

# --- 5. 세차 고수 대백과 (부위별 상세 가이드) ---
elif menu == "📚 세차 고수 대백과":
    st.header("📖 팰리세이드 전문 세차 가이드")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🛁 도장면(3PH)", "🛞 휠/타이어", "🛋️ 실내/가죽", "💎 유리/코팅", "🧪 용품학개론"])
    
    with tab1:
        st.markdown("### 🧪 고수들의 3PH 공법\n1. **알칼리(pH13):** 프리워시로 단백질/벌레 제거\n2. **산성(pH1~2):** 워터스팟 및 무기질 오염 제거\n3. **중성(pH7):** 풍부한 윤활력의 버킷 세차")
    with tab2:
        st.markdown("### 🛞 휠 & 타이어 케어\n- **휠:** 철분 제거제 도포 후 전용 브러쉬질\n- **타이어:** 갈변 제거제로 묵은 때 제거 필수!\n- **마무리:** 타이어 광택제로 새 타이어 느낌 유지")
    with tab3:
        st.markdown("### 🛋️ 실내 세정 및 코팅\n- 가죽 세정제로 오염 제거 후 **컨디셔너 도포** (가죽 갈라짐 방지)\n- 하이그로시 부위는 부드러운 타월로 지문 제거")
    with tab4:
        st.markdown("### 💎 유리창 유막제거/발수\n- 장마철 필수! 산화세륨으로 유막을 완전히 친수 상태로 만드세요.\n- 발수 코팅제는 겹치듯이 꼼꼼하게 발라야 합니다.")
    with tab5:
        st.markdown("### 🧪 용품 선택 가이드\n- **왁스:** 깊은 광택감(카나우바 등)\n- **코팅제:** 긴 지속력과 쉬운 관리(물왁스, 실란트 등)")

# --- 6. 세차 인증 & 평가 ---
elif menu == "📸 세차 인증 & 평가":
    st.header("📸 오늘 내 팰리 광빨은?")
    
    with st.expander("인증샷 올리기"):
        img = st.file_uploader("사진 선택", type=["jpg", "png"])
        comment = st.text_input("한줄평")
        if st.button("인증완료"):
            st.success("사진이 등록되었습니다!")

    if img:
        st.image(img, caption=f"오늘의 인증샷: {comment}")
        score = st.select_slider("회원님들의 평가는?", options=["초보", "깨끗함", "눈부심", "거울인줄", "디테일링 고수"])
        st.write(f"현재 평가 지수: **{score}**")

# --- 7. 자유게시판 ---
elif menu == "💬 자유게시판 & 용품":
    st.header("💬 자유 게시판")
    with st.form("free_form", clear_on_submit=True):
        f_title = st.text_input("제목")
        f_content = st.text_area("내용")
        if st.form_submit_button("글 올리기"):
            st.session_state.posts.append({"title": f_title, "content": f_content, "time": datetime.now().strftime("%H:%M")})
    
    for p in reversed(st.session_state.posts):
        st.chat_message("user").write(f"**{p['title']}** ({p['time']})\n\n{p['content']}")