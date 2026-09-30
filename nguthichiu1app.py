import streamlit as st
import random
import time

st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="wide"
)

# ===== CSS =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8f9ff, #e8f7ff);
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: 900;
    color: #ff4d6d;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
}

.race {
    background: #58b957;
    border: 8px solid white;
    border-radius: 25px;
    padding: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.lane {
    height: 65px;
    position: relative;
    border-bottom: 3px dashed white;
}

.lane:last-child {
    border-bottom: none;
}

.name {
    position: absolute;
    left: 5px;
    top: 20px;
    width: 105px;
    color: white;
    font-weight: bold;
    font-size: 15px;
    z-index: 5;
    text-shadow: 2px 2px 3px #555;
}

.duck {
    position: absolute;
    top: 8px;
    font-size: 40px;
    transition: left 0.1s linear;
}

.finish {
    position: absolute;
    right: 0;
    top: 0;
    width: 42px;
    height: 100%;
    background:
        repeating-conic-gradient(
            #111 0% 25%,
            white 0% 50%
        ) 50% / 18px 18px;
}

.start-line {
    position: absolute;
    left: 110px;
    top: 0;
    height: 100%;
    border-left: 4px solid white;
}

.winner {
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    padding: 20px;
    margin: 20px 0;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        #ffe66d,
        #ff9f1c,
        #ff6b6b
    );
}

.podium {
    text-align: center;
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)


# ===== TIÊU ĐỀ =====

st.markdown(
    '<div class="title">🦆 TRƯỜNG ĐUA VỊT 🏁</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🌈 Tất cả vịt cùng đua trên một sân! 🌈</div>',
    unsafe_allow_html=True
)


# ===== NHẬP TÊN =====

st.subheader("👨‍🎓 Danh sách người chơi")

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
    st.warning("⚠️ Cần ít nhất 2 người chơi!")
    st.stop()

st.info(f"👥 Có {len(names)} người tham gia")


# ===== NÚT BẮT ĐẦU =====

start = st.button(
    "🚀 🏁 BẮT ĐẦU ĐUA! 🏁 🚀",
    use_container_width=True
)


# ===== CUỘC ĐUA =====

if start:

    positions = {name: 0 for name in names}
    finished = []

    race = st.empty()

    # Đếm ngược
    for number in ["3️⃣", "2️⃣", "1️⃣"]:

        race.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:90px;
                font-weight:bold;
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
            font-weight:bold;
            color:#06d6a0;
        ">
            🦆💨 CHẠY!!!
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.5)


    # ===== CHẠY =====

    while len(finished) < len(names):

        for name in names:

            if name in finished:
                continue

            speed = random.randint(1, 6)

            if random.random() < 0.08:
                speed += random.randint(4, 10)

            positions[name] += speed

            if positions[name] >= 100:
                positions[name] = 100
                finished.append(name)


        # ===== VẼ SÂN ĐUA =====

        html = '<div class="race">'

        ducks = ["🦆", "🐥", "🐤", "🦆", "🐥"]

        for i, name in enumerate(names):

            pos = positions[name]

            left = 110 + (pos * 0.82)
            left = min(left, 91)

            duck = ducks[i % len(ducks)]

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

        race.markdown(html, unsafe_allow_html=True)

        time.sleep(0.09)


    # ===== KẾT QUẢ =====

    st.markdown(
        """
        <div class="winner">
            🎉🏆 CUỘC ĐUA KẾT THÚC! 🏆🎉
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🏆 KẾT QUẢ")

    medals = ["🥇", "🥈", "🥉"]

    cols = st.columns(3)

    for i in range(min(3, len(finished))):

        with cols[i]:

            st.markdown(
                f"""
                <div class="podium">

                    <div style="font-size:60px;">
                        {medals[i]}
                    </div>

                    <div style="
                        font-size:24px;
                        font-weight:bold;
                    ">
                        {finished[i]}
                    </div>

                    <div>
                        Hạng {i + 1}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    if len(finished) > 3:

        st.subheader("📋 Các vị trí còn lại")

        for i in range(3, len(finished)):
            st.write(
                f"**{i + 1}.** 🦆 {finished[i]}"
            )

    st.success(
        f"🎉 Chúc mừng **{finished[0]}** đã về đích đầu tiên!"
    )

    st.balloons()
