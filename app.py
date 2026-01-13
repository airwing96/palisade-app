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
    .best-item { 
        background: rgba(255, 255, 255, 0.05); 
        padding: 12px; 
        border-radius: 10px; 
        margin-top: 10px; 
        border-left: 4px solid #3B82F6; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 브랜드 데이터 (공식 로고/제품 이미지 경로 포함) ---
# 실제 이미지가 있다면 경로를 넣으시고, 현재는 예시 이미지를 보여주도록 설정했습니다.
brand_details = {
    "라보코스메티카": {
        "best": ["프리머스(Primus)", "퓨리피카(Purifica)", "사무(Sempra)"],
        "shop": "엔공구, 슬릭핸즈 공식 스토어",
        "desc": "이탈리아 마프라(Mafra)의 하이엔드 라인. 3PH 세차 시스템의 창시자.",
        "img": "https://images.unsplash.com/photo-1607860108855-64acf2078ed9?w=400" # 예시 이미지
    },
    "기온쿼츠": {
        "best": ["Q2M 웨트코트", "Q2M 아이언", "Q2M 프리워시"],
        "shop": "기온쿼츠 코리아 공식 홈페이지",
        "desc": "세련된 패키징과 압도적인 발수 성능. 전 세계 디테일러들의 워너비 브랜드.",
        "img": "https://images.unsplash.com/photo-1552933529-e359b2477262?w=400"
    },
    "코흐케미": {
        "best": ["Gsf(젠틀스노우폼)", "H9.02(컴파운드)", "Pw(프로텍트워시)"],
        "shop": "독특닷컴, 공식 수입원 전용관",
        "desc": "독일 완성차 브랜드(Benz, BMW) 공식 인증. 정밀한 화학 공학의 정수.",
        "img": "https://images.unsplash.com/photo-1599256621730-535171e28e50?w=400"
    },
    "더클래스": {
        "best": ["불렛(Bullet) 물왁스", "클린앤코트", "하이브리드 코트"],
        "shop": "더클래스 공식 네이버 스마트스토어",
        "desc": "국산 프리미엄의 자존심. 한국 기후에 최적화된 고성능 슬릭감.",
        "img": "https://images.unsplash.com/photo-1601362840469-51e4d8d59085?w=400"
    }
}

# --- 3. 시스템 설정 유지 ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": {"pw": "admin77", "tier": "관리자", "name": "마스터"}}
if 'logged_in_user' not in st.session_state: st.session_state.logged_in_user = None

# --- 4. 메인 UI ---
st.markdown("<h1 style='font-size:45px;'>APEX <span style='color:#3B82F6;'>STORE</span></h1>", unsafe_allow_html=True)

tabs = st.tabs(["🛍️ 브랜드 스토어", "🧼 세차 가이드", "👤 회원 관리"])

with tabs[0]:
    st.markdown("### 🏷️ 글로벌 프리미엄 브랜드 & Best 라인업")
    
    for name, info in brand_details.items():
        # 열 분리를 통해 사진과 설명을 나란히 배치
        col_img, col_txt = st.columns([1, 2])
        
        with col_img:
            # 사진 출력 로직 (URL 또는 로컬 파일)
            st.image(info['img'], caption=f"{name} 제품 라인업", use_container_width=True)
            
        with col_txt:
            st.markdown(f"""
                <div class="premium-card">
                    <span class="brand-badge">{name}</span>
                    <p style="margin-top:10px; font-size:15px;">{info['desc']}</p>
                    <div class="best-item">
                        <b style="color:#60A5FA;">🏆 BEST 3</b><br>
                        {', '.join(info['best'])}
                    </div>
                    <p style="font-size:12px; margin-top:10px; color:#94A3B8 !important;">🛒 판매처: {info['shop']}</p>
                </div>
            """, unsafe_allow_html=True)

with tabs[1]:
    st.markdown("### 🧼 전문가 세차 8단계")
    # 가이드 텍스트 유지
    st.write("1단계부터 8단계까지의 텍스트 가이드가 표시됩니다.")

with tabs[2]:
    st.write("관리자 및 로그인 섹션")

# 사이드바 유가 정보 유지
st.sidebar.markdown("### ⛽ 오천읍 실시간 유가")
st.sidebar.markdown("<div class='premium-card'>GS칼텍스: 1,615원<br>S-OIL: 1,598원</div>", unsafe_allow_html=True)
