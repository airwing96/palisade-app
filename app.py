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
        transition: transform 0.3s;
    }
    .premium-card:hover { transform: translateY(-5px); border-color: #3B82F6; }
    
    .brand-header {
        display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;
    }
    .brand-badge {
        background: linear-gradient(135deg, #3B82F6, #1D4ED8); 
        color: white; padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 800;
    }
    .official-tag { color: #10B981 !important; font-size: 12px; font-weight: 600; }
    .best-item { background: rgba(255, 255, 255, 0.05); padding: 10px; border-radius: 10px; margin-top: 10px; border-left: 3px solid #3B82F6; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 강화된 브랜드 데이터 (Best 라인업 & 공식판매처) ---
brand_details = {
    "라보코스메티카": {
        "best": ["프리머스(Primus)", "퓨리피카(Purifica)", "사무(Sempra)"],
        "shop": "엔공구, 슬릭핸즈 공식 스토어",
        "desc": "이탈리아 마프라(Mafra)의 하이엔드 라인. 3PH 세차 시스템의 창시자.",
        "img_query": "Labocosmetica detailing products line"
    },
    "기온쿼츠": {
        "best": ["Q2M 웨트코트", "Q2M 아이언", "Q2M 프리워시"],
        "shop": "기온쿼츠 코리아 공식 홈페이지",
        "desc": "전 세계 디테일러들이 사랑하는 세련된 패키징과 확실한 코팅 성능.",
        "img_query": "Gyeon Quartz detailing product kit"
    },
    "코흐케미": {
        "best": ["Gsf(젠틀스노우폼)", "H9.02(컴파운드)", "Pw(프로텍트워시)"],
        "shop": "독특닷컴, 공식 수입원 전용관",
        "desc": "독일 벤츠, BMW 공식 인증 케미컬. 정밀한 화학 공학의 정수.",
        "img_query": "Koch-Chemie car care products"
    },
    "더클래스": {
        "best": ["불렛(Bullet) 물왁스", "클린앤코트", "하이브리드 코트"],
        "shop": "더클래스 공식 네이버 스마트스토어",
        "desc": "대한민국 No.1 슬릭감. 한국 기후에 최적화된 고성능 LSP 전문.",
        "img_query": "The Class car detailing products South Korea"
    },
    "파이어볼": {
        "best": ["이지커트 컴파운드", "신라(Silla) 코팅제", "타월 시리즈"],
        "shop": "파이어볼 코리아 공식 쇼핑몰",
        "desc": "전 세계 40개국 수출. 압도적인 발수력과 비딩을 선사하는 국산 하이테크.",
        "img_query": "Fireball car care detailing line"
    },
    "메니악": {
        "best": ["휠&타이어 클리너", "블랙라인 샴푸", "디테일러"],
        "shop": "마프라 코리아 공식 스토어",
        "desc": "마프라 50주년 기념 라인. 극한의 퍼포먼스를 즐기는 매니아 전용.",
        "img_query": "Mafra Maniac Line products"
    }
}

# --- 3. 시스템 설정 유지 ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "admin77", "tier": "관리자", "name": "마스터"}}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None

# --- 4. 메인 UI ---
st.markdown("<h1 style='font-size:45px;'>APEX <span style='color:#3B82F6;'>STORE</span></h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🛍️ 프리미엄 브랜드관", "🧼 세차 가이드", "🗓️ 일정/회원"])

with tab1:
    st.markdown("### 🏷️ 글로벌 프리미엄 브랜드 & Best 라인업")
    st.write("오천 버블스타 멤버들을 위해 검증된 브랜드 공식 정보입니다.")
    
    # 브랜드 카드 출력
    for name, info in brand_details.items():
        st.markdown(f"""
            <div class="premium-card">
                <div class="brand-header">
                    <div>
                        <span class="brand-badge">{name}</span>
                        <span class="official-tag">✓ Official Store 인증</span>
                    </div>
                </div>
                <div style="display: flex; gap: 20px; align-items: flex-start;">
                    <div style="flex: 1;">
                        <p style="font-size: 15px; opacity: 0.9; margin-bottom: 15px;">{info['desc']}</p>
                        <p style="font-size: 13px; color: #94A3B8 !important;">🛒 <b>공식 판매처:</b> {info['shop']}</p>
                        <div class="best-item">
                            <span style="color: #60A5FA; font-weight: 800; font-size: 14px;">🏆 BEST 3 라인업</span><br>
                            <span style="font-size: 14px;">{' / '.join(info['best'])}</span>
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # 각 브랜드 카드 아래에 시각적 이해를 돕기 위한 이미지 태그 삽입
        st.write(f"}]")

with tab2:
    st.markdown("### 🧼 전문가 세차 8단계")
    guide = {
        "1. 중성 세차": "고압수 후 도장면 손상 없는 중성 세정", "2. 2PH 세차":
