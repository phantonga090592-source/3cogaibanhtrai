import streamlit as st
import random

st.set_page_config(page_title="Bí Ẩn Lịch Sử VN", layout="centered")

# Khởi tạo trạng thái
if "screen" not in st.session_state:
    st.session_state.screen = "home"
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Bộ câu hỏi mẫu
questions = [
    {
        "q": "Ai là vị vua đầu tiên của nhà Nguyễn?",
        "options": ["Gia Long", "Minh Mạng", "Thiệu Trị", "Tự Đức"],
        "answer": "Gia Long"
    },
    {
        "q": "Chiến thắng Bạch Đằng diễn ra năm nào?",
        "options": ["938", "1288", "1427", "1789"],
        "answer": "938"
    }
]

# Màn hình Home
if st.session_state.screen == "home":
    st.markdown("<h1 style='text-align:center;color:gold;'>Bí Ẩn Lịch Sử Việt Nam</h1>", unsafe_allow_html=True)
    if st.button("🎮 BẮT ĐẦU CHƠI"):
        st.session_state.screen = "quiz"
        st.experimental_rerun()

# Màn hình Quiz
elif st.session_state.screen == "quiz":
    q = questions[st.session_state.question_index]
    st.subheader(f"Câu hỏi {st.session_state.question_index+1}/{len(questions)}")
    st.write(q["q"])
    for opt in q["options"]:
        if st.button(opt):
            if opt == q["answer"]:
                st.success("✅ Chính xác!")
                st.session_state.score += 1
            else:
                st.error("❌ Sai rồi!")
            st.session_state.question_index += 1
            if st.session_state.question_index >= len(questions):
                st.session_state.screen = "result"
            st.experimental_rerun()

# Màn hình Kết quả
elif st.session_state.screen == "result":
    st.markdown(f"<h2 style='color:gold;'>Điểm số của bạn: {st.session_state.score}/{len(questions)}</h2>", unsafe_allow_html=True)
    if st.button("🔄 Chơi lại"):
        st.session_state.screen = "home"
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.experimental_rerun()
