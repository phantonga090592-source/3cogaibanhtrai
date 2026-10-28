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
            height: 680px;
            background: linear-gradient(135deg, rgba(44, 26, 14, 0.98), rgba(20, 10, 4, 0.99));
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
            background: radial-gradient(circle, rgba(139,38,8,0.2) 0%, rgba(26,15,7,0.9) 100%),
                        url('https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
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
            height: 155px;
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
            font-size: 0.8rem;
            color: var(--gold-light);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .level-name {
            font-family: 'Merriweather', serif;
            font-size: 0.95rem;
            color: #fff;
            font-weight: 700;
            margin: 5px 0;
            line-height: 1.3;
        }

        .level-stars {
            color: var(--gold-primary);
            font-size: 1.1rem;
            margin-top: 3px;
        }

        .lock-icon {
            position: absolute;
            top: 12px;
            right: 12px;
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
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            position: relative;
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
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 0.9rem;
            color: var(--parchment);
            margin-top: 5px;
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
            font-size: 2.3rem;
            color: var(--gold-primary);
            margin-bottom: 20px;
        }

        .credits-section {
            margin-bottom: 30px;
        }

        .credits-role {
            font-size: 0.9rem;
            color: var(--gold-light);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 5px;
        }

        .credits-name {
            font-family: 'Merriweather', serif;
            font-size: 1.4rem;
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
                <p style="color: #bbb; font-size: 0.9rem;">Hoàn thành các màn chơi để mở khóa giai đoạn lịch sử tiếp theo</p>
            </div>
            <div class="levels-grid" id="levels-grid">
                <!-- Dynamically generated levels -->
            </div>
        </div>

        <!-- Screen 3: Quiz Gameplay -->
        <div class="screen" id="screen-quiz">
            <div class="quiz-header">
                <div>
                    <span id="quiz-level-title" style="color: var(--gold-primary); font-weight: bold; font-size: 0.95rem;">Màn 1: Cổ Đại</span>
                    <span id="quiz-progress" style="margin-left: 12px; color: #ccc; font-size: 0.9rem;">Câu 1/15</span>
                </div>
                <div class="timer-box">
                    <i class="fa-regular fa-clock"></i>
                    <div class="timer-circle" id="timer-display">20</div>
                </div>
                <div>
                    <span style="color: var(--gold-light); font-size: 0.9rem;">Điểm: <strong id="quiz-score" style="color:#fff;">0</strong></span>
                </div>
            </div>

            <div class="quiz-body">
                <div class="question-card">
                    <div class="question-text" id="question-text">Đang tải câu hỏi...</div>
                </div>

                <div class="options-grid" id="options-grid">
                    <!-- Options buttons will be generated here -->
                </div>

                <div class="explanation-box" id="explanation-box">
                    <strong><i class="fa-solid fa-circle-info"></i> Giải thích lịch sử:</strong>
                    <p id="explanation-text" style="margin-top: 4px;"></p>
                </div>

                <div class="lifelines">
                    <button class="lifeline-btn" id="btn-5050"><i class="fa-solid fa-scissors"></i> 50:50</button>
                    <button class="lifeline-btn" id="btn-hint"><i class="fa-regular fa-lightbulb"></i> Gợi ý</button>
                    <button class="lifeline-btn" id="btn-audience"><i class="fa-solid fa-users"></i> Khán giả</button>
                </div>
            </div>
        </div>

        <!-- Screen 4: Credits -->
        <div class="screen" id="screen-credits">
            <div class="credits-container">
                <div class="credits-scroll">
                    <h2 class="credits-title">BÍ ẨN LỊCH SỬ VIỆT NAM</h2>
                    <p style="color: var(--gold-light); margin-bottom: 35px;">Dự án Web Game Lịch Sử Giáo Dục</p>
                    
                    <div class="credits-section">
                        <div class="credits-role">NHẬP CODE, CHẠY GAME</div>
                        <div class="credits-name">Thân Thanh Thy</div>
                    </div>

                    <div class="credits-section">
                        <div class="credits-role">SOẠN CÂU HỎI, Ý TƯỞNG</div>
                        <div class="credits-name">Đinh Ngọc Nữ</div>
                    </div>

                    <div class="credits-section">
                        <div class="credits-role">SOẠN CÂU HỎI, CHỈNH SỬA LỖI</div>
                        <div class="credits-name">Phan Ngọc Bảo Uyên</div>
                    </div>

                    <div class="credits-section" style="margin-top: 40px;">
                        <p style="color: #aaa; font-size: 0.9rem;">Cảm ơn bạn đã tham gia trải nghiệm game!</p>
                    </div>
                </div>
                <button class="btn-back-menu" onclick="showScreen('screen-home')">VỀ TRANG CHỦ</button>
            </div>
        </div>

        <!-- Modal: Settings -->
        <div class="modal-overlay" id="modal-settings">
            <div class="modal-card">
                <h3 class="modal-title"><i class="fa-solid fa-sliders"></i> Cài Đặt Game</h3>
                
                <div class="setting-row">
                    <span>Âm thanh hiệu ứng</span>
                    <div class="toggle-switch active" id="toggle-sfx"></div>
                </div>

                <div class="setting-row">
                    <span>Nhạc nền cổ phong</span>
                    <div class="toggle-switch active" id="toggle-bgm"></div>
                </div>

                <div class="setting-row">
                    <span>Reset tiến trình chơi</span>
                    <button id="btn-reset-data" style="background:#c62828; color:#fff; border:none; padding:6px 12px; border-radius:4px; cursor:pointer;">Xóa dữ liệu</button>
                </div>

                <button class="close-btn" id="btn-close-settings">Đóng</button>
            </div>
        </div>
    </div>

    <script>
        // Data Game: 6 Levels, 15 Questions per level = Total 90 Questions
        const gameData = [
            {
                id: 1,
                title: "Màn 1: Cổ Đại & Bắc Thuộc",
                timePerQuestion: 25,
                questions: [
                    { q: "Quốc hiệu đầu tiên của nước ta thời vua Hùng là gì?", options: ["Đại Việt", "Văn Lang", "Âu Lạc", "Vạn Xuân"], correct: 1, exp: "Văn Lang là quốc hiệu đầu tiên của Việt Nam trong lịch sử, dưới thời các Vua Hùng." },
                    { q: "Thành Cổ Loa do ai xây dựng?", options: ["An Dương Vương", "Vua Hùng", "Lý Nam Đế", "Ngô Quyền"], correct: 0, exp: "An Dương Vương (Thục Phán) cho xây dựng thành Cổ Loa làm kinh đô nước Âu Lạc." },
                    { q: "Hai Bà Trưng phất cờ khởi nghĩa chống quân xâm lược nào?", options: ["Quân Nam Hán", "Quân Đông Hán", "Quân Minh", "Quân Nguyên"], correct: 1, exp: "Năm 40, Hai Bà Trưng phất cờ khởi nghĩa chống lại chính sách cai trị khắc nghiệt của nhà Đông Hán." },
                    { q: "Ai là người xưng Nam Đế và đặt tên nước là Vạn Xuân năm 544?", options: ["Triệu Quang Phục", "Lý Bôn", "Mai Thúc Loan", "Phùng Hưng"], correct: 1, exp: "Lý Bôn (Lý Nam Đế) sau khi đánh đuổi quân Lương đã lên ngôi và đặt tên nước là Vạn Xuân." },
                    { q: "Trận chiến trên sông Bạch Đằng năm 938 do ai lãnh đạo?", options: ["Lý Thường Kiệt", "Trần Hưng Đạo", "Ngô Quyền", "Lê Hoàn"], correct: 2, exp: "Ngô Quyền dùng cọc gỗ bọc sắt cắm xuống sông Bạch Đằng đánh tan quân Nam Hán năm 938." },
                    { q: "Trận Bạch Đằng năm 938 chấm dứt bao nhiêu năm Bắc thuộc?", options: ["500 năm", "800 năm", "Hơn 1000 năm", "1200 năm"], correct: 2, exp: "Chiến thắng Bạch Đằng 938 chấm dứt hơn 1000 năm Bắc thuộc, mở ra thời kỳ độc lập lâu dài." },
                    { q: "Ai được mệnh danh là Dạ Trạch Vương?", options: ["Triệu Quang Phục", "Phùng Hưng", "Khúc Thừa Dụ", "Mai Thúc Loan"], correct: 0, exp: "Triệu Quang Phục chọn vùng đầm lầy Dạ Trạch làm căn cứ kháng chiến nên được gọi là Dạ Trạch Vương." },
                    { q: "Khởi nghĩa Phùng Hưng đánh chiếm thành Bồ Đề, nhân dân tôn ông là gì?", options: ["Bố Cái Đại Vương", "Đại Hành Hoàng Đế", "Bình Định Vương", "Thái Tổ"], correct: 0, exp: "Sau khi mất, Phùng Hưng được nhân dân ghi nhớ công ơn và tôn xưng là Bố Cái Đại Vương." },
                    { q: "Ai là người dựng quyền tự chủ đầu tiên cho Việt Nam vào năm 905?", options: ["Khúc Thừa Dụ", "Ngô Quyền", "Dương Đình Nghệ", "Lý Bôn"], correct: 0, exp: "Khúc Thừa Dụ nhân lúc nhà Đường suy yếu đã nổi dậy tự xưng Tiết độ sứ năm 905." },
                    { q: "Vị vua nào gắn liền với truyền thuyết Nỏ Thần và Mị Châu - Trọng Thủy?", options: ["Vua Hùng thứ 18", "An Dương Vương", "Lý Nam Đế", "Triệu Đà"], correct: 1, exp: "Truyền thuyết Nỏ Thần và chuyện tình Mị Châu - Trọng Thủy gắn liền với thời An Dương Vương." },
                    { q: "Nữ tướng nào cùng Hai Bà Trưng ra trận đánh đuổi Tô Định?", options: ["Lê Chân", "Bùi Thị Xuân", "Nguyễn Thị Định", "Triệu Thị Trinh"], correct: 0, exp: "Nữ tướng Lê Chân là một trong những tướng lĩnh xuất sắc nhất dưới trướng Hai Bà Trưng." },
                    { q: "Bà Triệu (Triệu Thị Trinh) phất cờ khởi nghĩa chống quân xâm lược nào năm 248?", options: ["Nhà Ngô", "Nhà Tấn", "Nhà Lương", "Nhà Hán"], correct: 0, exp: "Bà Triệu khởi nghĩa chống lại sự cai trị tàn bạo của nhà Ngô vào năm 248." },
                    { q: "Thành Cổ Loa có cấu trúc đặc biệt gồm mấy vòng thành?", options: ["2 vòng", "3 vòng", "4 vòng", "5 vòng"], correct: 1, exp: "Thành Cổ Loa gồm 3 vòng xoáy trôn ốc: Thành ngoại, Thành trung và Thành nội." },
                    { q: "Mai Thúc Loan lãnh đạo cuộc khởi nghĩa chống nhà Đường và xưng là gì?", options: ["Mai Đen", "Mai Hắc Đế", "Bố Cái Đại Vương", "Dạ Trạch Vương"], correct: 1, exp: "Mai Thúc Loan giải phóng vùng đất Hoan Châu và lên ngôi xưng là Mai Hắc Đế." },
                    { q: "Ai là người lãnh đạo đánh đuổi quân Kiều Công Tiễn và quân Nam Hán?", options: ["Ngô Quyền", "Đinh Bộ Lĩnh", "Lê Hoàn", "Trần Hưng Đạo"], correct: 0, exp: "Ngô Quyền diệt trừ phản thần Kiều Công Tiễn rồi tiến ra Bạch Đằng tiêu diệt quân Nam Hán." }
                ]
            },
            {
                id: 2,
                title: "Màn 2: Hào Khí Lý - Trần - Lê",
                timePerQuestion: 20,
                questions: [
                    { q: "Đinh Bộ Lĩnh có công lao lịch sử nổi bật nào?", options: ["Dời đô về Thăng Long", "Dẹp loạn 12 quân sứ", "Đánh tan quân Nguyên", "Viết Bình Ngô Đại Cáo"], correct: 1, exp: "Đinh Bộ Lĩnh đã đánh dẹp loạn 12 quân sứ, thống nhất đất nước và lập ra nhà Đinh." },
                    { q: "Năm 1010, vị vua nào quyết định dời đô từ Hoa Lư về Thăng Long?", options: ["Lý Thái Tổ", "Lý Thái Tông", "Lý Nhân Tông", "Trần Thái Tông"], correct: 0, exp: "Vua Lý Thái Tổ (Lý Công Uẩn) ban 'Chiếu dời đô' chuyển kinh đô về Thăng Long năm 1010." },
                    { q: "Bài thơ thần 'Nam quốc sơn hà' gắn liền với chiến công của ai?", options: ["Trần Hưng Đạo", "Lý Thường Kiệt", "Quang Trung", "Nguyễn Trãi"], correct: 1, exp: "Lý Thường Kiệt đọc bài thơ thần trên sông Như Nguyệt để cổ vũ tinh thần quân sĩ chống Tống." },
                    { q: "Quân dân nhà Trần đã mấy lần đánh tan quân xâm lược Nguyên Mông?", options: ["1 lần", "2 lần", "3 lần", "4 lần"], correct: 2, exp: "Quân dân nhà Trần xuất sắc 3 lần đánh bại đế quốc Nguyên Mông (1258, 1285, 1287-1288)." },
                    { q: "Hội nghị Diên Hồng do nhà Trần tổ chức để trưng cầu ý kiến ai?", options: ["Các quan lại", "Các vương tôn", "Các bô lão đại diện nhân dân", "Các tướng lĩnh"], correct: 2, exp: "Hội nghị Diên Hồng thể hiện sự đoàn kết khi hỏi ý kiến các bô lão về việc 'Nên đánh hay nên hòa'." },
                    { q: "Tác phẩm 'Bình Ngô Đại Cáo' do ai sáng tác?", options: ["Lê Lợi", "Nguyễn Trãi", "Trần Hưng Đạo", "Lê Thánh Tông"], correct: 1, exp: "Nguyễn Trãi thay lời Lê Lợi viết Bình Ngô Đại Cáo tuyên bố độc lập sau khi đại phá quân Minh." },
                    { q: "Khởi nghĩa Lam Sơn kéo dài bao nhiêu năm?", options: ["5 năm", "10 năm", "15 năm", "20 năm"], correct: 1, exp: "Khởi nghĩa Lam Sơn do Lê Lợi lãnh đạo kéo dài 10 năm (1418 - 1427) giành lại độc lập." },
                    { q: "Thái sư Trần Thủ Độ nổi tiếng với câu nói nào thể hiện quyết tâm chống Nguyên Mông?", options: ["Đầu thần chưa rơi xuống đất, xin bệ hạ đừng lo", "Thà làm ma nước Nam còn hơn làm vương đất Bắc", "Nếu muốn hàng hãy chặt đầu tôi đi", "Sát Thát"], correct: 0, exp: "Trần Thủ Độ trả lời vua Trần Thái Tông: 'Đầu thần chưa rơi xuống đất, xin bệ hạ đừng lo'." },
                    { q: "Ai là người khâu chữ 'Phá cường địch, báo hoàng ân' lên lá cờ ra trận?", options: ["Trần Quốc Toản", "Trần Quang Khải", "Trần Bình Trọng", "Trần Khánh Dư"], correct: 0, exp: "Trần Quốc Toản vì nhỏ tuổi không được dự họp đã bóp nát quả cam và thêu lá cờ 6 chữ vàng." },
                    { q: "Vị vua nào cho lập Văn Miếu - Quốc Tử Giám, trường đại học đầu tiên của nước ta?", options: ["Lý Thái Tổ", "Lý Thánh Tông", "Lý Nhân Tông", "Lê Thánh Tông"], correct: 1, exp: "Vua Lý Thánh Tông cho dựng Văn Miếu năm 1070, sau đó mở Quốc Tử Giám năm 1076." },
                    { q: "Trần Bình Trọng nổi tiếng với câu nói kiên cường nào trước kẻ thù?", options: ["Thà làm ma nước Nam còn hơn làm vương đất Bắc", "Đầu tôi chưa rơi xin bệ hạ đừng lo", "Đánh một trận sạch không kình ngạc", "Nhân nghĩa chi sư"], correct: 0, exp: "Khi bị quân Nguyên bắt và dụ dỗ, Trần Bình Trọng dõng dạc trả lời thà làm ma nước Nam." },
                    { q: "Chủ tướng nào lãnh đạo cuộc khởi nghĩa Lam Sơn chống quân Minh?", options: ["Lê Lợi", "Nguyễn Trãi", "Trần Nguyên Hãn", "Lê Lai"], correct: 0, exp: "Bình Định Vương Lê Lợi là người xướng xuất và lãnh đạo cuộc khởi nghĩa Lam Sơn." },
                    { q: "Lê Lai đã có hành động dũng cảm gì để cứu Lê Lợi?", options: ["Liều thân cứu chủ", "Đổi áo mặc thay Lê Lợi", "Chém tướng Minh", "Cướp lương thảo"], correct: 1, exp: "Lê Lai đã cải trang mặc áo gấm của Lê Lợi liều xông ra trận để giải cứu chủ tướng." },
                    { q: "Bộ luật Hồng Đức nổi tiếng được ban hành dưới thời vị vua nào?", options: ["Lê Thái Tổ", "Lê Thánh Tông", "Lý Thánh Tông", "Trần Nhân Tông"], correct: 1, exp: "Bộ luật Quốc triều hình luật (Luật Hồng Đức) đạt đỉnh cao dưới triều vua Lê Thánh Tông." },
                    { q: "Chiến thắng Chi Lăng - Xương Giang năm 1427 tiêu diệt tướng nào của nhà Minh?", options: ["Liễu Thăng", "Mộc Thạnh", "Vương Thông", "Mã Viện"], correct: 0, exp: "An Lạc Hầu Liễu Thăng bị quân Lam Sơn chém đầu tại ải Chi Lăng năm 1427." }
                ]
            },
            {
                id: 3,
                title: "Màn 3: Trịnh - Nguyễn & Tây Sơn",
                timePerQuestion: 18,
                questions: [
                    { q: "Sông nào làm ranh giới chia cắt Đàng Trong và Đàng Ngoài thời Trịnh - Nguyễn?", options: ["Sông Bến Hải", "Sông Gianh", "Sông Hương", "Sông Mã"], correct: 1, exp: "Sông Gianh (Quảng Bình) là ranh giới quân sự phân chia Đàng Trong và Đàng Ngoài gần 200 năm." },
                    { q: "Ba anh em Tây Sơn gồm những ai?", options: ["Nguyễn Nhạc, Nguyễn Huệ, Nguyễn Lữ", "Nguyễn Huệ, Nguyễn Ánh, Nguyễn Nhạc", "Nguyễn Trãi, Nguyễn Huệ, Nguyễn Lữ", "Nguyễn Huệ, Quang Trung, Nguyễn Nhạc"], correct: 0, exp: "Ba anh em Tây Sơn nổi dậy gồm Nguyễn Nhạc, Nguyễn Huệ và Nguyễn Lữ." },
                    { q: "Trận Rạch Gầm - Xoài Mút năm 1785 tiêu diệt lực lượng quân xâm lược nào?", options: ["Quân Thanh", "Quân Xiêm", "Quân Pháp", "Quân Minh"], correct: 1, exp: "Nguyễn Huệ dùng phục binh trên sông Tiền đánh tan 5 vạn quân Xiêm xâm lược năm 1785." },
                    { q: "Nguyễn Huệ chính thức lên ngôi Hoàng đế lấy niên hiệu Quang Trung vào năm nào?", options: ["1788", "1789", "1785", "1792"], correct: 0, exp: "Năm 1788, Nguyễn Huệ làm lễ lên ngôi tại Núi Băn (Thừa Thiên Huế) lấy niên hiệu Quang Trung." },
                    { q: "Đại thắng Ngọc Hồi - Đống Đa xuân Kỷ Dậu (1789) đánh tan quân xâm lược nào?", options: ["Quân Xiêm", "Quân Thanh", "Quân Nguyên", "Quân Mông Cổ"], correct: 1, exp: "Vua Quang Trung tiến quân thần tốc quét sạch 29 vạn quân Thanh vào mùng 5 Tết Kỷ Dậu 1789." },
                    { q: "Nữ tướng nổi tiếng nhất của triều đại Tây Sơn là ai?", options: ["Bùi Thị Xuân", "Nguyễn Thị Định", "Lê Chân", "Triệu Thị Trinh"], correct: 0, exp: "Đô đốc Bùi Thị Xuân là nữ danh tướng chỉ huy đội voi chiến dũng mãnh của Tây Sơn." },
                    { q: "Quân Thanh tiến sang xâm lược nước ta theo sự cầu viện của ai?", options: ["Lê Chiêu Thống", "Nguyễn Ánh", "Trịnh Cản", "Lê Chiêu Tông"], correct: 0, exp: "Lê Chiêu Thống hèn hạ chạy sang Trung Quốc cầu viện nhà Thanh về sang đánh Tây Sơn." },
                    { q: "Tướng quân nào của nhà Thanh phải thắt cổ tự tử tại gò Đống Đa?", options: ["Tôn Sĩ Nghị", "Sầm Nghi Đống", "Hứa Thế Hanh", "Thượng Chiêm"], correct: 1, exp: "Tướng Sầm Nghi Đống thất bại thảm hại đã thắt cổ tự tử trên gò Đống Đa." },
                    { q: "Trận Rạch Gầm - Xoài Mút diễn ra trên địa bàn tỉnh nào ngày nay?", options: ["Tiền Giang", "Bến Tre", "Cần Thơ", "Vĩnh Long"], correct: 0, exp: "Khúc sông Rạch Gầm - Xoài Mút thuộc địa phận tỉnh Tiền Giang ngày nay." },
                    { q: "Ai là tác giả tác phẩm 'Gia Định thành thông chí' nổi tiếng thời Nguyễn?", options: ["Trịnh Hoài Đức", "Lê Quý Đôn", "Phan Huy Chú", "Nguyễn Du"], correct: 0, exp: "Trịnh Hoài Đức biên soạn Gia Định thành thông chí phản ánh địa lý, lịch sử Nam Bộ." },
                    { q: "Chúa Nguyễn nào có công khai phá và mở rộng vùng đất Nam Bộ?", options: ["Nguyễn Hoàng", "Nguyễn Phúc Chu", "Nguyễn Phúc Ánh", "Nguyễn Hoàng Tôn"], correct: 0, exp: "Chúa Tiên Nguyễn Hoàng mở đường vào Nam, đặt nền móng khai phá vùng đất Đàng Trong." },
                    { q: "Lễ thành hầu Nguyễn Hữu Cảnh có công lao lớn gì năm 1698?", options: ["Đánh tan quân Xiêm", "Lập phủ Gia Định, mở rộng Nam Bộ", "Đắp lũy Thầy", "Mở cảng Hội An"], correct: 1, exp: "Nguyễn Hữu Cảnh kinh lược phương Nam, chính thức thành lập phủ Gia Định năm 1698." },
                    { q: "Văn bia tiến sĩ tại Văn Miếu Thăng Long bắt đầu được dựng từ thời nào?", options: ["Thời Lý", "Thời Trần", "Thời Lê Sơ", "Thời Nguyễn"], correct: 2, exp: "Vua Lê Thánh Tông bắt đầu cho dựng bia Tiến sĩ năm 1484 để vinh danh danh nhân tri thức." },
                    { q: "Trung tâm thương mại, cảng thị sầm uất nhất Đàng Trong thế kỷ 17 là đâu?", options: ["Hội An", "Phố Hiến", "Gia Định", "Đà Nẵng"], correct: 0, exp: "Hội An (Quảng Nam) là thương cảng quốc tế sầm uất bậc nhất thời chúa Nguyễn." },
                    { q: "Phố Hiến - cảng thị nổi tiếng Đàng Ngoài nằm ở tỉnh nào hiện nay?", options: ["Hải Phòng", "Hưng Yên", "Nam Định", "Quảng Ninh"], correct: 1, exp: "Phố Hiến thuộc tỉnh Hưng Yên, nổi tiếng với câu 'Thứ nhất Kinh Kỳ, thứ nhì Phố Hiến'." }
                ]
            },
            {
                id: 4,
                title: "Màn 4: Nhà Nguyễn & Chống Pháp",
                timePerQuestion: 15,
                questions: [
                    { q: "Năm 1802, ai lên ngôi đặt niên hiệu Gia Long, lập ra nhà Nguyễn?", options: ["Nguyễn Ánh", "Nguyễn Huệ", "Minh Mạng", "Tự Đức"], correct: 0, exp: "Nguyễn Ánh đánh bại Tây Sơn, lên ngôi lấy niên hiệu Gia Long, lập ra triều Nguyễn." },
                    { q: "Thực dân Pháp nổ súng tấn công cảng Đà Nẵng mở đầu xâm lược năm nào?", options: ["1858", "1867", "1883", "1885"], correct: 0, exp: "Liên quân Pháp - Tây Ban Nha nổ súng bắn vào bán đảo Sơn Trà (Đà Nẵng) ngày 1/9/1858." },
                    { q: "Anh hùng Trương Định được nhân dân Nam Bộ tôn xưng là gì?", options: ["Bình Tây Đại Nguyên Soái", "Bình Định Vương", "Bố Cái Đại Vương", "Kháng Pháp Tướng Quân"], correct: 0, exp: "Trương Định từ chối lệnh rút quân của triều đình, ở lại cùng dân đánh Pháp và được tôn là Bình Tây Đại Nguyên Soái." },
                    { q: "Ai là tác giả câu nói nổi tiếng 'Bao giờ người Tây rút hết cỏ nước Nam thì mới hết người Nam đánh Tây'?", options: ["Trương Định", "Nguyễn Trung Trực", "Thủ Khoa Huân", "Phan Đình Phùng"], correct: 1, exp: "Nguyễn Trung Trực dõng dạc tuyên bố trước khi bị thực dân Pháp hành quyết." },
                    { q: "Trận đốt cháy tàu Hy Vọng (Espérance) của Pháp trên sông Nhật Tảo do ai chỉ huy?", options: ["Nguyễn Trung Trực", "Trương Định", "Nguyễn Tri Phương", "Hoàng Diệu"], correct: 0, exp: "Nguyễn Trung Trực chỉ huy trận tập kích đốt cháy tàu chiến Espérance năm 1861." },
                    { q: "Phong trào Cần Vương bùng nổ sau chiếu Cần Vương của vị vua nào?", options: ["Hàm Nghi", "Duy Tân", "Thành Thái", "Bảo Đại"], correct: 0, exp: "Vua Hàm Nghi ban chiếu Cần Vương năm 1885 kêu gọi sĩ phu và nhân dân giúp vua cứu nước." },
                    { q: "Ai là lãnh đạo tối cao của cuộc khởi nghĩa Hương Khê?", options: ["Phan Đình Phùng", "Đinh Công Tráng", "Nguyễn Thiện Thuật", "Hoàng Hoa Thám"], correct: 0, exp: "Phan Đình Phùng là linh hồn của cuộc khởi nghĩa Hương Khê - cuộc khởi nghĩa lớn nhất phong trào Cần Vương." },
                    { q: "Anh hùng Hoàng Hoa Thám lãnh đạo cuộc khởi nghĩa nào chống Pháp?", options: ["Khởi nghĩa Yên Thế", "Khởi nghĩa Ba Đình", "Khởi nghĩa Bãi Sậy", "Khởi nghĩa Hùng Lĩnh"], correct: 0, exp: "Hoàng Hoa Thám (Hùm xám Yên Thế) lãnh đạo nông dân Yên Thế kiên cường chống Pháp suốt gần 30 năm." },
                    { q: "Phong trào Đông Du vận động thanh niên sang nước nào học tập?", options: ["Trung Quốc", "Nhật Bản", "Pháp", "Nga"], correct: 1, exp: "Phan Bội Châu khởi xướng phong trào Đông Du đưa thanh niên sang Nhật Bản du học." },
                    { q: "Nguyễn Tất Thành ra đi tìm đường cứu nước từ bến cảng nào?", options: ["Cảng Đà Nẵng", "Cảng Hải Phòng", "Cảng Nhà Rồng", "Cảng Cam Ranh"], correct: 2, exp: "Ngày 5/6/1911, người thanh niên Nguyễn Tất Thành rời bến cảng Nhà Rồng ra đi tìm đường cứu nước." },
                    { q: "Hai tổng đốc kiên cường tự thuẫn để bảo vệ thành Hà Nội là những ai?", options: ["Nguyễn Tri Phương & Hoàng Diệu", "Trương Định & Nguyễn Trung Trực", "Phan Thanh Cản & Tự Đức", "Hoàng Hoa Thám & Phan Đình Phùng"], correct: 0, exp: "Tổng đốc Nguyễn Tri Phương (1873) và Tổng đốc Hoàng Diệu (1882) tuẫn tiết thề sống chết cùng thành Hà Nội." },
                    { q: "Khởi nghĩa Ba Đình do ai lãnh đạo?", options: ["Đinh Công Tráng", "Phan Đình Phùng", "Nguyễn Thiện Thuật", "Hoàng Hoa Thám"], correct: 0, exp: "Đinh Công Tráng và Phạm Bành lãnh đạo căn cứ Ba Đình (Thanh Hóa) chống Pháp." },
                    { q: "Tổ chức Việt Nam Quang phục Hội do ai sáng lập năm 1912?", options: ["Phan Bội Châu", "Phan Châu Trinh", "Huỳnh Thúc Kháng", "Cường Để"], correct: 0, exp: "Phan Bội Châu thành lập Việt Nam Quang phục Hội tại Quảng Châu (Trung Quốc)." },
                    { q: "Cuộc vận động Duy Tân đầu thế kỷ XX gắn liền với tên tuổi sĩ phu nào?", options: ["Phan Châu Trinh", "Phan Bội Châu", "Nguyễn Thái Học", "Lương Văn Can"], correct: 0, exp: "Phan Châu Trinh đề xướng phong trào Duy Tân với khẩu hiệu 'Khai dân trí, chấn dân khí, hậu dân sinh'." },
                    { q: "Trường Đông Kinh Nghĩa Thục (1907) được thành lập tại đâu?", options: ["Hà Nội", "Huế", "Sài Gòn", "Đà Nẵng"], correct: 0, exp: "Đông Kinh Nghĩa Thục do Lương Văn Can, Nguyễn Quyền sáng lập tại Hà Nội nhằm tân văn hóa." }
                ]
            },
            {
                id: 5,
                title: "Màn 5: Cách Mạng & Kháng Pháp (1930 - 1954)",
                timePerQuestion: 12,
                questions: [
                    { q: "Đảng Cộng sản Việt Nam được thành lập vào ngày tháng năm nào?", options: ["03/02/1930", "19/05/1930", "02/09/1945", "19/12/1946"], correct: 0, exp: "Hội nghị hợp nhất các tổ chức cộng sản diễn ra tại Cửu Long (Hương Cảng) do Nguyễn Ái Quốc chủ trì ngày 3/2/1930." },
                    { q: "Tổng Bí thư đầu tiên của Đảng Cộng sản Việt Nam là ai?", options: ["Trần Phú", "Lê Hồng Phong", "Nguyễn Văn Cừ", "Trường Chinh"], correct: 0, exp: "Đồng chí Trần Phú được bầu làm Tổng Bí thư đầu tiên của Đảng tháng 10/1930." },
                    { q: "Bác Hồ đọc bản Tuyên ngôn Độc lập khai sinh nước VNDCCH vào ngày nào?", options: ["19/08/1945", "02/09/1945", "19/12/1946", "07/05/1954"], correct: 1, exp: "Ngày 2/9/1945, tại Quảng trường Ba Đình, Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập." },
                    { q: "Lời kêu gọi Toàn quốc kháng chiến được Bác Hồ phát động vào ngày nào?", options: ["19/12/1946", "23/09/1945", "19/12/1945", "10/10/1954"], correct: 0, exp: "Đêm 19/12/1946, Chủ tịch Hồ Chí Minh ra Lời kêu gọi Toàn quốc kháng chiến." },
                    { q: "Chiến dịch Việt Bắc thu - đông 1947 đánh tan kế hoạch quân sự nào của Pháp?", options: ["Đánh nhanh thắng nhanh", "Nava", "Rơ-ve", "Bồ-đoanh"], correct: 0, exp: "Chiến dịch Việt Bắc 1947 làm phá sản hoàn toàn chiến lược 'Đánh nhanh thắng nhanh' của thực dân Pháp." },
                    { q: "Anh hùng nào đã lấy thân mình lấp lỗ châu mai trong Chiến dịch Điện Biên Phủ?", options: ["Phan Đình Giót", "Bế Văn Đàn", "Tô Vĩnh Diện", "Cù Chính Lan"], correct: 0, exp: "Phan Đình Giót dũng cảm lấy thân mình lấp lỗ châu mai mở đường cho đồng đội tiến lên." },
                    { q: "Anh hùng lấy thân làm giá súng trong chiến dịch là ai?", options: ["Bế Văn Đàn", "Phan Đình Giót", "Tô Vĩnh Diện", "Nguyễn Quốc Trị"], correct: 0, exp: "Bế Văn Đàn lấy thân mình làm giá súng cho đồng đội bắn tỉa tiêu diệt địch." },
                    { q: "Anh hùng Tô Vĩnh Diện đã có hành động dũng cảm nào?", options: ["Lấy thân chèn pháo", "Lấp lỗ châu mai", "Làm giá súng", "Đốt xe tăng"], correct: 0, exp: "Tô Vĩnh Diện đã xả thân chèn lưng cứu khẩu pháo cao xạ khỏi lao xuống vực thẳm." },
                    { q: "Chiến thắng Điện Biên Phủ lừng lẫy năm châu diễn ra vào ngày nào?", options: ["07/05/1954", "30/04/1954", "13/03/1954", "20/07/1954"], correct: 0, exp: "Chiều 7/5/1954, lá cờ Quyết chiến Quyết thắng tung bay trên mái hầm Tướng De Castries." },
                    { q: "Tướng chỉ huy tập đoàn căn cứ điểm Điện Biên Phủ của Pháp là ai?", options: ["De Castries", "Navarre", "Salan", "Cogny"], correct: 0, exp: "Tướng De Castries cùng toàn bộ BTM tập đoàn căn cứ điểm Điện Biên Phủ bị bắt sống." },
                    { q: "Tổng chỉ huy Quân đội Nhân dân VN trong chiến dịch Điện Biên Phủ là ai?", options: ["Võ Nguyên Giáp", "Nguyễn Chí Thanh", "Văn Tiến Dũng", "Trần Giao"], correct: 0, exp: "Đại tướng Võ Nguyên Giáp là Tổng chỉ huy trực tiếp chỉ đạo chiến dịch Điện Biên Phủ." },
                    { q: "Hiệp định Giơ-ne-vơ năm 1954 lấy vĩ tuyến nào làm ranh giới quân sự tạm thời?", options: ["Vĩ tuyến 17", "Vĩ tuyến 16", "Vĩ tuyến 18", "Vĩ tuyến 20"], correct: 0, exp: "Hiệp định Giơ-ne-vơ lấy vĩ tuyến 17 (sông Bến Hải, Quảng Trị) làm ranh giới quân sự tạm thời." },
                    { q: "Phong trào Xô Viết Nghệ Tĩnh diễn ra trong đỉnh cao năm nào?", options: ["1930 - 1931", "1936 - 1939", "1939 - 1945", "1945"], correct: 0, exp: "Phong trào Xô Viết Nghệ Tĩnh (1930-1931) là cuộc diễn tập đầu tiên cho Cách mạng Tháng Tám." },
                    { q: "Mặt trận Việt Minh (Việt Nam Độc lập Đồng minh) thành lập năm nào?", options: ["1941", "1930", "1945", "1936"], correct: 0, exp: "Mặt trận Việt Minh do Nguyễn Ái Quốc sáng lập ngày 19/5/1941 tại Pắc Bó (Cao Bằng)." },
                    { q: "Đội Việt Nam Tuyên truyền Giải phóng quân thành lập ngày 22/12/1944 có bao nhiêu chiến sĩ?", options: ["34 chiến sĩ", "12 chiến sĩ", "50 chiến sĩ", "100 chiến sĩ"], correct: 0, exp: "Đội gồm 34 chiến sĩ do đồng chí Võ Nguyên Giáp trực tiếp chỉ huy thành lập tại Cao Bằng." }
                ]
            },
            {
                id: 6,
                title: "Màn 6: Chống Mỹ & Thống Nhất",
                timePerQuestion: 10,
                questions: [
                    { q: "Phong trào 'Đồng Khởi' (1960) bùng nổ sớm nhất và mạnh mẽ nhất ở tỉnh nào?", options: ["Bến Tre", "Mỹ Tho", "Tây Ninh", "Cà Mau"], correct: 0, exp: "Phong trào Đồng Khởi khởi nguồn từ Bến Tre dưới sự lãnh đạo của Nữ tướng Nguyễn Thị Định." },
                    { q: "Tuyến đường chiến lược viện trợ sức người sức của cho miền Nam có tên là gì?", options: ["Đường Trường Sơn (Đường Hồ Chí Minh)", "Đường 9 Nam Lào", "Đường 1A", "Đường Cái Quan"], correct: 0, exp: "Tuyến đường huyền thoại Trường Sơn (Đường Hồ Chí Minh) bắt đầu mở từ năm 1959." },
                    { q: "Cuộc Tổng tiến công và nổi dậy Mậu Thân diễn ra vào năm nào?", options: ["1968", "1972", "1965", "1975"], correct: 0, exp: "Cuộc tiến công bất ngờ Mậu Thân 1968 đã làm giật mình và làm phá sản chiến lược Chiến tranh cục bộ." },
                    { q: "Chiến thắng 'Điện Biên Phủ trên không' năm 1972 đập tan cuộc tập kích bằng máy bay nào?", options: ["B-52", "F-4", "A-37", "C-130"], correct: 0, exp: "Quân dân Hà Nội - Hải Phòng đánh tan cuộc tập kích chiến lược bằng máy bay B-52 suốt 12 ngày đêm." },
                    { q: "Chiến dịch giải phóng Sài Gòn - Gia Định chính thức đổi tên thành chiến dịch gì?", options: ["Chiến dịch Hồ Chí Minh", "Chiến dịch Tây Nguyên", "Chiến dịch Huế - Đà Nẵng", "Chiến dịch Xuân 1975"], correct: 0, exp: "Bộ Chính trị quyết định đổi tên Chiến dịch giải phóng Sài Gòn thành Chiến dịch Hồ Chí Minh." },
                    { q: "Xe tăng mang số hiệu nào đã húc văng cổng chính Dinh Độc Lập ngày 30/4/1975?", options: ["Xe tăng 390", "Xe tăng 843", "Xe tăng 380", "Xe tăng 840"], correct: 0, exp: "Xe tăng 390 do Trung úy Vũ Đăng Toàn chỉ huy húc văng cổng chính Dinh Độc Lập trưa 30/4/1975." },
                    { q: "Chiến dịch mở màn cho Tổng tiến công và nổi dậy Mùa Xuân 1975 là chiến dịch nào?", options: ["Chiến dịch Tây Nguyên", "Chiến dịch Huế - Đà Nẵng", "Chiến dịch Hồ Chí Minh", "Chiến dịch Đường 14"], correct: 0, exp: "Trận đòn điểm huyệt Buôn Ma Thuột mở màn cho Chiến dịch Tây Nguyên thắng lợi rực rỡ." },
                    { q: "Tổng thống cuối cùng của chính quyền Sài Gòn tuyên bố đầu hàng không điều kiện là ai?", options: ["Dương Văn Minh", "Nguyễn Văn Thiệu", "Trần Văn Hương", "Nguyễn Cao Kỳ"], correct: 0, exp: "Tổng thống Dương Văn Minh đọc lời tuyên bố đầu hàng không điều kiện trưa ngày 30/4/1975." },
                    { q: "Năm 1976, Quốc hội quyết định đổi tên thành phố Sài Gòn - Gia Định thành gì?", options: ["Thành phố Hồ Chí Minh", "Thành phố Nam Bộ", "Thành phố Gia Định", "Thành phố Mới"], correct: 0, exp: "Quốc hội khóa VI đổi tên thành phố Sài Gòn - Gia Định chính thức thành Thành phố Hồ Chí Minh." },
                    { q: "Đường lối Đổi Mới đất nước chính thức được Đảng đề ra từ Đại hội toàn quốc lần thứ mấy?", options: ["Đại hội VI (1986)", "Đại hội V (1981)", "Đại hội VII (1991)", "Đại hội IV (1976)"], correct: 0, exp: "Đại hội Đảng lần thứ VI (12/1986) mở ra thời kỳ Đổi Mới toàn diện cho Việt Nam." },
                    { q: "Nữ tướng duy nhất của Quân đội Nhân dân VN thời kỳ chống Mỹ là ai?", options: ["Nguyễn Thị Định", "Bùi Thị Xuân", "Nguyễn Thị Bình", "Hà Thị Liêm"], correct: 0, exp: "Bà Nguyễn Thị Định là Phó Tổng Tư lệnh Quân giải phóng miền Nam, phong Thiếu tướng năm 1965." },
                    { q: "Đại đội 915 lực lượng thanh niên xung phong hy sinh kiên cường tại đâu đêm Noel 1972?", options: ["Lưu Xá (Thái Nguyên)", "Gạt Ma", "Đồng Lộc", "Trường Sơn"], correct: 0, exp: "60 chiến sĩ TNXP Đại đội 915 đã anh dũng hy sinh tại ga Lưu Xá khi giải tỏa hàng hóa viện trợ." },
                    { q: "Chiến thắng Đường 14 - Phước Long (1/1975) có ý nghĩa như thế nào?", options: ["Trận đòn trinh sát chiến lược", "Giải phóng toàn miền Nam", "Phá sản chiến tranh đặc biệt", "Buộc Mỹ ký Hiệp định"], correct: 0, exp: "Thắng lợi Phước Long được xem là 'trận đòn trinh sát' chứng minh sự suy yếu của chính quyền Sài Gòn." },
                    { q: "Tác phẩm 'Nhật ký Đặng Thùy Trâm' gắn liền với chiến trường nào?", options: ["Đức Phổ (Quảng Ngãi)", "Củ Chi", "Tây Nguyên", "Khe Sanh"], correct: 0, exp: "Nữ bác sĩ hy sinh tại địa bàn huyện Đức Phổ (Quảng Ngãi) trong khi làm nhiệm vụ." },
                    { q: "Việt Nam chính thức trở thành thành viên thứ 149 của Liên Hợp Quốc (LHQ) vào năm nào?", options: ["1977", "1975", "1986", "1995"], correct: 0, exp: "Ngày 20/9/1977, Việt Nam chính thức gia nhập Liên Hợp Quốc." }
                ]
            }
        ];

        // App State
        let currentState = {
            currentLevelIdx: 0,
            currentQuestionIdx: 0,
            score: 0,
            timer: null,
            timeLeft: 0,
            sfxEnabled: true,
            bgmEnabled: true,
            unlockedLevels: 1,
            levelScores: [0, 0, 0, 0, 0, 0],
            lifelines: { p5050: true, hint: true, audience: true }
        };

        // Audio Context for Effects
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        function playBeep(freq, duration) {
            if (!currentState.sfxEnabled) return;
            try {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.value = freq;
                gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch(e){}
        }

        // Load & Save Progress
        function loadProgress() {
            const saved = localStorage.getItem('historacle_progress');
            if (saved) {
                const data = JSON.parse(saved);
                currentState.unlockedLevels = data.unlockedLevels || 1;
                currentState.levelScores = data.levelScores || [0, 0, 0, 0, 0, 0];
            }
        }

        function saveProgress() {
            localStorage.setItem('historacle_progress', JSON.stringify({
                unlockedLevels: currentState.unlockedLevels,
                levelScores: currentState.levelScores
            }));
        }

        // Navigation
        function showScreen(screenId) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            
            if (screenId === 'screen-levels') {
                renderLevels();
            }
        }

        // Render Levels Screen
        function renderLevels() {
            const grid = document.getElementById('levels-grid');
            grid.innerHTML = '';

            gameData.forEach((lvl, idx) => {
                const isLocked = idx + 1 > currentState.unlockedLevels;
                const score = currentState.levelScores[idx];
                const card = document.createElement('div');
                card.className = `level-card ${isLocked ? 'locked' : ''}`;
                
                let starsHTML = '';
                if (!isLocked) {
                    const stars = score >= 120 ? 3 : score >= 80 ? 2 : score >= 40 ? 1 : 0;
                    starsHTML = '<div class="level-stars">';
                    for (let i = 0; i < 3; i++) {
                        starsHTML += `<i class="fa-${i < stars ? 'solid' : 'regular'} fa-star"></i> `;
                    }
                    starsHTML += '</div>';
                }

                card.innerHTML = `
                    <div class="level-number">MÀN ${idx + 1}</div>
                    <div class="level-name">${lvl.title.split(':')[1] || lvl.title}</div>
                    ${isLocked ? '<i class="fa-solid fa-lock lock-icon"></i>' : starsHTML}
                    <div style="font-size:0.75rem; color:#aaa;">${lvl.questions.length} câu hỏi</div>
                `;

                if (!isLocked) {
                    card.onclick = () => startLevel(idx);
                }

                grid.appendChild(card);
            });
        }

        // Start Level
        function startLevel(lvlIdx) {
            currentState.currentLevelIdx = lvlIdx;
            currentState.currentQuestionIdx = 0;
            currentState.score = 0;
            currentState.lifelines = { p5050: true, hint: true, audience: true };
            
            // Reset Lifeline UI
            document.querySelectorAll('.lifeline-btn').forEach(btn => btn.classList.remove('used'));
