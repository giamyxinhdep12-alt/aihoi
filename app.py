import streamlit as st
import random
import time

st.set_page_config(
    page_title="Trường Đua Vịt",
    page_icon="🦆",
    layout="centered"
)

st.title("🦆 TRƯỜNG ĐUA VỊT")
st.write("Nhập tên học sinh rồi xem những chú vịt tranh tài! 🏁")

# Nhập danh sách học sinh
text = st.text_area(
    "👨‍🎓 Danh sách học sinh",
    "An\nBình\nChi\nDũng\nHà\nMinh\nNam\nVy"
)

names = [name.strip() for name in text.split("\n") if name.strip()]

if len(names) < 2:
    st.warning("⚠️ Cần ít nhất 2 học sinh!")
    st.stop()

names = names[:20]

if st.button("🏁 BẮT ĐẦU ĐUA!", use_container_width=True):

    positions = {name: 0 for name in names}
    finished = []

    race = st.empty()
    result = st.empty()

    # Đếm ngược
    race.markdown("# 3️⃣")
    time.sleep(0.7)

    race.markdown("# 2️⃣")
    time.sleep(0.7)

    race.markdown("# 1️⃣")
    time.sleep(0.7)

    race.markdown("# 🏁 CHẠY!!!")
    time.sleep(0.5)

    # Cuộc đua
    while len(finished) < len(names):

        for name in names:

            if name in finished:
                continue

            positions[name] += random.randint(1, 6)

            if positions[name] >= 100:
                positions[name] = 100
                finished.append(name)

        # Hiển thị đường đua
        output = ""

        for name in names:

            pos = positions[name]

            track_length = 30
            duck_position = int(pos / 100 * track_length)
            duck_position = min(duck_position, track_length - 1)

            track = (
                "·" * duck_position
                + "🦆"
                + "·" * (track_length - duck_position - 1)
            )

            output += f"**{name}**\n\n"
            output += f"`{track}🏁`\n\n"

        race.markdown(output)

        time.sleep(0.12)

    # Kết quả
    result.success("🏆 CUỘC ĐUA KẾT THÚC!")

    st.subheader("🏆 KẾT QUẢ")

    medals = ["🥇", "🥈", "🥉"]

    for i, name in enumerate(finished):

        if i < 3:
            st.markdown(f"## {medals[i]} {name}")
        else:
            st.write(f"**{i + 1}.** {name}")

    st.balloons()
