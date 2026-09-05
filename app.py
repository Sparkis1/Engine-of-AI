import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_video_content(audio_file_path):
    print("⏳ Step 1: Transcribing audio/video file via Whisper...")
    
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format="verbose_json",
            timestamp_granularities=["segment"]
        )
    
    timestamp_guide = ""
    for seg in transcription.segments:
        start_min = int(seg['start'] // 60)
        start_sec = int(seg['start'] % 60)
        timestamp_guide += f"[{start_min:02d}:{start_sec:02d}] {seg['text']}\n"

    print("⏳ Step 2: Generating smart metadata and chapters via GPT-4o...")

    system_prompt = (
        "You are an expert video marketer, SEO specialist, and content editor for YouTube and TikTok. "
        "Your task is to analyze the provided transcript with timestamps and generate a complete distribution package."
    )
    
    user_prompt = f"""
    Here is the video transcript with timestamps:
    {timestamp_guide}
    
    Please generate the following clearly separated sections:
    1. 🎯 VIRAL TITLES (5 high-CTR, SEO-optimized title options).
    2. 📜 YOUTUBE CHAPTERS (Standard format '00:00 - Chapter Name' based on topic shifts).
    3. 📝 DESCRIPTION & HASHTAGS (An engaging short summary + 5 relevant hashtags).
    4. ✂️ SHORTS / TIKTOK IDEAS (Identify 2-3 viral hooks with exact time ranges and why they work).
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    
    return response.choices.message.content

if __name__ == "__main__":
    target_file = "interview_or_podcast.mp3" 
    
    if os.path.exists(target_file):
        final_result = process_video_content(target_file)
        print("\n🚀 === GENERATED CONTENT FOR CREATOR ===\n")
        print(final_result)
        
        with open("creator_result.txt", "w", encoding="utf-8") as f:
            f.write(final_result)
        print("\n✅ Results successfully saved to 'creator_result.txt'!")
    else:
        print(f"❌ File '{target_file}' not found in the folder.")
