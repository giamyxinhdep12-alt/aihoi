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
    import streamlit.components.v1 as components
    import html
    import random

    # Đếm ngược
    for x in ["3️⃣", "2️⃣", "1️⃣", "🦆💨 CHẠY!"]:
        st.markdown(
            f"<h1 style='text-align:center'>{x}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.7)

    # Tạo các làn đua
    lanes = ""

    lane_colors = [
        "#FFE5EC",
        "#E0F7FF",
        "#E8FFD9",
        "#FFF4CC",
        "#EDE0FF",
        "#FFE4CC"
    ]

    for i, name in enumerate(names):
        lanes += f"""
        <div class="lane" style="background:{lane_colors[i % len(lane_colors)]};">
            <div class="name">🦆 {html.escape(name)}</div>
            <div class="road">
                <div class="duck" id="duck{i}">🦆</div>
                <div class="finish">🏁</div>
            </div>
        </div>
        """

    speeds = [
        round(random.uniform(0.8, 2.2), 2)
        for _ in names
    ]

    race_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            overflow-x: hidden;
        }}

        .lane {{
            height: 60px;
            margin: 7px 0;
            border-radius: 15px;
            display: flex;
            align-items: center;
            padding: 5px;
        }}

        .name {{
            width: 120px;
            font-weight: bold;
            font-size: 16px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        .road {{
            position: relative;
            flex: 1;
            height: 48px;
            background: repeating-linear-gradient(
                90deg,
                #eeeeee 0px,
                #eeeeee 30px,
                #ffffff 30px,
                #ffffff 60px
            );
            border: 2px solid #555;
            border-radius: 10px;
            overflow: hidden;
        }}

        .duck {{
            position: absolute;
            left: 0%;
            top: 4px;
            font-size: 32px;
        }}

        .finish {{
            position: absolute;
            right: 5px;
            top: 5px;
            font-size: 30px;
        }}

        /* ===== BẢNG KẾT QUẢ ===== */

        #result {{
            display: none;
            margin-top: 25px;
            padding: 20px;
            border-radius: 20px;
            background: linear-gradient(135deg, #fff8c7, #ffffff);
            border: 3px solid #ffd43b;
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }}

        #result h2 {{
            text-align: center;
            font-size: 28px;
            margin: 5px 0 15px;
        }}

        .rank {{
            background: white;
            padding: 12px;
            margin: 8px 0;
            border-radius: 14px;
            font-size: 19px;
            font-weight: bold;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }}

        .rank.first {{
            font-size: 23px;
            background: #fff1a8;
        }}

        /* ===== BONG BÓNG ===== */

        .bubble {{
            position: fixed;
            bottom: -60px;
            font-size: 30px;
            z-index: 9999;
            animation: baylen 3s linear forwards;
            pointer-events: none;
        }}

        @keyframes baylen {{
            0% {{
                transform: translateY(0) rotate(0deg);
                opacity: 1;
            }}

            100% {{
                transform: translateY(-700px) rotate(360deg);
                opacity: 0;
            }}
        }}
    </style>
    </head>

    <body>

    {lanes}

    <!-- KẾT QUẢ -->
    <div id="result">
        <h2>🏆 KẾT QUẢ CUỘC ĐUA 🏆</h2>
        <div id="ranking"></div>
    </div>

    <script>

        const speeds = {speeds};
        const names = {names};

        const ducks = [];
        const finishOrder = [];

        for (let i = 0; i < {len(names)}; i++) {{
            ducks.push({{
                element: document.getElementById("duck" + i),
                position: 0,
                speed: speeds[i],
                finished: false
            }});
        }}

        function race() {{

            let stillRunning = false;

            ducks.forEach((duck, index) => {{

                if (!duck.finished) {{

                    stillRunning = true;

                    duck.position += duck.speed * 0.15;

                    // Thỉnh thoảng tăng tốc
                    if (Math.random() < 0.01) {{
                        duck.position += Math.random() * 1.5;
                    }}

                    // Vịt cán đích
                    if (duck.position >= 93) {{

                        duck.position = 93;
                        duck.finished = true;

                        // Lưu thứ tự về đích
                        finishOrder.push(index);
                    }}

                    duck.element.style.left =
                        duck.position + "%";
                }}
            }});

            if (stillRunning) {{

                requestAnimationFrame(race);

            }} else {{

                // Tất cả đã về đích
                showResult();
            }}
        }}


        // =========================
        // CÔNG BỐ KẾT QUẢ
        // =========================

        function showResult() {{

            setTimeout(() => {{

                const result =
                    document.getElementById("result");

                const ranking =
                    document.getElementById("ranking");

                result.style.display = "block";

                const medals = [
                    "🥇",
                    "🥈",
                    "🥉"
                ];

                finishOrder.forEach((duckIndex, position) => {{

                    const div =
                        document.createElement("div");

                    div.className = "rank";

                    if (position === 0) {{
                        div.classList.add("first");
                    }}

                    const medal =
                        position < 3
                        ? medals[position]
                        : "🏅";

                    div.innerHTML =
                        medal +
                        " Hạng " +
                        (position + 1) +
                        " — 🦆 " +
                        names[duckIndex];

                    ranking.appendChild(div);
                }});

                // =========================
                // BONG BÓNG ĂN MỪNG 🎈
                // =========================

                for (let i = 0; i < 35; i++) {{

                    setTimeout(() => {{

                        const bubble =
                            document.createElement("div");

                        bubble.className = "bubble";

                        const items = [
                            "🎈",
                            "🎈",
                            "🫧",
                            "🎉",
                            "✨"
                        ];

                        bubble.innerHTML =
                            items[
                                Math.floor(
                                    Math.random() * items.length
                                )
                            ];

                        bubble.style.left =
                            Math.random() * 100 + "%";

                        bubble.style.animationDuration =
                            (2 + Math.random() * 2) + "s";

                        document.body.appendChild(bubble);

                        setTimeout(() => {{
                            bubble.remove();
                        }}, 4500);

                    }}, i * 100);
                }}

            }}, 700);
        }}


        // Bắt đầu đua
        requestAnimationFrame(race);

    </script>

    </body>
    </html>
    """

    components.html(
        race_html,
        height=120 + len(names) * 65 + 450,
        scrolling=False
    )
