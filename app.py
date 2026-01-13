import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 스타일 설정 (다크모드에서도 선명하게 보이도록 강제 설정) ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

# 세션 상태 초기화
if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    /* 배경과 폰트 강제 지정 (가장 중요) */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    .stApp {
        background-color: #f2f4f7 !important; /* 이미지와 동일한 연회색 배경 */
    }
    
    /* 모든 텍스트 기본색을 어두운 색으로 고정 */
    * {
        font-family: 'Pretendard', sans-serif !important;
        color: #1e293b !important;
    }

    /* 카드 섹션: 흰색 배경에 그림자 효과 */
    .card {
        background-color: white !important;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }

    /* 제목 스타일 (유튜브/숏츠 감성 볼드) */
    .brand-title {
        font-size: 32px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        color: #0f172a !important;
    }
    .brand-sub {
        text-align: center;
        color: #64748b !important;
        font-size: 14px;
        margin-bottom: 30px;
    }

    /* 탭 메뉴 글자색 보정 */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #475569 !important;
        font-weight: 700;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: white !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        height: 50px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #3b82f6 !important;
        background-color: #f8fafc !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 상단 브랜딩 ---
st.markdown("<div class='brand-title'>APEX POHANG</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-sub'>오천 버블스타 크루 전용 스마트 라운지</div>", unsafe_allow_html=True)

# --- 3. 3개 열 레이아웃 (이미지 UI 재현) ---
col1, col2, col3 = st.columns([1, 1.2, 1])

# [왼쪽 열: 실시간 정보]
with col1:
    st.markdown("### 🌤️ 실시간 정보")
    st.markdown("""
        <div class="card">
            <p style="color:#3b82f6 !important; font-weight:800; font-size:12px;">WEATHER</p>
            <h3 style="margin:5px 0;">포항 오천읍 5.2°C</h3>
            <p style="font-size:14px;">풍속: <b>3.2m/s</b> (세차 적합 ✨)</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="card">
            <p style="color:#f59e0b !important; font-weight:800; font-size:12px;">OIL PRICE</p>
            <p style="margin:5px 0;">⛽ 휘발유: <b>1,625원</b></p>
            <p style="margin:5px 0;">⛽ 경유: <b>1,510원</b></p>
            <p style="margin:5px 0;">⛽ 고급유: <b>1,890원</b></p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("📍 주변 맛집/카페 소개"):
        st.write("☕ **인더그레이**: 문덕 핫플 카페")
        st.write("🍱 **뚝배기 주물럭**: 오천읍 노포 맛집")

# [가운데 열: 디테일링 LAB]
with col2:
    st.markdown("### 🧼 디테일링 LAB")
    tabs = st.tabs(["세차 방법", "희석 계산기", "추천 용품"])
    
    with tabs[0]:
        st.markdown("""
        <div class="card">
            <ol style="font-size:14px; line-height:1.8;">
                <li><b>중성 세차:</b> 안전한 오염물 제거</li>
                <li><b>2PH 세차:</b> 알칼리+중성 교차 세정</li>
                <li><b>3PH 세차:</b> 산성+알칼리+중성 매니아 세차</li>
                <li><b>유막제거/발수:</b> 유리 유막 제거 후 코팅</li>
                <li><b>휠/타이어:</b> 철분 제거 및 드레싱</li>
                <li><b>외장 왁스:</b> 고체왁스/LSP 광택</li>
                <li><b>내장재 세정:</b> 실내 크리닝 및 보호</li>
                <li><b>시트 코팅:</b> 가죽 가디언 코팅</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        total = st.number_input("목표 용량 (ml)", value=1000, step=100)
        ratio = st.number_input("희석 비율 (1:N)", value=10, step=1)
        res = total / (ratio + 1)
        st.info(f"결과: 원액 {res:.1f}ml + 물 {total-res:.1f}ml")
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        st.write("라보코스메티카, 코흐케미, 메니악, 기온쿼츠 등 강력 추천")

# [오른쪽 열: 소통과 지도]
with col3:
    st.markdown("### 💬 소통과 위치")
    st.markdown("""
        <div class="card">
            <p style="font-weight:800; margin-bottom:5px;">오천 버블스타 세차장</p>
            <p style="color:#64748b !important; font-size:13px;">경북 포항시 남구 오천읍 문덕로79번길 26</p>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("N 네이버 지도로 보기", "https://naver.me/F6lTwCXz", use_container_width=True)

    st.write("")
    st.markdown("<b>최신 후기/자유게시판</b>", unsafe_allow_html=True)
    with st.form("board", clear_on_submit=True):
        u_name = st.text_input("닉네임", placeholder="이름")
        u_msg = st.text_area("내용", placeholder="세차 소감을 남겨주세요")
        if st.form_submit_button("등록"):
            st.session_state.posts.append({"name": u_name, "msg": u_msg, "time": datetime.now().strftime("%H:%M")})
            st.rerun()
    
    for p in reversed(st.session_state.posts[-3:]):
        st.markdown(f"<div style='background:white; padding:10px; border-radius:10px; margin-top:5px; border:1px solid #e2e8f0;'><b>{p['name']}</b>: {p['msg']} <small style='color:gray !important;'>{p['time']}</small></div>", unsafe_allow_html=True)

# --- 4. 하단 고정 메뉴 (이미지 재현) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
with m1: st.button("🏠\n홈", use_container_width=True)
with m2: st.button("🧪\n계산기", use_container_width=True)
with m3: st.button("💬\n라운지", use_container_width=True)
with m4: st.button("👤\n마이", use_container_width=True)
