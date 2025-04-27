import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Streamlit 페이지 설정
st.set_page_config(
    page_title="로또 번호 생성기",
    page_icon="🎲",
    layout="wide"
)

# matplotlib 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 번호별 당첨횟수 데이터 (동행복권 공식 통계 2025.04 기준)
lotto_stats = {
    1:191, 2:180, 3:188, 4:187, 5:170, 6:188, 7:189, 8:171, 9:149, 10:182,
    11:182, 12:197, 13:195, 14:186, 15:181, 16:182, 17:191, 18:186, 19:181, 20:190,
    21:182, 22:155, 23:156, 24:184, 25:162, 26:188, 27:196, 28:168, 29:160, 30:179,
    31:184, 32:171, 33:195, 34:202, 35:182, 36:179, 37:187, 38:188, 39:181, 40:185,
    41:158, 42:169, 43:193, 44:179, 45:185
}
df_stats = pd.DataFrame(list(lotto_stats.items()), columns=["번호", "당첨횟수"]).sort_values("번호")

st.title("로또 번호 자동 생성기 및 당첨번호 통계")

tab1, tab2 = st.tabs(["로또 번호 생성", "지난 당첨번호 통계"])

with tab1:
    # 기존 로또 번호 생성 코드
    import random
    if st.button("로또 번호 생성"):
        lotto_numbers = random.sample(range(1, 46), 6)
        lotto_numbers.sort()
        st.write("생성된 로또 번호:", lotto_numbers)

with tab2:
    st.header("번호별 당첨 횟수 (공식 통계)")
    st.dataframe(df_stats.style.highlight_max(axis=0), use_container_width=True)

    st.header("번호별 당첨횟수 시각화")
    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(df_stats["번호"], df_stats["당첨횟수"], color='skyblue')
    ax.set_xlabel("번호")
    ax.set_ylabel("당첨횟수")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.header("최근 10회 당첨번호")
    # 최근 10회 당첨번호 예시 데이터 (직접 갱신 필요)
    recent_wins = [
        [14,23,25,27,29,42], [6,7,27,29,38,45], [17,18,23,25,38,39],
        [2,13,15,16,33,43], [20,21,22,25,28,29], [2,12,20,24,34,42],
        [7,13,18,36,39,45], [3,9,27,28,38,39], [21,25,27,32,37,38], [5,7,12,20,25,26]
    ]
    df_recent = pd.DataFrame(recent_wins, columns=[f"번호{i}" for i in range(1,7)])
    st.dataframe(df_recent.style.highlight_max(axis=1), use_container_width=True)

    st.info("전체 통계는 동행복권 공식 홈페이지에서 확인할 수 있습니다.")