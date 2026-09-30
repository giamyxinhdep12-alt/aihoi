import streamlit as st
import streamlit.components.v1 as components
import random
import time
import html

st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="wide"
)

# =========================
# GIAO DIỆN
# =========================

st.markdown(
    """
    <h1 style="text-align:center; color:#ff4d6d;">
        🦆 TRƯỜNG ĐUA VỊT 🏁
    </h1>
    <p style="text-align:center; font-size:20px;">
        🌈 Ai sẽ là chú vịt về đích đầu tiên? 🌈
    </p>
    """,
    unsafe_allow_html=True
)

# =========================
# NHẬP TÊN
# =========================

text = st.text_area(
    "👨‍🎓 Nhập tên người chơi — mỗi dòng một tên:",
    "An\nBình\nChi\nDũng\nHà\nMinh\nNam\nVy",
    height=160
)

names = []

for line in text.splitlines():
    name = line.strip()

    if name and name not in names:
        names.append(name)

names = names[:12]

if len(names) < 2:
    st.warning("⚠️ Cần ít nhất 2 người chơi!")
    st.stop()

st.info(f"👥 Có {len(names)} người tham gia")

# =========================
# BẮT ĐẦU
# =========================

start = st.button(
    "🚀🏁 BẮT ĐẦU ĐUA! 🏁🚀",
    use_container_width=True
)

if start:

    # -------------------------
    # ĐẾM NGƯỢC
    # -------------------------

    count = st.empty()

    for n in ["3️⃣", "2️⃣", "1️⃣", "🦆💨 CHẠY!"]:

        count.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:65px;
                font-weight:bold;
            ">
                {n}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.7)

    count.empty()

    # -------------------------
    # VỊ TRÍ
    # -------------------------

    positions = [0 for _ in names]
    finished = []

    board = st.empty()

    colors = [
        "#ff6b81",
        "#4dabf7",
        "#ffd43b",
        "#51cf66",
        "#9775fa",
        "#ff922b",
        "#20c997",
        "#f06595",
        "#15aabf",
        "#ae3ec9",
        "#fab005",
        "#339af0"
    ]

    # =========================
    # VÒNG ĐUA
    # =========================

    while len(finished) < len(names):

        for i in range(len(names)):

            if i in finished:
                continue

            positions[i] += random.randint(1, 5)

            # thỉnh thoảng tăng tốc
            if random.random() < 0.08:
                positions[i] += random.randint(4, 9)

            if positions[i] >= 100:
                positions[i] = 100
                finished.append(i)

        # -------------------------
        # TẠO HTML SÂN ĐUA
        # -------------------------

        lanes = ""

        for i, name in enumerate(names):

            safe_name = html.escape(name)

            # vị trí con vịt
            pos = max(0, min(positions[i], 100))

            lanes += f"""
            <div class="lane"
                 style="background:{colors[i % len(colors)]};">

                <div class="name">
                    {i + 1}. {safe_name}
                </div>

                <div class="road">

                    <div
                        class="duck"
                        style="left:{pos}%;">
                        🦆
                    </div>

                    <div class="finish">
                        🏁
                    </div>

                </div>

            </div>
            """

        # -------------------------
        # TOÀN BỘ SÂN
        # -------------------------

        race_html = f"""
        <!DOCTYPE html>
        <html>
        <head>

        <style>

        * {{
            box-sizing:border-box;
        }}

        body {{
            margin:0;
            padding:10px;
            background:transparent;
            font-family:Arial,sans-serif;
        }}

        .race {{
            background:#36a852;
            padding:14px;
            border-radius:28px;
            border:7px solid white;
            box-shadow:0 10px 30px rgba(0,0,0,.2);
        }}

        .lane {{
            height:68px;
            margin-bottom:7px;
            border-radius:17px;
            position:relative;
            overflow:hidden;
            border:3px solid white;
        }}

        .name {{
            position:absolute;
            left:10px;
            top:20px;
            width:105px;
            color:white;
            font-weight:900;
            font-size:14px;
            z-index:10;
            text-shadow:2px 2px 3px rgba(0,0,0,.6);
        }}

        .road {{
            position:absolute;
            left:120px;
            right:45px;
            top:7px;
            bottom:7px;
            border-radius:14px;
            border:3px solid white;

            background:
                repeating-linear-gradient(
                    90deg,
                    #eeeeee 0px,
                    #eeeeee 28px,
                    #d0d0d0 28px,
                    #d0d0d0 56px
                );
        }}

        .duck {{
            position:absolute;
            top:2px;
            transform:translateX(-50%);
            font-size:43px;
            z-index:5;
            white-space:nowrap;
        }}

        .finish {{
            position:absolute;
            right:-3px;
            top:-3px;
            bottom:-3px;
            width:40px;
            background:
                repeating-conic-gradient(
                    #111 0deg 90deg,
                    white 90deg 180deg
                );
            background-size:20px 20px;
            border-left:4px solid white;
            z-index:8;
            font-size:25px;
            display:flex;
            align-items:center;
            justify-content:center;
        }}

        </style>

        </head>

        <body>

            <div class="race">
                {lanes}
            </div>

        </body>
        </html>
        """

        # QUAN TRỌNG:
        # Dùng components.html thay vì st.markdown
        components.html(
            race_html,
            height=(
                30
                + len(names) * 75
            ),
            scrolling=False
        )

        time.sleep(0.08)

    # =========================
    # KẾT QUẢ
    # =========================

    winner = names[finished[0]]

    st.markdown(
        f"""
        <div style="
            text-align:center;
            background:linear-gradient(
                90deg,
                #ffe066,
                #ff922b,
                #ff6b6b
            );
            padding:25px;
            border-radius:25px;
            margin-top:25px;
        ">

            <div style="font-size:65px;">
                🏆
            </div>

            <div style="
                font-size:32px;
                font-weight:900;
            ">
                {html.escape(winner)}
            </div>

            <div style="font-size:21px;">
                🎉 VỀ ĐÍCH ĐẦU TIÊN! 🎉
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # TOP 3
    # =========================

    st.subheader("🏆 KẾT QUẢ")

    medals = ["🥇", "🥈", "🥉"]

    for rank, index in enumerate(finished):

        name = names[index]

        if rank < 3:

            st.markdown(
                f"""
                <div style="
                    background:white;
                    padding:15px;
                    margin:8px 0;
                    border-radius:15px;
                    font-size:24px;
                    text-align:center;
                    box-shadow:0 4px 12px rgba(0,0,0,.12);
                ">
                    {medals[rank]}
                    <b>{html.escape(name)}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.write(
                f"**{rank + 1}.** 🦆 {name}"
            )

    st.balloons()
