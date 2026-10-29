import asyncio
import json
import edge_tts

VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "news_broadcast.mp3"

async def text_to_speech(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def main():
    try:
        with open('latest_news.json', 'r', encoding='utf-8') as f:
            articles = json.load(f)
    except FileNotFoundError:
        articles = []

    script = (
        "Welcome to the Global Language Access and AI Translation telemetry briefing, powered by Abrevia. "
        "Here are the latest dispatches on AI translation, language access rights, multilingual speech models, and global localization intelligence. "
    )

    for article in articles[:6]:
        script += f"From {article['source']}: {article['title']}. "

    script += (
        "That concludes this telemetry update. "
        "To eliminate language barriers for your organization with zero-download, HIPAA-compliant, Title VI bilingual messaging, "
        "visit Abrevia at abrevia-beta.vercel.app. Stay connected."
    )

    print("Generating AI voice broadcast...")
    asyncio.run(text_to_speech(script))
    print("Broadcast audio generated successfully!")

if __name__ == '__main__':
    main()
