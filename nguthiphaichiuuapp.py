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

    lane_colors = [
        "#FFE5EC",
        "#E0F7FF",
        "#E8FFD9",
        "#FFF4CC",
        "#EDE0FF",
        "#FFE4CC"
    ]

    lanes = ""

    for i, name in enumerate(names):
        lanes += f"""
        <div class="lane" id="lane{i}"
             style="background:{lane_colors[i % len(lane_colors)]};">
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

        * {{
            box-sizing: border-box;
        }}

        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }}

        body {{
            background: white;
        }}

        /* =========================
           CÁC MÀN HÌNH
        ========================= */

        .screen {{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            display: none;
            overflow: hidden;
        }}

        .screen.active {{
            display: flex;
        }}

        /* =========================
           ĐẾM NGƯỢC
        ========================= */

        #countScreen {{
            align-items: center;
            justify-content: center;
        }}

        #count {{
            font-size: 100px;
            font-weight: bold;
            animation: pop 0.7s ease;
        }}

        @keyframes pop {{
            0% {{
                transform: scale(0.3);
                opacity: 0;
            }}

            60% {{
                transform: scale(1.2);
                opacity: 1;
            }}

            100% {{
                transform: scale(1);
            }}
        }}

        /* =========================
           TRƯỜNG ĐUA
        ========================= */

        #raceScreen {{
            flex-direction: column;
            padding: 10px;
        }}

        .title {{
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 8px;
        }}

        .lane {{
            height: 55px;
            margin: 5px 0;
            border-radius: 14px;
            display: flex;
            align-items: center;
            padding: 5px;
        }}

        .name {{
            width: 120px;
            font-weight: bold;
            font-size: 15px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        .road {{
            position: relative;
            flex: 1;
            height: 43px;

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
            top: 2px;
            font-size: 31px;
            z-index: 5;
        }}

        .finish {{
            position: absolute;
            right: 4px;
            top: 2px;
            font-size: 29px;
        }}

        /* =========================
           KẾT QUẢ
        ========================= */

        #resultScreen {{
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 15px;
        }}

        #resultBox {{
            width: min(600px, 95%);
            max-height: 90%;
            overflow-y: auto;

            background: linear-gradient(
                135deg,
                #fff8c7,
                #ffffff
            );

            border: 3px solid #ffd43b;
            border-radius: 25px;

            padding: 20px;

            box-shadow:
                0 8px 25px rgba(0,0,0,0.15);

            animation: resultPop 0.7s ease;
        }}

        @keyframes resultPop {{
            from {{
                transform: scale(0.5);
                opacity: 0;
            }}

            to {{
                transform: scale(1);
                opacity: 1;
            }}
        }}

        #resultBox h1 {{
            text-align: center;
            margin: 0 0 15px 0;
            font-size: 29px;
        }}

        .rank {{
            background: white;
            margin: 7px 0;
            padding: 11px;
            border-radius: 13px;

            font-size: 18px;
            font-weight: bold;

            box-shadow:
                0 2px 6px rgba(0,0,0,0.1);
        }}

        .first {{
            background: #fff0a8;
            font-size: 21px;
        }}

        /* =========================
           BONG BÓNG
        ========================= */

        .balloon {{
            position: fixed;
            bottom: -80px;
            font-size: 35px;
            z-index: 999;
            pointer-events: none;

            animation:
                balloonUp 3.5s linear forwards;
        }}

        @keyframes balloonUp {{

            0% {{
                transform:
                    translateY(0)
                    rotate(0deg);

                opacity: 1;
            }}

            100% {{
                transform:
                    translateY(-750px)
                    rotate(360deg);

                opacity: 0;
            }}

        }}

    </style>

    </head>

    <body>

        <!-- =========================
             MÀN HÌNH ĐẾM NGƯỢC
        ========================= -->

        <div id="countScreen" class="screen active">
            <div id="count">3</div>
        </div>


        <!-- =========================
             MÀN HÌNH ĐUA
        ========================= -->

        <div id="raceScreen" class="screen">

            <div class="title">
                🏁 TRƯỜNG ĐUA VỊT 🦆
            </div>

            {lanes}

        </div>


        <!-- =========================
             MÀN HÌNH KẾT QUẢ
        ========================= -->

        <div id="resultScreen" class="screen">

            <div id="resultBox">

                <h1>
                    🏆 KẾT QUẢ CUỘC ĐUA 🏆
                </h1>

                <div id="ranking"></div>

            </div>

        </div>


    <script>

        const names = {names};
        const speeds = {speeds};

        const ducks = [];
        const finishOrder = [];

        for (
            let i = 0;
            i < names.length;
            i++
        ) {{

            ducks.push({{

                element:
                    document.getElementById(
                        "duck" + i
                    ),

                position: 0,

                speed: speeds[i],

                finished: false

            }});

        }}


        /* =========================
           HÀM CHUYỂN MÀN HÌNH
        ========================= */

        function showScreen(id) {{

            document
                .querySelectorAll(".screen")
                .forEach(screen => {{
                    screen.classList.remove("active");
                }});

            document
                .getElementById(id)
                .classList.add("active");
        }}


        /* =========================
           ĐẾM NGƯỢC
        ========================= */

        let number = 3;

        const count =
            document.getElementById("count");

        const countdown =
            setInterval(() => {{

                number--;

                if (number > 0) {{

                    count.innerText = number;

                    // chạy lại hiệu ứng
                    count.style.animation = "none";

                    void count.offsetWidth;

                    count.style.animation =
                        "pop 0.7s ease";

                }}

                else {{

                    clearInterval(countdown);

                    count.innerText =
                        "🦆💨";

                    setTimeout(() => {{

                        showScreen("raceScreen");

                        setTimeout(() => {{
                            race();
                        }}, 100);

                    }}, 500);

                }}

            }}, 1000);


        /* =========================
           CUỘC ĐUA
        ========================= */

        function race() {{

            let stillRunning = false;

            ducks.forEach((duck, index) => {{

                if (!duck.finished) {{

                    stillRunning = true;

                    duck.position +=
                        duck.speed * 0.15;


                    // tăng tốc ngẫu nhiên
                    if (
                        Math.random() < 0.012
                    ) {{

                        duck.position +=
                            Math.random() * 1.5;

                    }}


                    // cán đích
                    if (
                        duck.position >= 93
                    ) {{

                        duck.position = 93;

                        duck.finished = true;

                        finishOrder.push(index);

                    }}


                    duck.element.style.left =
                        duck.position + "%";

                }}

            }});


            if (stillRunning) {{

                requestAnimationFrame(race);

            }}

            else {{

                setTimeout(
                    showResults,
                    700
                );

            }}

        }}


        /* =========================
           HIỆN KẾT QUẢ
        ========================= */

        function showResults() {{

            showScreen("resultScreen");

            const ranking =
                document.getElementById(
                    "ranking"
                );

            ranking.innerHTML = "";

            const medals = [
                "🥇",
                "🥈",
                "🥉"
            ];


            finishOrder.forEach(
                (duckIndex, position) => {{

                    const row =
                        document.createElement(
                            "div"
                        );

                    row.className = "rank";


                    if (position === 0) {{
                        row.classList.add("first");
                    }}


                    const medal =
                        position < 3
                        ? medals[position]
                        : "🏅";


                    row.innerHTML =
                        medal +
                        " Hạng " +
                        (position + 1) +
                        " — 🦆 " +
                        names[duckIndex];


                    ranking.appendChild(row);

                }}
            );


            // bong bóng ăn mừng
            createBalloons();

        }}


        /* =========================
           BONG BÓNG
        ========================= */

        function createBalloons() {{

            const items = [
                "🎈",
                "🎈",
                "🎈",
                "🫧",
                "🎉",
                "✨"
            ];


            for (
                let i = 0;
                i < 40;
                i++
            ) {{

                setTimeout(() => {{

                    const balloon =
                        document.createElement(
                            "div"
                        );

                    balloon.className =
                        "balloon";


                    balloon.innerText =
                        items[
                            Math.floor(
                                Math.random() *
                                items.length
                            )
                        ];


                    balloon.style.left =
                        Math.random() * 100 +
                        "%";


                    balloon.style.animationDuration =
                        (
                            2.5 +
                            Math.random() * 2
                        ) +
                        "s";


                    document.body.appendChild(
                        balloon
                    );


                    setTimeout(() => {{

                        balloon.remove();

                    }}, 5000);

                }}, i * 80);

            }}

        }}

    </script>

    </body>
    </html>
    """

    components.html(
        race_html,
        height=650,
        scrolling=False
    )
