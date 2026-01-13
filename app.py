import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 스타일 및 시인성 설정 ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 배경 및 전역 폰트 설정 (다크모드 완벽 대응) */
    .stApp { background-color: #F8FAFC !important; }
    * { font-family: 'Pretendard', sans-serif !important; color: #1E293B !important; }

    /* 카드 디자인 */
    .app-card {
        background-color: #FFFFFF !important;
        border-radius: 22px !important;
        padding: 24px !important;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05) !important;
        margin-bottom: 20px !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* 강조 텍스트 */
    .station-name { font-size: 15px; font-weight: 700; color: #0F172A !important; }
    .price-tag { font-size: 16px; font-weight: 800; color: #3B82F6 !important; }
    .neon-text { color: #3B82F6 !important; font-weight: 800; }
    
    /* 지도 버튼 커스텀 */
    .btn-naver {
        background: #03C75A !important;
        color: white !important;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-weight: 800;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 위치 기반 유가 정보 데이터 (포항 오천 반경 5Km) ---
# 실제 오천읍 문덕리 반경 5Km 내 주요 주유소 정보를 수동으로 매핑한 데이터입니다.
oil_data = [
    {"name": "GS칼텍스 오천주유소", "dist": "1.2km", "gas": "1,615", "diesel": "1,495"},
    {"name": "SK에너지 문덕주유소", "dist": "0.8km", "gas": "1,620", "diesel": "1,505"},
    {"name": "S-OIL 셀프 오천점", "dist": "2.1km", "gas": "1,598", "diesel": "1,480"},
    {"name": "현대오일뱅크 포항스틸호", "dist": "3.5km", "gas": "1,635", "diesel": "1,520"}
]

detailing_methods = {
    "1. 중성 세차": "도장면 안전 오염 제거",
    "2. 2PH 세차": "알칼리+중성 교차 세정",
    "3. 3PH 세차": "산성+알칼리+중성 마스터",
    "4. 유막제거/발수": "시야 확보 및 코팅",
    "5. 휠/타이어": "갈변 제거 및 드레싱",
    "6. 외장 왁스": "광택 및 비딩 형성",
    "7. 실내 세정": "정밀 크리닝 및 보호",
    "8. 시트 코팅": "이염 방지 및 유지"
}

# --- 3. 헤더 섹션 ---
st.markdown("<div style='text-align:center; padding:40px 0;'><h1 style='font-size:42px; font-weight:900;'>APEX POHANG</h1><p style='color:#64748B !important;'>오천 버블스타 크루 전용 스마트 라운지</p></div>", unsafe_allow_html=True)

# --- 4. 메인 3열 레이아웃 ---
col1, col2, col3 = st.columns([1, 1.2, 1], gap="large")

with col1:
    st.markdown("### ⛽ 반경 5Km 유가 정보")
    st.markdown("<div class='app-card'>", unsafe_allow_html=True)
    for oil in oil_data:
        st.markdown(f"""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; border-bottom:1px solid #F1F5F9; padding-bottom:10px;">
                <div>
                    <span class="station-name">{oil['name']}</span><br>
                    <small style="color:#94A3B8 !important;">📍 {oil['dist']}</small>
                </div>
                <div style="text-align:right;">
                    <span class="price-tag">{oil['gas']}원</span><br>
                    <small style="color:#64748B !important;">경유 {oil['diesel']}원</small>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="app-card">
            <p class="neon-text" style="font-size:12px;">WEATHER INFO</p>
            <h2 style="margin:5px 0;">5.2°C</h2>
            <p>풍속 <b>3.2m/s</b> (세차 지수: 매우 좋음 ✨)</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🧼 디테일링 LAB")
    tabs = st.tabs(["세차 가이드", "희석 계산기", "맛집/카페"])
    
    with tabs[0]:
        st.markdown("<div class='app-card'>", unsafe_allow_html=True)
        for m, d in detailing_methods.items():
            st.markdown(f"**{m}**: {d}")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with tabs[1]:
        st.markdown("<div class='app-card'>", unsafe_allow_html=True)
        vol = st.number_input("목표 용량 (ml)", value=1000)
        rat = st.number_input("비율 (1:N)", value=10)
        res = vol / (rat + 1)
        st.markdown(f"<div style='background:#F8FAFC; padding:20px; border-radius:15px; text-align:center; margin-top:20px;'><p style='margin:0;'>원액 필요량</p><h2 class='neon-text'>{res:.1f}ml</h2></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("<div class='app-card'>☕ <b>인더그레이</b>: 문덕 핫플<br>🥘 <b>뚝배기 주물럭</b>: 오천 노포 맛집</div>", unsafe_allow_html=True)

with col3:
    st.markdown("### 💬 커뮤니티")
    st.markdown("""
        <div class="app-card">
            <p style="font-weight:800; margin-bottom:5px;">오천 버블스타 세차장</p>
            <p style="font-size:13px; color:#64748B !important;">포항 남구 오천읍 문덕로79번길 26</p>
            <a href="https://naver.me/F6lTwCXz" target="_blank" class="btn-naver">🗺️ 네이버 지도로 보기</a>
        </div>
    """, unsafe_allow_html=True)

    with st.form("board", clear_on_submit=True):
        u_name = st.text_input("닉네임")
        u_msg = st.text_area("세차 후기 작성")
        if st.form_submit_button("등록"):
            if u_name and u_msg:
                st.session_state.posts.append({"name": u_name, "msg": u_msg, "time": datetime.now().strftime("%H:%M")})
                st.rerun()

    for p in reversed(st.session_state.posts[-3:]):
        st.markdown(f"<div class='app-card' style='padding:15px !important;'><b>{p['name']}</b> <small style='color:gray;'>{p['time']}</small><br>{p['msg']}</div>", unsafe_allow_html=True)

# --- 5. 하단 고정 메뉴 ---
st.markdown("<div style='margin-top:50px;'></div>", unsafe_allow_html=True)
m_cols = st.columns(4)
m_labels = ["🏠 HOME", "🧪 CALC", "💬 TALK", "👤 MY"]
for i, c in enumerate(m_cols):
    c.button(m_labels[i], key=f"foot_{i}", use_container_width=True)
