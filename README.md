# Engine of AI

An AI-powered automation tool designed for content creators to speed up their workflow. It automatically processes video/audio files to generate SEO-optimized titles, YouTube chapters with precise timestamps, and viral ideas for Shorts/TikTok.

## 🚀 Features
- **Automated Transcription:** High-accuracy audio-to-text conversion via OpenAI Whisper.
- **Smart YouTube Chapters:** Automatic timestamp generation based on topic shifts.
- **SEO Title Generator:** 5 highly clickable, optimized title options.
- **Shorts/TikTok Clipper Ideas:** Identifies the most engaging hooks for short-form content.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Engine-of-AI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## 💻 How to Use
1. Place your audio/video file (e.g., `podcast.mp3`) in the project folder.
2. Run the script:
   ```bash
   python app.py
   ```
3. Find your generated metadata inside `rezultat_creator.txt`.
