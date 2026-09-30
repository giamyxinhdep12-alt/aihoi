import streamlit as st
import random
import time
import base64
import urllib.request

# =========================================================
# CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="wide"
)

# =========================================================
# ẢNH VỊT
# =========================================================

DUCK_URL = (
    "https://opengameart.org/sites/default/files/"
    "fowl_animal_ducky.zip"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(
            180deg,
            #dff7ff 0%,
            #ffffff 45%,
            #eaffea 100%
        );
}

.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 900;
    color: #ff5c8a;
    margin-top: 10px;
    margin-bottom: 0;
}

.sub-title {
    text-align: center;
    font-size: 21px;
    color: #555;
    margin-bottom: 25px;
}

/* Khung sân */

.race-box {
    background: #38a852;
    border: 8px solid white;
    border-radius: 28px;
    padding: 15px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.20);
}

/* Một làn */

.lane {
    position: relative;
    height: 72px;
    margin-bottom: 8px;
    border-radius: 18px;
    overflow: hidden;
    border: 3px solid rgba(255,255,255,0.85);
}

/* Màu các làn */

.lane1 {
    background: #ff8fab;
}

.lane2 {
    background: #74b9ff;
}

.lane3 {
    background: #ffe066;
}

.lane4 {
    background: #7bed9f;
}

.lane5 {
    background: #a29bfe;
}

.lane6 {
    background: #ffb86c;
}

.lane7 {
    background: #81ecec;
}

.lane8 {
    background: #fab1a0;
}

.lane9 {
    background: #55efc4;
}

.lane10 {
    background: #fd79a8;
}

/* Tên */

.player-name {
    position: absolute;
    left: 12px;
    top: 20px;
    width: 105px;
    z-index: 5;

    font-size: 15px;
    font-weight: 900;
    color: white;

    text-shadow:
        2px 2px 3px rgba(0,0,0,0.55);
}

/* Đường chạy */

.road {
    position: absolute;
    left: 120px;
    right: 45px;
    top: 8px;
    bottom: 8px;

    background:
        repeating-linear-gradient(
            90deg,
            #eeeeee 0px,
            #eeeeee 28px,
            #d4d4d4 28px,
            #d4d4d4 56px
        );

    border-radius: 14px;
    border: 3px solid white;
}

/* Vịt */

.duck {
    position: absolute;
    top: 5px;
    font-size: 42px;
    z-index: 4;

    transform: translateX(-50%);
}

/* Vạch đích */

.finish {
    position: absolute;
    right: -3px;
    top: -3px;
    bottom: -3px;
    width: 38px;

    background:
        repeating-conic-gradient(
            #111 0deg 90deg,
            white 90deg 180deg
        );

    background-size: 19px 19px;

    border-left: 4px solid white;
    z-index: 3;
}

/* Đếm ngược */

.countdown {
    text-align: center;
    font-size: 85px;
    font-weight: 900;
    color: #ff4d6d;
}

/* Kết quả */

.result-box {
    background: white;
    border-radius: 25px;
    padding: 22px;
    margin-top: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="main-title">🦆 TRƯỜNG ĐUA VỊT 🏁</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    '🌈 Nhập tên và xem ai là chú vịt về đích đầu tiên! 🌈'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# NHẬP TÊN
# =========================================================

st.subheader("👨‍🎓 Danh sách người chơi")

text = st.text_area(
    "Mỗi dòng nhập một tên:",
    "An\nBình\nChi\nDũng\nHà\nMinh\nNam\nVy",
    height=170
)

names = []

for line in text.splitlines():

    name = line.strip()

    if name and name not in names:
        names.append(name)

# Tối đa 10 người
names = names[:10]

if len(names) < 2:

    st.warning(
        "⚠️ Hãy nhập ít nhất 2 người chơi!"
    )

    st.stop()


st.info(
    f"👥 Có **{len(names)} người** tham gia cuộc đua."
)


# =========================================================
# NÚT BẮT ĐẦU
# =========================================================

start = st.button(
    "🚀🏁 BẮT ĐẦU CUỘC ĐUA! 🏁🚀",
    use_container_width=True
)


# =========================================================
# CUỘC ĐUA
# =========================================================

if start:

    # -----------------------------------------
    # Đếm ngược
    # -----------------------------------------

    countdown = st.empty()

    for number in ["3", "2", "1"]:

        countdown.markdown(
            f"""
            <div class="countdown">
                {number}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.7)

    countdown.markdown(
        """
        <div class="countdown">
            🦆💨 GO!!!
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.6)

    countdown.empty()


    # -----------------------------------------
    # Vị trí
    # -----------------------------------------

    positions = {}

    for name in names:
        positions[name] = 0


    finished = []


    # -----------------------------------------
    # Khung hiển thị sân
    # -----------------------------------------

    board = st.empty()


    # =====================================================
    # CHẠY
    # =====================================================

    while len(finished) < len(names):

        # -----------------------------
        # Cho vịt chạy
        # -----------------------------

        for name in names:

            if name in finished:
                continue

            # tốc độ bình thường
            positions[name] += random.randint(1, 4)

            # đôi lúc tăng tốc
            if random.random() < 0.10:

                positions[name] += random.randint(
                    3,
                    8
                )

            # về đích
            if positions[name] >= 100:

                positions[name] = 100

                finished.append(name)


        # -----------------------------
        # Tạo sân
        # -----------------------------

        html = """
        <div class="race-box">
        """


        for i, name in enumerate(names):

            # vị trí %
            position = positions[name]

            # giới hạn vị trí
            position = max(
                0,
                min(position, 100)
            )

            # chuyển % thành vị trí trên đường
            left = 120 + (
                position * 0.78
            )

            # màu làn
            lane_number = (i % 10) + 1

            html += f"""
            <div class="lane lane{lane_number}">

                <div class="player-name">
                    {i + 1}. {name}
                </div>

                <div class="road">

                    <div
                        class="duck"
                        style="left:{position}%"
                    >
                        🦆
                    </div>

                    <div class="finish"></div>

                </div>

            </div>
            """


        html += """
        </div>
        """


        # -----------------------------
        # Hiển thị
        # -----------------------------

        board.markdown(
            html,
            unsafe_allow_html=True
        )

        time.sleep(0.08)


    # =====================================================
    # KẾT THÚC
    # =====================================================

    time.sleep(0.5)

    winner = finished[0]

    st.markdown(
        f"""
        <div class="result-box">

            <div style="
                font-size:65px;
            ">
                🏆
            </div>

            <div style="
                font-size:32px;
                font-weight:900;
                color:#ff4d6d;
            ">
                {winner}
            </div>

            <div style="
                font-size:20px;
            ">
                🎉 ĐÃ VỀ ĐÍCH ĐẦU TIÊN! 🎉
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # TOP 3
    # =====================================================

    st.subheader("🏆 BẢNG XẾP HẠNG")

    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]

    for rank, name in enumerate(finished):

        if rank < 3:

            st.markdown(
                f"""
                <div class="result-box">

                    <span style="
                        font-size:42px;
                    ">
                        {medals[rank]}
                    </span>

                    <span style="
                        font-size:25px;
                        font-weight:900;
                    ">
                        {name}
                    </span>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.write(
                f"**{rank + 1}.** 🦆 {name}"
            )


    st.balloons()
