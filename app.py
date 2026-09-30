import streamlit as st
import random
import time

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="wide"
)

# =========================
# CSS - GIAO DIỆN
# =========================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #dff6ff, #fff7d6);
    }

    .title {
        text-align: center;
        font-size: 55px;
        font-weight: 900;
        color: #ff7a00;
        margin-bottom: 5px;
        text-shadow: 3px 3px 0px #ffffff;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #555;
        margin-bottom: 30px;
    }

    .race-box {
        background: rgba(255,255,255,0.85);
        border-radius: 20px;
        padding: 18px;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
    }

    .player-name {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-bottom: 5px;
    }

    .track {
        height: 55px;
        border-radius: 30px;
        background: repeating-linear-gradient(
            45deg,
            #eeeeee,
            #eeeeee 10px,
            #ffffff 10px,
            #ffffff 20px
        );
        border: 3px solid #444;
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
    }

    .finish {
        position: absolute;
        right: 5px;
        top: 0;
        height: 100%;
        width: 35px;
        background: repeating-linear-gradient(
            45deg,
            #222,
            #222 7px,
            #fff 7px,
            #fff 14px
        );
    }

    .duck {
        font-size: 34px;
        position: absolute;
        transition: left 0.1s linear;
    }

    .winner {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        color: #ff9800;
        background: #fff3cd;
        padding: 20px;
        border-radius: 20px;
        margin: 20px 0;
    }

    .podium {
        text-align: center;
        background: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
    }
</style>
""", unsafe_allow_html=True)

# =========================
# TIÊU ĐỀ
# =========================
st.markdown(
    '<div class="title">🦆 TRƯỜNG ĐUA VỊT 🏁</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🔥 Ai sẽ là chú vịt nhanh nhất hôm nay?</div>',
    unsafe_allow_html=True
)

# =========================
# NHẬP TÊN
# =========================
st.markdown("### 👨‍🎓 Danh sách người chơi")

text = st.text_area(
    "Mỗi dòng một tên:",
    "An\nBình\nChi\nDũng\nHà\nMinh\nNam\nVy",
    height=180
)

names = []

for name in text.split("\n"):
    name = name.strip()

    if name and name not in names:
        names.append(name)

names = names[:20]

st.info(f"👥 Có **{len(names)}** người tham gia")

# =========================
# KIỂM TRA
# =========================
if len(names) < 2:
    st.warning("⚠️ Cần ít nhất 2 người để bắt đầu cuộc đua!")
    st.stop()

# =========================
# NÚT ĐUA
# =========================
start = st.button(
    "🏁  BẮT ĐẦU CUỘC ĐUA!",
    use_container_width=True
)

# =========================
# CUỘC ĐUA
# =========================
if start:

    positions = {name: 0 for name in names}
    finished = []

    race_area = st.empty()

    # -------------------------
    # ĐẾM NGƯỢC
    # -------------------------
    race_area.markdown(
        """
        <div style="
            text-align:center;
            font-size:80px;
            font-weight:900;
            color:#ff7a00;
        ">
        3
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.7)

    race_area.markdown(
        """
        <div style="
            text-align:center;
            font-size:80px;
            font-weight:900;
            color:#ff7a00;
        ">
        2
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.7)

    race_area.markdown(
        """
        <div style="
            text-align:center;
            font-size:80px;
            font-weight:900;
            color:#ff7a00;
        ">
        1
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.7)

    race_area.markdown(
        """
        <div style="
            text-align:center;
            font-size:65px;
            font-weight:900;
            color:#e91e63;
        ">
        🦆 GO!!!
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.5)

    # -------------------------
    # CHẠY
    # -------------------------
    while len(finished) < len(names):

        for name in names:

            if name in finished:
                continue

            # Tốc độ ngẫu nhiên
            positions[name] += random.randint(1, 7)

            # Có lúc vịt chạy nhanh hơn
            if random.random() < 0.08:
                positions[name] += random.randint(5, 12)

            if positions[name] >= 100:
                positions[name] = 100
                finished.append(name)

        # -------------------------
        # VẼ SÂN ĐUA
        # -------------------------
        html = ""

        for number, name in enumerate(names):

            pos = positions[name]

            # Vị trí con vịt
            duck_left = max(1, min(pos * 0.88, 88))

            html += f"""
            <div class="race-box">

                <div class="player-name">
                    {number + 1}. {name}
                </div>

                <div class="track">

                    <div
                        class="duck"
                        style="left:{duck_left}%"
                    >
                        🦆
                    </div>

                    <div class="finish"></div>

                </div>

            </div>
            """

        race_area.markdown(
            html,
            unsafe_allow_html=True
        )

        time.sleep(0.08)

    # =========================
    # KẾT QUẢ
    # =========================
    st.markdown(
        '<div class="winner">🏆 CUỘC ĐUA KẾT THÚC! 🏆</div>',
        unsafe_allow_html=True
    )

    st.markdown("## 🏆 BẢNG XẾP HẠNG")

    medals = ["🥇", "🥈", "🥉"]

    # TOP 3
    cols = st.columns(3)

    for i in range(min(3, len(finished))):

        with cols[i]:

            st.markdown(
                f"""
                <div class="podium">
                    <div style="font-size:55px;">
                        {medals[i]}
                    </div>

                    <div style="
                        font-size:24px;
                        font-weight:bold;
                    ">
                        {finished[i]}
                    </div>

                    <div style="
                        font-size:16px;
                        color:#777;
                    ">
                        Hạng {i + 1}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Những người còn lại
    if len(finished) > 3:

        st.markdown("### 📋 Những người về sau")

        for i in range(3, len(finished)):

            st.write(
                f"**{i + 1}.** 🦆 {finished[i]}"
            )

    st.balloons()

    st.success(
        f"🎉 Xin chúc mừng **{finished[0]}** đã về đích đầu tiên!"
    )
