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
        }

        .game-container {
            width: 100%;
            max-width: 1000px;
            height: 650px;
            background: linear-gradient(135deg, rgba(44, 26, 14, 0.95), rgba(20, 10, 4, 0.98));
            border: 4px solid var(--gold-dark);
            box-shadow: 0 0 30px rgba(245, 207, 109, 0.2), inset 0 0 15px rgba(0, 0, 0, 0.8);
            border-radius: 16px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* Top Bar & Navigation */
        .top-bar {
            height: 60px;
            background: rgba(15, 7, 2, 0.85);
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
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.5);
        }

        .icon-btn:hover {
            transform: scale(1.1) rotate(5deg);
            background: var(--gold-primary);
            color: var(--wood-dark);
        }

        /* Screen Management */
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

        /* Screen 1: Bìa Game (Home Screen) */
        #screen-home {
            justify-content: center;
            align-items: center;
            text-align: center;
            background: radial-gradient(circle, rgba(139,38,8,0.2) 0%, rgba(26,15,7,0.8) 100%),
                        url('https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1200&q=80') center/cover no-blend;
            background-blend-mode: overlay;
        }

        .title-container {
            margin-bottom: 30px;
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
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
            margin-bottom: 5px;
            text-transform: uppercase;
        }

        .sub-title {
            font-family: 'Merriweather', serif;
            font-size: 1.3rem;
            color: #dcdcdc;
            letter-spacing: 1px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        }

        .btn-play-big {
            font-family: 'Playfair Display', serif;
            padding: 16px 50px;
            font-size: 1.6rem;
            font-weight: 800;
            color: #fff;
            background: linear-gradient(180deg, #d32f2f, #8b2608);
            border: 3px solid var(--gold-primary);
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(211, 47, 47, 0.6), 0 5px 0 #4a1103;
            transition: all 0.2s;
            position: relative;
            overflow: hidden;
            margin-top: 20px;
        }

        .btn-play-big:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 0 30px rgba(245, 207, 109, 0.8), 0 8px 0 #4a1103;
            background: linear-gradient(180deg, #e53935, #a02a0a);
        }

        .btn-play-big:active {
            transform: translateY(2px) scale(0.98);
            box-shadow: 0 0 10px rgba(211, 47, 47, 0.4), 0 2px 0 #4a1103;
        }

        /* Screen 2: Chọn Màn (Level Selection) */
        .section-header {
            text-align: center;
            margin-bottom: 25px;
        }

        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: var(--gold-primary);
        }

        .levels-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            max-width: 900px;
            margin: 0 auto;
            width: 100%;
        }

        .level-card {
            background: linear-gradient(145deg, rgba(58, 35, 19, 0.9), rgba(30, 18, 9, 0.9));
            border: 2px solid var(--gold-dark);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 180px;
        }

        .level-card:hover:not(.locked) {
            transform: translateY(-5px);
            border-color: var(--gold-primary);
            box-shadow: 0 10px 20px rgba(245, 207, 109, 0.2);
            background: linear-gradient(145deg, rgba(74, 45, 24, 0.95), rgba(40, 24, 12, 0.95));
        }

        .level-card.locked {
            opacity: 0.5;
            cursor: not-allowed;
            filter: grayscale(0.8);
        }

        .level-number {
            font-size: 0.85rem;
            color: var(--gold-light);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .level-name {
            font-family: 'Merriweather', serif;
            font-size: 1.1rem;
            color: #fff;
            font-weight: 700;
            margin: 8px 0;
        }

        .level-stars {
            color: var(--gold-primary);
            font-size: 1.2rem;
            margin-top: 5px;
        }

        .lock-icon {
            position: absolute;
            top: 15px;
            right: 15px;
            color: #aaa;
        }

        /* Screen 3: Màn Chơi Quiz */
        .quiz-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(15, 7, 2, 0.6);
            padding: 10px 20px;
            border-radius: 8px;
            border: 1px solid var(--gold-dark);
            margin-bottom: 15px;
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
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: rgba(211, 47, 47, 0.2);
            border: 2px solid var(--red-bright);
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
        }

        .quiz-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .question-card {
            background: var(--parchment);
            color: var(--text-dark);
            padding: 20px;
            border-radius: 10px;
            border: 3px solid var(--gold-dark);
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            position: relative;
        }

        .question-text {
            font-family: 'Merriweather', serif;
            font-size: 1.15rem;
            line-height: 1.5;
            font-weight: 700;
        }

        .options-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .option-btn {
            background: linear-gradient(180deg, #3a2313, #22140a);
            border: 2px solid var(--gold-dark);
            color: #fff;
            padding: 14px 18px;
            border-radius: 8px;
            font-size: 1rem;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .option-btn:hover {
            border-color: var(--gold-primary);
            background: linear-gradient(180deg, #4a2d18, #2c1a0e);
        }

        .option-prefix {
            background: var(--gold-dark);
            color: var(--wood-dark);
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 0.9rem;
            flex-shrink: 0;
        }

        .option-btn.correct {
            background: linear-gradient(180deg, #2e7d32, #1b5e20) !important;
            border-color: #81c784 !important;
            color: #fff !important;
        }

        .option-btn.wrong {
            background: linear-gradient(180deg, #c62828, #8e0000) !important;
            border-color: #ef9a9a !important;
            color: #fff !important;
        }

        /* Help Buttons */
        .lifelines {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }

        .lifeline-btn {
            background: rgba(20, 10, 4, 0.8);
            border: 1px solid var(--gold-primary);
            color: var(--gold-primary);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .lifeline-btn:hover:not(.used) {
            background: var(--gold-primary);
            color: var(--wood-dark);
        }

        .lifeline-btn.used {
            opacity: 0.4;
            cursor: not-allowed;
            border-color: #666;
            color: #aaa;
        }

        /* Explanation Popover */
        .explanation-box {
            background: rgba(26, 15, 7, 0.95);
            border: 2px solid var(--gold-primary);
            padding: 12px 18px;
            border-radius: 8px;
            font-size: 0.95rem;
            color: var(--parchment);
            margin-top: 10px;
            display: none;
            line-height: 1.4;
        }

        /* Modal Overlay & Dialogs */
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
            backdrop-filter: blur(4px);
        }

        .modal-card {
            background: linear-gradient(135deg, #2c1a0e, #1a0f07);
            border: 3px solid var(--gold-primary);
            border-radius: 12px;
            width: 450px;
            padding: 25px;
            box-shadow: 0 0 25px rgba(0,0,0,0.9);
            position: relative;
        }

        .modal-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            color: var(--gold-primary);
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 1px solid var(--gold-dark);
            padding-bottom: 10px;
        }

        .setting-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
            font-size: 1.05rem;
        }

        .toggle-switch {
            width: 50px;
            height: 26px;
            background: #444;
            border-radius: 13px;
            position: relative;
            cursor: pointer;
            transition: 0.3s;
        }

        .toggle-switch.active {
            background: #2e7d32;
        }

        .toggle-switch::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
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
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
            float: right;
            margin-top: 10px;
            font-weight: bold;
        }

        /* Movie Credits Screen */
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
            font-size: 2.5rem;
            color: var(--gold-primary);
            margin-bottom: 30px;
        }

        .credits-section {
            margin-bottom: 35px;
        }

        .credits-role {
            font-size: 0.95rem;
            color: var(--gold-light);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 6px;
        }

        .credits-name {
            font-family: 'Merriweather', serif;
            font-size: 1.5rem;
            color: #fff;
            font-weight: 700;
        }

        .btn-back-menu {
            position: absolute;
            bottom: 20px;
            z-index: 10;
            background: linear-gradient(180deg, #3a2313, #1a0f07);
            border: 2px solid var(--gold-primary);
            color: var(--gold-primary);
            padding: 10px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
        }

        .btn-back-menu:hover {
            background: var(--gold-primary);
            color: var(--wood-dark);
        }
    </style>
</head>
<body>

    <div class="game-container">
        <!-- Top Navigation -->
        <div class="top-bar">
            <div class="game-logo-sm">
                <i class="fa-solid fa-landmark"></i> Bí Ấn Lịch Sử VN
            </div>
            <div class="nav-buttons">
                <button class="icon-btn" id="btn-home" title="Trang chủ"><i class="fa-solid fa-house"></i></button>
                <button class="icon-btn" id="btn-credits" title="Ban phát triển"><i class="fa-solid fa-users"></i></button>
                <button class="icon-btn" id="btn-settings" title="Cài đặt"><i class="fa-solid fa-gear"></i></button>
            </div>
        </div>

        <!-- Screen 1: Home/Cover -->
        <div class="screen active" id="screen-home">
            <div class="title-container">
                <h1 class="main-title">Bí Ấn Lịch Sử</h1>
                <p class="sub-title">VIỆT NAM</p>
            </div>
            <button class="btn-play-big" id="btn-start-game">
                <i class="fa-solid fa-play" style="margin-right: 10px;"></i> BẮT ĐẦU CHƠI
            </button>
        </div>

        <!-- Screen 2: Level Selection -->
        <div class="screen" id="screen-levels">
            <div class="section-header">
                <h2 class="section-title">CHỌN MÀN CHƠI</h2>
                <p style="color: #bbb; font-size: 0.95rem;">Hoàn thành các màn chơi để mở khóa giai đoạn lịch sử tiếp theo</p>
            </div>
            <div class="levels-grid" id="levels-grid">
                <!-- Dynamically generated levels -->
            </div>
        </div>

        <!-- Screen 3: Quiz Gameplay -->
        <div class="screen" id="screen-quiz">
            <div class="quiz-header">
                <div>
                    <span id="quiz-level-title" style="color: var(--gold-primary); font-weight: bold;">Màn 1: Cổ Đại</span>
                    <span id="quiz-progress" style="margin-left: 15px; color: #ccc;">Câu 1/15</span>
                </div>
                <div class="timer-box">
                    <i class="fa-regular fa-clock"></i>
                    <div class="timer-circle" id="timer-display">20</div>
                </div>
                <div>
                    <span style="color: var(--gold-light);">Điểm: <strong id="quiz-score"
