import streamlit as st
import streamlit.components.v1 as components

# Cấu hình giao diện Streamlit
st.set_page_config(
    page_title="Bí Ấn Lịch Sử Việt Nam",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Bỏ lề và ẩn khung thừa của Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Mã nguồn Web Game
game_html = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bí Ấn Lịch Sử Việt Nam - Game Giải Đố</title>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,400;0,700;0,900;1,400&family=Playfair+Display:wght@600;700;800;900&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --bg-amber: #1a0f07;
            --gold-primary: #f5cf6d;
            --gold-light: #fff2c2;
            --gold-dark: #b8860b;
            --red-bronze: #8b2608;
            --red-bright: #d32f2f;
            --wood-dark: #2c1a0e;
            --wood-card: #3a2313;
            --parchment: #f4e4bc;
            --parchment-dark: #e2cb93;
            --text-dark: #2b1810;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }

        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--bg-amber);
            color: #fff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-image: 
                radial-gradient(circle at 50% 30%, rgba(139, 38, 8, 0.3) 0%, transparent 70%),
                radial-gradient(circle at 80% 80%, rgba(245, 207, 109, 0.1) 0%, transparent 50%);
            overflow-x: hidden;
            padding: 10px;
        }

        .game-container {
            width: 100%;
            max-width: 980px;
            height: 670px;
            background: linear-gradient(135deg, rgba(44, 26, 14, 0.98), rgba(20, 10, 4, 0.99));
            border: 4px solid var(--gold-dark);
            box-shadow: 0 0 30px rgba(245, 207, 109, 0.2), inset 0 0 15px rgba(0, 0, 0, 0.8);
            border-radius: 16px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* Top Bar */
        .top-bar {
            height: 55px;
            background: rgba(15, 7, 2, 0.9);
            border-bottom: 2px solid var(--gold-dark);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            z-index: 10;
        }

        .game-logo-sm {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            color: var(--gold-primary);
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .nav-buttons {
            display: flex;
            gap: 12px;
        }

        .icon-btn {
            background: linear-gradient(180deg, #4a2d18, #261408);
            border: 1px solid var(--gold-primary);
            color: var(--gold-primary);
            width: 38px;
            height: 38px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .icon-btn:hover {
            transform: scale(1.1);
            background: var(--gold-primary);
            color: var(--wood-dark);
        }

        /* Screens */
        .screen {
            flex: 1;
            display: none;
            flex-direction: column;
            position: relative;
            padding: 20px;
            overflow-y: auto;
        }

        .screen.active {
            display: flex;
        }

        /* Home Screen (Ảnh nền ban đầu chuẩn cổ phong lịch sử) */
        #screen-home {
            justify-content: center;
            align-items: center;
            text-align: center;
            background: radial-gradient(circle, rgba(139,38,8,0.3) 0%, rgba(26,15,7,0.85) 100%),
                        url('https://images.unsplash.com/photo-1599707367072-cd69233a37c6?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
            background-blend-mode: overlay;
        }

        .title-container {
            margin-bottom: 30px;
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        .main-title {
            font-family: 'Playfair Display', serif;
            font-size: 3.2rem;
            font-weight: 900;
            background: linear-gradient(180deg, #fff2c2 0%, #f5cf6d 40%, #b8860b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 5px 15px rgba(0,0,0,0.8);
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .sub-title {
            font-family: 'Merriweather', serif;
            font-size: 1.3rem;
            color: #dcdcdc;
            letter-spacing: 1px;
        }

        .btn-play-big {
            font-family: 'Playfair Display', serif;
            padding: 16px 50px;
            font-size: 1.5rem;
            font-weight: 800;
            color: #fff;
            background: linear-gradient(180deg, #d32f2f, #8b2608);
            border: 3px solid var(--gold-primary);
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(211, 47, 47, 0.6);
            transition: all 0.2s;
            margin-top: 20px;
        }

        .btn-play-big:hover {
            transform: scale(1.05);
            background: linear-gradient(180deg, #e53935, #a02a0a);
        }

        /* Levels Screen */
        .section-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            color: var(--gold-primary);
        }

        .levels-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            max-width: 900px;
            margin: 0 auto;
            width: 100%;
        }

        .level-card {
            background: linear-gradient(145deg, rgba(58, 35, 19, 0.95), rgba(30, 18, 9, 0.95));
            border: 2px solid var(--gold-dark);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 150px;
        }

        .level-card:hover:not(.locked) {
            transform: translateY(-4px);
            border-color: var(--gold-primary);
            box-shadow: 0 8px 18px rgba(245, 207, 109, 0.2);
        }

        .level-card.locked {
            opacity: 0.5;
            cursor: not-allowed;
            filter: grayscale(0.8);
        }

        .level-number {
            font-size: 0.8rem;
            color: var(--gold-light);
            text-transform: uppercase;
        }

        .level-name {
            font-family: 'Merriweather', serif;
            font-size: 0.95rem;
            color: #fff;
            font-weight: 700;
            margin: 5px 0;
        }

        .level-stars {
            color: var(--gold-primary);
            font-size: 1.1rem;
        }

        .lock-icon {
            position: absolute;
            top: 12px;
            right: 12px;
            color: #aaa;
        }

        /* Quiz Gameplay */
        .quiz-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(15, 7, 2, 0.6);
            padding: 10px 20px;
            border-radius: 8px;
            border: 1px solid var(--gold-dark);
            margin-bottom: 12px;
        }

        .timer-box {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--gold-primary);
        }

        .timer-circle {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(211, 47, 47, 0.2);
            border: 2px solid var(--red-bright);
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            font-size: 0.95rem;
        }

        .quiz-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .question-card {
            background: var(--parchment);
            color: var(--text-dark);
            padding: 16px 20px;
            border-radius: 10px;
            border: 3px solid var(--gold-dark);
        }

        .question-text {
            font-family: 'Merriweather', serif;
            font-size: 1.1rem;
            line-height: 1.4;
            font-weight: 700;
        }

        .options-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }

        .option-btn {
            background: linear-gradient(180deg, #3a2313, #22140a);
            border: 2px solid var(--gold-dark);
            color: #fff;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 0.95rem;
            text-align: left;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.2s;
        }

        .option-btn:hover {
            border-color: var(--gold-primary);
            background: linear-gradient(180deg, #4a2d18, #2c1a0e);
        }

        .option-prefix {
            background: var(--gold-dark);
            color: var(--wood-dark);
            width: 26px;
            height: 26px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 0.85rem;
            flex-shrink: 0;
        }

        .option-btn.correct {
            background: linear-gradient(180deg, #2e7d32, #1b5e20) !important;
            border-color: #81c784 !important;
        }

        .option-btn.wrong {
            background: linear-gradient(180deg, #c62828, #8e0000) !important;
            border-color: #ef9a9a !important;
        }

        .lifelines {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-top: 5px;
        }

        .lifeline-btn {
            background: rgba(20, 10, 4, 0.8);
            border: 1px solid var(--gold-primary);
            color: var(--gold-primary);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .lifeline-btn.used {
            opacity: 0.4;
            cursor: not-allowed;
        }

        .explanation-box {
            background: rgba(26, 15, 7, 0.95);
            border: 2px solid var(--gold-primary);
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 0.9rem;
            color: var(--parchment);
            margin-top: 5px;
            display: none;
        }

        /* Modal Settings */
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 100;
        }

        .modal-card {
            background: linear-gradient(135deg, #2c1a0e, #1a0f07);
            border: 3px solid var(--gold-primary);
            border-radius: 12px;
            width: 420px;
            padding: 25px;
        }

        .modal-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            color: var(--gold-primary);
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 1px solid var(--gold-dark);
            padding-bottom: 8px;
        }

        .setting-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .toggle-switch {
            width: 48px;
            height: 24px;
            background: #444;
            border-radius: 12px;
            position: relative;
            cursor: pointer;
        }

        .toggle-switch.active {
            background: #2e7d32;
        }

        .toggle-switch::after {
            content: '';
            position: absolute;
            width: 18px;
            height: 18px;
            background: #fff;
            border-radius: 50%;
            top: 3px;
            left: 3px;
            transition: 0.3s;
        }

        .toggle-switch.active::after {
            left: 27px;
        }

        .close-btn {
            background: var(--red-bright);
            color: #fff;
            border: none;
            padding: 8px 18px;
            border-radius: 6px;
            cursor: pointer;
            float: right;
            margin-top: 10px;
            font-weight: bold;
        }

        /* Credits Screen */
        .credits-container {
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            overflow: hidden;
            position: relative;
        }

        .credits-scroll {
            position: absolute;
            width: 100%;
            text-align: center;
            animation: scrollCredits 25s linear infinite;
        }

        @keyframes scrollCredits {
            0% { top: 100%; }
            100% { top: -120%; }
        }

        .credits-title {
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            color:
