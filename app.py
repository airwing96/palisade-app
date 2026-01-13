import streamlit as st
import requests
from datetime import datetime

# --- 1. 앱 설정 및 프리미엄 스타일 ---
st.set_page_config(page_title="APEX | Pohang Premium", page_icon="🏔️", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'HOME'

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Lexend:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background-color: #f8f9fa; }
    
    /* APEX 브랜딩 */
    .brand-title { font-family: 'Lexend', sans-serif; font-size: 3rem; font-weight: 700; color: #0f172a; text-align: center; margin-bottom: 0px; }
    .brand-subtitle { font-size: 0.8rem; color: #64748b; letter-spacing: 4px; text-align: center; margin-bottom: 30px; text-transform: uppercase; }

    /* 카드 및 알람 디자인 */
    .card { background-color: white; padding: 25px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #f1f5f9; margin-bottom: 20px; }
    .weather-widget { background: linear-gradient(135deg, #0f172a 0%, #334155 100%); color: white; padding: 25px; border-radius: 20px; margin-bottom: 25px; }
    
    /* 버튼 스타일 */
    .stButton>button { border-radius: 12px; height: 50px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 실시간 날씨 데이터 (포항시 남구 오천읍 기준) ---
def get_pohang_weather():
    # 실제 운영시 OpenWeatherMap 등의 API를 연결하는 부분입니다.
    # 현재는 요청하신 알람 로직 테스트를 위한 가상 실시간 데이터입니다.
    return {
        "temp": 5.2,
        "condition": "Clear", # 테스트 시 "Rain", "Snow"로 변경해 보세요
        "wind_speed": 7.5,    # 6.0m/s 이상으로 설정 (알람 테스트용)
        "humidity": 45,
        "location": "경북 포항시 남구 오천읍"
    }

weather = get_pohang_weather()

# --- 3. 세차 지수 및 알람 로직 ---
def weather_alarm():
    if weather["condition"] in ["Rain", "Snow"]:
        st.error(f"⚠️ **세차 중단 알림**: 현재 오천읍에 {weather['condition']}(비/눈) 예보가 있습니다. 세차를 권장하지 않습니다!")
    elif weather["wind_speed"] >= 6.0:
        st.warning(f"🚩 **강풍 주의보**: 현재 풍속 {weather['wind_speed']}m/s입니다. 문덕로 일대 강풍으로 인해 물때 및 약재 건조가 빠를 수 있으니 주의하세요!")
    else:
        st.success("☀️ **세차 최적기**: 현재 오천읍 기상 상태가 매우 쾌적합니다. 버블스타로 출발하세요!")

# --- 4. 페이지 전환 함수 ---
def set_page(page_name):
    st.session_state.page = page_name

# --- 5. 헤더 섹션 ---
st.markdown("<div style='padding-top: 20px;'>", unsafe_allow_html=True)
st.markdown("<div class='brand-title'>APEX</div>", unsafe_allow_html=True)
st.markdown("<div class='brand-subtitle'>Pohang Luxury Mobility</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 6. 페이지별 콘텐츠 ---

# [HOME 페이지]
if st.session_state.page == 'HOME':
    # 날씨 알람 상단 배치
    weather_alarm()
    
    # 오천읍 날씨 위젯
    st.markdown(f"""
    <div class="weather-widget">
        <p style='font-size: 0.9rem; opacity: 0.8;'>{weather['location']} 실시간 기상</p>
        <h1 style='font-size: 3.5rem; margin: 10px 0;'>{weather['temp']}°C</h1>
        <p style='font-size: 1.1rem;'>{weather['condition']} | 풍속 {weather['wind_speed']}m/s | 습도 {weather['humidity']}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>LAB</h3><p>오천 버블스타 세차장 정보</p></div>', unsafe_allow_html=True)
        if st.button("세차장 정보 및 지도 보기"): set_page('LAB')
    with col2:
        st.markdown('<div class="card"><h3>ROAD</h3><p>포항 해안도로 드라이브 세션</p></div>', unsafe_allow_html=True)
        if st.button("드라이브 세션 참여"): set_page('ROAD')

# [LAB 페이지] - 세차장 정보 집중
elif st.session_state.page == 'LAB':
    st.subheader("🧪 APEX LAB : 거점 세차장")
    
    st.markdown(f"""
    <div class="card">
        <h2 style='color:#0f172a; margin-bottom:5px;'>오천 버블스타 세차장</h2>
        <p style='color:#64748b; font-size:1rem; margin-bottom:20px;'>경북 포항시 남구 오천읍 문덕로79번길 26</p>
        <div style='background-color:#f1f5f9; padding:15px; border-radius:10px; margin-bottom:20px;'>
            <p style='margin:0; font-size:0.9rem;'><b>MEMO:</b> 포항 남구 최대 규모, 폼건 및 하부세차 완비</p>
        </div>
        <a href="https://naver.me/F6lTwCXz" target="_blank" style="text-decoration:none;">
            <div style="background-color:#00c73c; color:white; text-align:center; padding:15px; border-radius:12px; font-weight:bold;">
                N 네이버 지도로 길찾기
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← 홈으로 돌아가기"): set_page('HOME')

# [ROAD 페이지]
elif st.session_state.page == 'ROAD':
    st.subheader("🛣️ ROAD SESSION")
    st.markdown('<div class="card"><h3>포항 호미곶 해안도로 정기 런</h3><p>기상 상황에 따라 일정이 변경될 수 있습니다.</p></div>', unsafe_allow_html=True)
    if st.button("← 홈으로 돌아가기"): set_page('HOME')

# --- 7. 하단 네비게이션 바 ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    if st.button("🏠\nHOME"): set_page('HOME')
with nav2:
    if st.button("🧼\nLAB"): set_page('LAB')
with nav3:
    if st.button("🛣️\nROAD"): set_page('ROAD')
with nav4:
    if st.button("👤\nMY"): set_page('MY')
