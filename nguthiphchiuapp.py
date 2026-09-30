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

    # =========================
    # ĐẾM NGƯỢC
    # =========================

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

    # =========================
    # TẠO TỐC ĐỘ NGẪU NHIÊN
    # =========================

    speeds = []

    for i in range(len(names)):
        speeds.append(
            round(random.uniform(0.8, 2.2), 2)
        )

    # =========================
    # TẠO CÁC LÀN ĐUA
    # =========================

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

    lanes = ""

    for i, name in enumerate(names):

        safe_name = html.escape(name)

        lanes += f"""
        <div class="lane"
             style="background:{colors[i % len(colors)]};">

            <div class="name">
                {i + 1}. {safe_name}
            </div>

            <div class="road">

                <div
                    class="duck"
                    id="duck{i}"
                    style="left:0%;">
                    🦆
                </div>

                <div class="finish">
                    🏁
                </div>

            </div>

        </div>
        """

    # =========================
    # HTML + JAVASCRIPT
    # =========================

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
        padding:8px;
        font-family:Arial,sans-serif;
    }}

    .race {{
        background:#36a852;
        padding:12px;
        border-radius:25px;
        border:6px solid white;
        box-shadow:0 10px 25px rgba(0,0,0,.2);
    }}

    .lane {{
        height:58px;
        margin-bottom:5px;
        border-radius:15px;
        position:relative;
        overflow:hidden;
        border:2px solid white;
    }}

    .name {{
        position:absolute;
        left:8px;
        top:17px;
        width:105px;
        color:white;
        font-weight:900;
        font-size:13px;
        z-index:10;
        text-shadow:2px 2px 3px #555;
    }}

    .road {{
        position:absolute;
        left:115px;
        right:40px;
        top:5px;
        bottom:5px;
        border-radius:12px;
        border:2px solid white;

        background:
        repeating-linear-gradient(
            90deg,
            #eeeeee 0px,
            #eeeeee 25px,
            #cccccc 25px,
            #cccccc 50px
        );
    }}

    .duck {{
        position:absolute;
        top:1px;
        font-size:38px;
        z-index:5;
        transition:none;
    }}

    .finish {{
        position:absolute;
        right:-2px;
        top:-2px;
        bottom:-2px;
        width:36px;

        background:
        repeating-conic-gradient(
            #111 0deg 90deg,
            white 90deg 180deg
        );

        background-size:18px 18px;

        z-index:8;

        display:flex;
        align-items:center;
        justify-content:center;

        font-size:22px;
    }}

    </style>

    </head>

    <body>

    <div class="race">

        {lanes}

    </div>


    <script>

    const speeds = {speeds};

    const ducks = [];

    for (let i = 0; i < {len(names)}; i++) {{

        ducks.push({{
            element: document.getElementById("duck" + i),
            position: 0,
            speed: speeds[i]
        }});

    }}


    function race() {{

        let stillRunning = false;

        ducks.forEach((duck) => {{

            if (duck.position < 93) {{

                stillRunning = true;

                // tốc độ chính
                duck.position += duck.speed * 0.15;

                // đôi lúc tăng tốc
                if (Math.random() < 0.01) {{
                    duck.position += Math.random() * 1.5;
                }}

                if (duck.position > 93) {{
                    duck.position = 93;
                }}

                duck.element.style.left =
                    duck.position + "%";
            }}

        }});


        if (stillRunning) {{
            requestAnimationFrame(race);
        }}

    }}


    // BẮT ĐẦU CHẠY
    requestAnimationFrame(race);

    </script>

    </body>

    </html>
    """

    # =========================
    # HIỂN THỊ SÂN
    # =========================

    components.html(
        race_html,
        height=(
            35 + len(names) * 65
        ),
        scrolling=False
    )
