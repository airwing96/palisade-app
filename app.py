import streamlit as st
import pandas as pd

# --- 1. 앱 설정 및 고급 스타일 ---
st.set_page_config(page_title="APEX POHANG", page_icon="🏔️", layout="wide")

# 세션 상태 초기화 (페이지 이동 및 게시판 저장용)
if 'page' not in st.session_state: st.session_state.page = 'HOME'
if 'posts' not in st.session_state: st.session_state.posts = []

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { border-radius: 10px; font-weight: 600; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #eee; margin-bottom: 15px; }
    .brand-title { font-size: 2.5rem; font-weight: 800; color: #0f172a; text-align: center; letter-spacing: -1px; }
    .info-label { color: #3b82f6; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 데이터 정의 (세차법, 용품, 맛집) ---
detailing_methods = {
    "중성 세차": "산성/알칼리 없이 도장면 오염물만 안전하게 제거하는 가장 기초적인 세차 방식",
    "2PH 세차": "알칼리(프리워시) -> 중성(카샴푸) 2단계로 나누어 오염물 제거 효율을 극대화",
    "3PH 세차": "알칼리 -> 산성 -> 중성 순서로 진행. 미네랄과 찌든 때를 완벽히 제거하는 매니아 공법",
    "유막제거/발수": "산화세륨으로 유리막 오염 제거 후 불소계 코팅제로 빗길 시야 확보",
    "휠/타이어": "철분제거제로 분진 제거 후 타이어 전용 광택제로 갈변 방지 및 광택",
    "외장 왁스": "고체 왁스 또는 물왁스(LSP)를 이용한 광택 및 비딩(Beading) 형성",
    "실내/시트": "가죽 전용 클리너로 유분 제거 후 컨디셔너로 갈라짐 방지 및 보습"
}

brands = {
    "라보코스메티카": "이탈리아 하이엔드, 3PH 세차 공법의 선두주자 (프리머스, 퓨리피카)",
    "코흐케미": "독일 프리미엄, 완성차 브랜드 납품용 고성능 케미컬 (Gsf, Mw)",
    "기온쿼츠": "세련된 패키징과 강력한 성능의 발수 코팅 라인업 (웨트코트, 아이언)",
    "더클래스/파이어볼": "국산 디테일링의 자존심, 극강의 가성비와 슬릭감 제공"
}

# --- 3. 공통 네비게이션 함수 ---
def set_page(name): st.session_state.page = name

# --- 4. 메인 헤더 ---
st.markdown("<div class='brand-title'>APEX POHANG</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray; margin-bottom:30px;'>오천 버블스타 크루 전용 스마트 라운지</p>", unsafe_allow_html=True)

# --- 5. 페이지별 콘텐츠 ---

# [HOME] 날씨 및 실시간 유가
if st.session_state.page == 'HOME':
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<div class='card'><h3>⛽ 실시간 오천읍 유가 정보</h3>"
                    "<p><b>휘발유:</b> 1,625원 (-) | <b>경유:</b> 1,510원 (↓) | <b>고급유:</b> 1,890원 (-)</p>"
                    "<small>오천읍 인근 주유소 평균가 기준</small></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><h3>🌥️ 포항 남구 기상 현황</h3>"
                    "<p>현재 풍속: <b>3.2m/s</b> (세차 적합) | 강수확률: 10%</p></div>", unsafe_allow_html=True)
    with col2:
        st.button("🔍 희석 비율 계산기", on_click=set_page, args=('CALC',))
        st.button("🧼 디테일링 가이드", on_click=set_page, args=('GUIDE',))
        st.button("🍔 주변 맛집/카페", on_click=set_page, args=('FOOD',))

# [CALC] 케미컬 희석 계산기
elif st.session_state.page == 'CALC':
    st.subheader("🧪 케미컬 희석 비율 계산기")
    total_vol = st.number_input("만들고 싶은 총 용량 (ml)", value=1000)
    ratio = st.number_input("희석 비율 (1 : N 에서 N값 입력)", value=10)
    chemical = total_vol / (ratio + 1)
    water = total_vol - chemical
    st.success(f"결과: **원액 {chemical:.1f}ml** + **물 {water:.1f}ml** 를 섞으세요.")
    if st.button("홈으로"): set_page('HOME')

# [GUIDE] 세차 방법 및 용품
elif st.session_state.page == 'GUIDE':
    st.subheader("📚 디테일링 백과사전")
    tab1, tab2 = st.tabs(["세차 공법", "브랜드 추천"])
    with tab1:
        for m, d in detailing_methods.items():
            st.markdown(f"**{m}**: {d}")
    with tab2:
        for b, d in brands.items():
            st.markdown(f"**[{b}]** {d}")
    if st.button("홈으로"): set_page('HOME')

# [FOOD] 주변 맛집
elif st.session_state.page == 'FOOD':
    st.subheader("🍴 문덕/오천 맛집 리스트")
    st.markdown("- **커피:** 문덕 인더그레이 (드라이브 코스 추천)\n- **맛집:** 오천 해병대 맛집 뚝배기 주물럭\n- **디저트:** 미사동커피 문덕점")
    if st.button("홈으로"): set_page('HOME')

# [COMMUNITY] 자유게시판 및 평가
elif st.session_state.page == 'COMMUNITY':
    st.subheader("💬 멤버 자유게시판 & 세차 후기")
    with st.form("post_form"):
        name = st.text_input("닉네임")
        content = st.text_area("내용 (세차 결과 공유 등)")
        rating = st.select_slider("오늘의 세차 만족도", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
        if st.form_submit_button("등록"):
            st.session_state.posts.append({"name": name, "content": content, "rating": rating, "date": datetime.now().strftime("%m/%d %H:%M")})
    
    for p in reversed(st.session_state.posts):
        st.markdown(f"<div class='card'><b>{p['name']}</b> ({p['date']})<br>{p['rating']}<br>{p['content']}</div>", unsafe_allow_html=True)
    if st.button("홈으로"): set_page('HOME')

# --- 6. 하단 고정 네비게이션 ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
n1, n2, n3, n4, n5 = st.columns(5)
with n1: st.button("🏠\nHOME", on_click=set_page, args=('HOME',))
with n2: st.button("🧼\nLAB", on_click=set_page, args=('GUIDE',))
with n3: st.button("🧪\nCALC", on_click=set_page, args=('CALC',))
with n4: st.button("💬\nTALK", on_click=set_page, args=('COMMUNITY',))
with n5: st.button("📍\nMAP", help="세차장 지도 보기")
