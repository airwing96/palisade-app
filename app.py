import streamlit as st

# --- 1. 스타일 설정 (인스타/유튜브 트렌드 반영) ---
st.set_page_config(page_title="APEX | Premium Mobility", page_icon="🏔️", layout="wide")

st.markdown("""
    <style>
    /* 요즘 유행하는 가독성 높은 폰트 스택 적용 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Lexend:wght@700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    .main { background-color: #f8f9fa; }

    /* APEX 타이틀 (인스타 감성 굵은 폰트) */
    .brand-title {
        font-family: 'Lexend', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -2px;
        color: #0f172a;
        margin-bottom: 0px;
        line-height: 1;
    }

    .brand-subtitle {
        font-size: 0.9rem;
        color: #64748b;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 50px;
        font-weight: 500;
    }

    /* 카드 디자인 (애플/에어비앤비 스타일) */
    .card {
        background-color: white;
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        border: 1px solid #f1f5f9;
        margin-bottom: 20px;
    }

    .card-label {
        color: #3b82f6;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 12px;
    }

    /* 버튼 (요즘 스타일의 둥글고 묵직한 디자인) */
    .stButton>button {
        border-radius: 12px;
        background-color: #0f172a;
        color: white;
        border: none;
        width: 100%;
        height: 52px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
        transform: translateY(-2px);
    }

    /* 하단 바 (모바일 앱 스타일 고정) */
    .bottom-nav {
        display: flex;
        justify-content: space-around;
        background-color: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-top: 1px solid #e2e8f0;
        position: fixed;
        bottom: 0; left: 0; right: 0;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 브랜드 헤더 ---
st.markdown("<div style='text-align: center; padding: 60px 0 20px 0;'>", unsafe_allow_html=True)
st.markdown("<div class='brand-title'>APEX</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>High-End Mobility Club</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 3. 3열 구성 (이미지 UI 최신화) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <div class="card-label">Next Session</div>
            <div class="card-title">드라이브 벙개</div>
            <p style='color:#64748b; font-size:0.95rem; line-height:1.6;'>
                이번 주 토요일 밤,<br>
                정점의 경로를 함께 달립니다.
            </p>
            <div style="background-color:#f8f9fa; padding:12px; border-radius:10px; font-size:0.85rem; color:#475569;">
                📍 목적지: 가평 스타벅스 R
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("세션 신청하기")

with col2:
    st.markdown("""
        <div class="card">
            <div class="card-label">Maintenance</div>
            <div class="card-title">디테일링 랩</div>
            <p style='color:#64748b; font-size:0.95rem; line-height:1.6;'>
                전문가들이 공유하는<br>
                하이엔드 차량 관리 기술.
            </p>
            <div style="display:flex; align-items:center; margin-top:10px;">
                <div style="width:40px; height:40px; background-color:#eff6ff; border-radius:8px; display:flex; align-items:center; justify-content:center; margin-right:10px;">🧼</div>
                <div style="font-size:0.85rem; font-weight:600;">초보를 위한 3PH 가이드</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <div class="card-label">Lounge</div>
            <div class="card-title">멤버 커뮤니티</div>
            <div style="display:flex; align-items:center; margin-bottom:15px;">
                <div style="width:32px; height:32px; background-color:#eee; border-radius:50%; margin-right:10px;"></div>
                <div style="font-size:0.85rem; color:#1e293b;">"오늘 세차장 자리 있나요?"</div>
            </div>
            <div style="display:flex; align-items:center;">
                <div style="width:32px; height:32px; background-color:#eee; border-radius:50%; margin-right:10px;"></div>
                <div style="font-size:0.85rem; color:#1e293b;">"광택제 추천 부탁드립니다!"</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. 하단 네비게이션 ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="bottom-nav">
        <div style="text-align:center; color:#0f172a; font-weight:700;"><span style="font-size:20px;">🏠</span><br><span style="font-size:10px;">HOME</span></div>
        <div style="text-align:center; color:#94a3b8;"><span style="font-size:20px;">🛣️</span><br><span style="font-size:10px;">ROAD</span></div>
        <div style="text-align:center; color:#94a3b8;"><span style="font-size:20px;">💬</span><br><span style="font-size:10px;">CHAT</span></div>
        <div style="text-align:center; color:#94a3b8;"><span style="font-size:20px;">👤</span><br><span style="font-size:10px;">MY</span></div>
    </div>
    """, unsafe_allow_html=True)
