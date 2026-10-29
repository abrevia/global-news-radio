import asyncio
import edge_tts
import os

VOICE = "en-US-ChristopherNeural"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_PATH = os.path.join(OUTPUT_DIR, "episode-01.mp3")

EPISODE_SCRIPT = """
Welcome to Global News Radio Telemetry. This is an investigative special report. 
Behind the Wire: Episode One — The Shadow Tier.

When a Spanish-speaking mother in California calls 911 because her child is choking, or when a patient in an emergency trauma bay cannot speak English, the medical staff hits a button on their phone. Within seconds, a third voice joins the line. A certified medical interpreter.

To the hospital, this service is seamless. The hospital network is billed between two and three dollars and fifty cents for every single minute of that call. That is one hundred and twenty to over two hundred dollars an hour. At the top of the contract sits a multi-billion dollar language services giant—LanguageLine Solutions, backed by global parent Teleperformance.

Corporate filings celebrate high-margin language access and global telemetry. But who is that third voice actually on the line?

That voice belongs to a frontline linguist sitting at a desk in Mexico or Colombia. A human being navigating stroke diagnoses, pediatric emergencies, domestic violence disputes, and complex surgical consents.

And what does that frontline linguist get paid? Six dollars an hour.

And it gets worse. If that interpreter fails to adhere to rigid shift times or misses assigned call windows, their pay is slashed to an unlivable two dollars an hour. A punitive eighty-percent docking rate enforced by an intermediary management chain.

All the while, these workers are told they are independent contractors—freelancers. No health insurance, no social security through IMSS, no mandatory annual bonuses, no paid leave, and zero labor rights.

Today, we begin uncovering what happens behind the scenes. We are peeling back layer upon layer of middlemen who capture fortunes from the vital labor of others.

Here is how the subcontracting pyramid actually works.

Layer One is the Client: US hospitals, 911 call centers, and federal agencies operating under Title VI of the Civil Rights Act and Section 1557 of the Affordable Care Act. They mandate meaningful language access and pay top dollar for it.

Layer Two is the Prime Contractor: LanguageLine Solutions and Teleperformance Specialized Services. To avoid foreign labor laws, foreign payroll taxes, and legal liability in Latin America, they avoid hiring frontline interpreters directly. Instead, they route their volume through staffing networks.

Layer Three is the Managed Service Provider: Global workforce intermediaries like Kelly Services and KellyOCG, acting as account managers and compliance buffers.

Layer Four is the Local Nearshore Vendor: Companies like Solucenter International in Mexico. They bill the prime vendor between eighteen and twenty-eight dollars an hour. They pay the frontline worker six dollars, and pocket the twelve to twenty-two dollar margin for every single hour every interpreter spends taking calls.

To evade Mexican labor laws under the Ley Federal del Trabajo, these vendors operate through deliberate opacity. Contracts are misclassified as professional fees or honorarios. Supervision and attendance logs are routed through disposable WhatsApp groups managed by handlers using first names and personal cell phones.

If an interpreter questions why they are scheduled like a full-time employee without the legal benefits of one, they are reminded that their six-dollar rate can instantly drop to two dollars—or their login credentials can be deactivated overnight with zero explanation.

Under Mexican labor law, this has a specific legal name: Simulación Laboral—employment simulation fraud. Under Article 20 and 21 of the Ley Federal del Trabajo, when a company dictates your schedule, disciplines your performance, tracks your logins, and punitively docks your pay, you are an employee. The label on the contract is legally void.

And behind the wall of WhatsApp chats, the digital paper trail is indelible. Corporate compliance training emails, Workday credentials, and internal account management teams directly link the frontline linguists to the global conglomerates profiting from their labor.

This is not an isolated incident. Across Mexico, Central America, South America, and the Philippines, tens of thousands of skilled interpreters are kept in the shadows—bridging life-and-death conversations for the richest healthcare networks in the world, while absorbing the psychological toll of emergency work for poverty wages.

This is Episode One. In upcoming dispatches, we will continue publishing the evidence, dissecting the legal frameworks, and tracking the transition toward ethical, transparent, direct B2B language access models where the workers who carry the voice receive the compensation and dignity they have earned.

Stay tuned to Global News Radio Telemetry. Truth has no middleman.
""".strip()

async def generate_episode_audio():
    print(f"Generating Episode 1 Audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(
        EPISODE_SCRIPT,
        VOICE,
        rate="-2%",    # Slightly deliberate investigative pace
        pitch="-1Hz"
    )
    await communicate.save(AUDIO_PATH)
    print(f"Audio generated successfully at: {AUDIO_PATH}")
    size = os.path.getsize(AUDIO_PATH)
    print(f"Audio file size: {size} bytes ({size / 1024 / 1024:.2f} MB)")

if __name__ == '__main__':
    asyncio.run(generate_episode_audio())
