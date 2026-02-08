"""Configuration for Islamic WhatsApp Automation

Configure your WhatsApp groups, channels, and posting schedule here.
"""

# ============================================
# WHATSAPP CONFIGURATION
# ============================================

# WhatsApp Groups (format: "GROUP_ID" from group invite link)
# To find group ID:
# 1. Open WhatsApp Web
# 2. Open your group
# 3. Look at URL or group info
WHATSAPP_GROUPS = [
    # Add your group IDs here
    # Example: "1234567890-1234567890",
]

# WhatsApp Channels (format: "CHANNEL_ID@newsletter")
# To find channel ID:
# 1. Use the GET /newsletters API endpoint
# 2. Or check channel link
WHATSAPP_CHANNELS = [
    # Add your channel IDs here
    # Example: "120363171744447809@newsletter",
]

# ============================================
# POSTING SCHEDULE
# ============================================

# Number of posts per day (5-10 recommended)
POSTS_PER_DAY = 7

# Exact posting times (24-hour format)
POSTING_TIMES = [
    "06:00",  # Fajr time
    "09:00",  # Morning
    "12:30",  # Dhuhr time
    "15:30",  # Asr time
    "18:00",  # Maghrib time
    "20:00",  # Isha time
    "22:00",  # Night
]

# ============================================
# CONTENT DISTRIBUTION
# ============================================

# Percentage of each content type
CONTENT_DISTRIBUTION = {
    'quran': 40,      # 40% Quran verses
    'hadith': 30,     # 30% Hadith
    'dua': 20,        # 20% Duas
    'allah_names': 10 # 10% Names of Allah
}

# ============================================
# API CONFIGURATION (Optional)
# ============================================

# For WhatsApp Channel API (Whapi.cloud or similar)
USE_WHATSAPP_API = False
WHATSAPP_API_URL = "https://gate.whapi.cloud"
WHATSAPP_API_TOKEN = "YOUR_API_TOKEN_HERE"

# Hadith API Key (get from hadithapi.com)
HADITH_API_KEY = "YOUR_HADITH_API_KEY"

# ============================================
# ADVANCED SETTINGS
# ============================================

# Wait time before sending (seconds)
WAIT_TIME = 15

# Delay between multiple posts (seconds)
DELAY_BETWEEN_POSTS = 60

# Auto-close browser tab after posting
CLOSE_TAB_AFTER_POST = True

# Enable logging
ENABLE_LOGGING = True

# Log file location
LOG_FILE = "islamic_automation.log"

# ============================================
# LANGUAGE SETTINGS
# ============================================

# Quran translation edition
QURAN_TRANSLATION = "en.asad"  # English - Muhammad Asad
# Other options:
# "en.sahih" - Saheeh International
# "en.yusufali" - Yusuf Ali
# "ur.jalandhry" - Urdu - Fateh Muhammad Jalandhry

# Include Arabic text
INCLUDE_ARABIC = True

# Include transliteration
INCLUDE_TRANSLITERATION = False
