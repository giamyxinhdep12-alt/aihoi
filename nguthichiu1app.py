import streamlit as st
import random
import time

# =========================
# CẤU HÌNH
# =========================

st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffd6e8, transparent 25%),
        radial-gradient(circle at 90% 10%, #cde7ff, transparent 25%),
        radial-gradient(circle at 50% 90%, #fff1b8, transparent 30%),
        linear-gradient(135deg, #f8f9ff, #e8f7ff);
}

.title {
    text-align: center;
    font-size: 58px;
    font-weight: 900;

    background: linear-gradient(
        90deg,
        #ff006e,
        #8338ec,
        #3a86ff,
        #06d6a0,
        #ffbe0b,
        #fb5607
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 25px;
}

.input-box {
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.race {
    background: #55b95f;
    border: 8px solid #ffffff;
    border-radius: 30px;
    padding: 15px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    overflow: hidden;
}

.lane {
    height: 65px;
    position: relative;

    background:
        repeating-linear-gradient(
            90deg,
            rgba(255,255,255,0.12) 0px,
            rgba(255,255,255,0.12) 40px,
            rgba(0,0,0,0.08) 40px,
            rgba(0,0,0,0.08) 80px
        );

    border-bottom: 3px dashed rgba(255,255,255,0.8);
}

.lane:last-child {
    border-bottom: none;
}

.name {
    position: absolute;
    left: 8px;
    top: 18px;
    width: 100px;

    font-weight: 900;
    font-size: 15px;

    color: white;

    z-index: 5;

    text-shadow:
        2px 2px 2px rgba(0,0,0,0.5);
}

.duck {
    position: absolute;
    top: 10px;

    font-size: 42px;

    transition: left 0.1s linear;

    filter:
        drop-shadow(3px 4px 2px rgba(0,0,0,0.3));
}

.finish {
    position: absolute;
    right: 0;
    top: 0;

    width: 45px;
    height: 100%;

    background:
        repeating-conic-gradient(
            #111 0% 25%,
            white 0% 50%
        )
        50% / 20px 20px;

    border-left: 5px solid white;
}

.start-line {
    position: absolute;
    left: 105px;
    top: 0;

    height: 100%;
    width: 4px;

    background: white;
}

.winner {
    margin-top: 25px;

    text-align: center;

    font-size: 38px;
    font-weight: 900;

    padding: 25px;

    border-radius: 25px;

    background:
        linear-gradient(
            90deg,
            #ffe66d,
            #ff9f1c,
            #ff6b6b
        );

    box-shadow:
        0 10px 30px rgba(255,120,0,0.3);
}

.podium {
    text-align: center;

    background: white;

    border-radius: 25px;

    padding: 25px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.12);
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
    '<div class="subtitle">🌈 Tất cả vịt cùng tranh tài trên một đường đua! 🌈</div>',
    unsafe_allow_html=True
)


# =========================
# NHẬP TÊN
# =========================

st.markdown("### 👨‍🎓 DANH SÁCH NGƯỜI CHƠI")

text = st.text_area(
    "Mỗi dòng một tên:",
    "An\nBình\nChi\nDũng\nHà\nMinh\nNam\nVy",
    height=160
)

names = []

for name in text.split("\n"):

    name = name.strip()

    if name and name not in names:
        names.append(name)

names = names[:20]

if len(names) < 2:

    st.warning(
        "⚠️ Cần ít nhất 2 người chơi!"
    )

    st.stop()

st.info(
    f"👥 Có **{len(names)}** người tham gia"
)


# =========================
# NÚT BẮT ĐẦU
# =========================

start = st.button(
    "🚀 🏁 BẮT ĐẦU ĐUA! 🏁 🚀",
    use_container_width=True
)


# =========================
# CUỘC ĐUA
# =========================

if start:

    positions = {
        name: 0
        for name in names
    }

    finished = []

    race = st.empty()


    # =====================
    # ĐẾM NGƯỢC
    # =====================

    for number in ["3️⃣", "2️⃣", "1️⃣"]:

        race.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:90px;
                font-weight:900;
                color:#ff006e;
            ">
                {number}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.7)


    race.markdown(
        """
        <div style="
            text-align:center;
            font-size:65px;
            font-weight:900;
            color:#06d6a0;
        ">
            🦆💨 CHẠY!!! 💨🦆
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.5)


    # =====================
    # CHẠY
    # =====================

    while len(finished) < len(names):

        for name in names:

            if name in finished:
                continue

            speed = random.randint(1, 6)

            # Có cơ hội tăng tốc
            if random.random() < 0.08:
                speed += random.randint(4, 10)

            positions[name] += speed

            if positions[name] >= 100:

                positions[name] = 100

                finished.append(name)


        # =================
        # VẼ SÂN ĐUA CHUNG
        # =================

        html = """
        <div class="race">
        """

        for i, name in enumerate(names):

            pos = positions[name]

            # Vị trí vịt
            left = 110 + (pos * 0.82)

            left = min(
                left,
                91
            )

            # Màu vịt
            ducks = [
                "🦆",
                "🐥",
                "🐤",
                "🦆",
                "🐥"
            ]

            duck = ducks[
                i % len(ducks)
            ]

            html += f"""

            <div class="lane">

                <div class="name">
                    {i + 1}. {name}
                </div>

                <div class="start-line"></div>

                <div
                    class="duck"
                    style="left:{left}%"
                >
                    {duck}
                </div>

                <div class="finish"></div>

            </div>

            """

        html += "</div>"

        race.markdown(
            html,
            unsafe_allow_html=True
        )

        time.sleep(0.09)


    # =====================
    # KẾT QUẢ
    # =====================

    st.markdown(
        """
        <div class="winner">
            🎉🏆 CUỘC ĐUA KẾT THÚC! 🏆🎉
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "## 🏆 KẾT QUẢ"
    )

    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]

    cols = st.columns(3)

    for i in range(
        min(3, len(finished))
    ):

        with cols[i]:

            st.markdown(
                f"""
                <div class="podium">

                    <div style="
                        font-size:65px;
                    ">
                        {medals[i]}
                    </div>

                    <div style="
                        font-size:25px;
                        font-weight:900;
                    ">
                        {finished[i]}
                    </div>

                    <div style="
                        color:#777;
                    ">
                        Hạng {i + 1}
                    </div>

                </div>import streamlit as st
import random
import time

# =========================
# CẤU HÌNH
# =========================

st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffd6e8, transparent 25%),
        radial-gradient(circle at 90% 10%, #cde7ff, transparent 25%),
        radial-gradient(circle at 50% 90%, #fff1b8, transparent 30%),
        linear-gradient(135deg, #f8f9ff, #e8f7ff);
}

.title {
    text-align: center;
    font-size: 58px;
    font-weight: 900;

    background: linear-gradient(
        90deg,
        #ff006e,
        #8338ec,
        #3a86ff,
        #06d6a0,
        #ffbe0b,
        #fb5607
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 25px;
}

.input-box {
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.race {
    background: #55b95f;
    border: 8px solid #ffffff;
    border-radius: 30px;
    padding: 15px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    overflow: hidden;
}

.lane {
    height: 65px;
    position: relative;

    background:
        repeating-linear-gradient(
            90deg,
            rgba(255,255,255,0.12) 0px,
            rgba(255,255,255,0.12) 40px,
            rgba(0,0,0,0.08) 40px,
            rgba(0,0,0,0.08) 80px
        );

    border-bottom: 3px dashed rgba(255,255,255,0.8);
}

.lane:last-child {
    border-bottom: none;
}

.name {
    position: absolute;
    left: 8px;
    top: 18px;
    width: 100px;

    font-weight: 900;
    font-size: 15px;

    color: white;

    z-index: 5;

    text-shadow:
        2px 2px 2px rgba(0,0,0,0.5);
}

.duck {
    position: absolute;
    top: 10px;

    font-size: 42px;

    transition: left 0.1s linear;

    filter:
        drop-shadow(3px 4px 2px rgba(0,0,0,0.3));
}

.finish {
    position: absolute;
    right: 0;
    top: 0;

    width: 45px;
    height: 100%;

    background:
        repeating-conic-gradient(
            #111 0% 25%,
            white 0% 50%
        )
        50% / 20px 20px;

    border-left: 5px solid white;
}

.start-line {
    position: absolute;
    left: 105px;
    top: 0;

    height: 100%;
    width: 4px;

    background: white;
}

.winner {
    margin-top: 25px;

    text-align: center;

    font-size: 38px;
    font-weight: 900;

    padding: 25px;

    border-radius: 25px;

    background:
        linear-gradient(
            90deg,
            #ffe66d,
            #ff9f1c,
            #ff6b6b
        );

    box-shadow:
        0 10px 30px rgba(255,120,0,0.3);
}

.podium {
    text-align: center;

    background: white;

    border-radius: 25px;

    padding: 25px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.12);
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
    '<div class="subtitle">🌈 Tất cả vịt cùng tranh tài trên một đường đua! 🌈</div>',
    unsafe_allow_html=True
)


# =========================
# NHẬP TÊN
# =========================

st.markdown("### 👨‍🎓 DANH SÁCH NGƯỜI CHƠI")

text = st.text_area(
    "Mỗi dòng một tên:",
    "An\nBình\nChi\nDũng\nHà\nMinh\nNam\nVy",
    height=160
)

names = []

for name in text.split("\n"):

    name = name.strip()

    if name and name not in names:
        names.append(name)

names = names[:20]

if len(names) < 2:

    st.warning(
        "⚠️ Cần ít nhất 2 người chơi!"
    )

    st.stop()

st.info(
    f"👥 Có **{len(names)}** người tham gia"
)


# =========================
# NÚT BẮT ĐẦU
# =========================

start = st.button(
    "🚀 🏁 BẮT ĐẦU ĐUA! 🏁 🚀",
    use_container_width=True
)


# =========================
# CUỘC ĐUA
# =========================

if start:

    positions = {
        name: 0
        for name in names
    }

    finished = []

    race = st.empty()


    # =====================
    # ĐẾM NGƯỢC
    # =====================

    for number in ["3️⃣", "2️⃣", "1️⃣"]:

        race.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:90px;
                font-weight:900;
                color:#ff006e;
            ">
                {number}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.7)


    race.markdown(
        """
        <div style="
            text-align:center;
            font-size:65px;
            font-weight:900;
            color:#06d6a0;
        ">
            🦆💨 CHẠY!!! 💨🦆
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.5)


    # =====================
    # CHẠY
    # =====================

    while len(finished) < len(names):

        for name in names:

            if name in finished:
                continue

            speed = random.randint(1, 6)

            # Có cơ hội tăng tốc
            if random.random() < 0.08:
                speed += random.randint(4, 10)

            positions[name] += speed

            if positions[name] >= 100:

                positions[name] = 100

                finished.append(name)


        # =================
        # VẼ SÂN ĐUA CHUNG
        # =================

        html = """
        <div class="race">
        """

        for i, name in enumerate(names):

            pos = positions[name]

            # Vị trí vịt
            left = 110 + (pos * 0.82)

            left = min(
                left,
                91
            )

            # Màu vịt
            ducks = [
                "🦆",
                "🐥",
                "🐤",
                "🦆",
                "🐥"
            ]

            duck = ducks[
                i % len(ducks)
            ]

            html += f"""

            <div class="lane">

                <div class="name">
                    {i + 1}. {name}
                </div>

                <div class="start-line"></div>

                <div
                    class="duck"
                    style="left:{left}%"
                >
                    {duck}
                </div>

                <div class="finish"></div>

            </div>

            """

        html += "</div>"

        race.markdown(
            html,
            unsafe_allow_html=True
        )

        time.sleep(0.09)


    # =====================
    # KẾT QUẢ
    # =====================

    st.markdown(
        """
        <div class="winner">
            🎉🏆 CUỘC ĐUA KẾT THÚC! 🏆🎉
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "## 🏆 KẾT QUẢ"
    )

    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]

    cols = st.columns(3)

    for i in range(
        min(3, len(finished))
    ):

        with cols[i]:

            st.markdown(
                f"""
                <div class="podium">

                    <div style="
                        font-size:65px;
                    ">
                        {medals[i]}
                    </div>

                    <div style="
                        font-size:25px;
                        font-weight:900;
                    ">
                        {finished[i]}
                    </div>

                    <div style="
                        color:#777;
                    ">
                        Hạng {i + 1}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    # =====================
    # CÁC HẠNG CÒN LẠI
    # =====================

    if len(finished) > 3:

        st.markdown(
            "### 📋 Những người về sau"
        )

        for i in range(
            3,
            len(finished)
        ):

            st.write(
                f"**{i + 1}.** 🦆 {finished[i]}"
            )


    st.success(
        f"🎉 Chúc mừng **{finished[0]}** đã về đích đầu tiên!"
    )

    st.balloons()
                """,
                unsafe_allow_html=True
            )


    # =====================
    # CÁC HẠNG CÒN LẠI
    # =====================

    if len(finished) > 3:

        st.markdown(
            "### 📋 Những người về sau"
        )

        for i in range(
            3,
            len(finished)
        ):

            st.write(
                f"**{i + 1}.** 🦆 {finished[i]}"
            )


    st.success(
        f"🎉 Chúc mừng **{finished[0]}** đã về đích đầu tiên!"
    )

    st.balloons()
