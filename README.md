# 🕌 Islamic WhatsApp Automation System

**روزانہ خودکار طریقے سے قرآن، حدیث اور دعائیں WhatsApp گروپس اور چینلز پر شیئر کریں**

Automatic daily posting of Quran verses, Hadith, Duas, and Names of Allah to your WhatsApp groups and channels with a beautiful web dashboard.

## ✨ Features

- 📖 **Quran Verses**: Random verses with Arabic text and English translation
- 📜 **Authentic Hadith**: From Sahih Bukhari, Muslim, Abu Dawud, Tirmidhi
- 🤲 **Daily Duas**: Beautiful supplications from Quran and Sunnah
- ✨ **99 Names of Allah**: With meanings and Arabic text
- 🌐 **Web Dashboard**: Beautiful Urdu/English interface to control everything
- ⏰ **Auto Scheduling**: Posts 5-10 times daily at Islamic prayer times
- 📱 **Multi-Target**: Post to multiple groups and channels simultaneously
- 📊 **Analytics**: Track posting history and success rates
- 🎨 **Beautiful Formatting**: Islamic-themed WhatsApp messages

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/Meelad5815/islamic-whatsapp-automation.git
cd islamic-whatsapp-automation

# Install dependencies
pip install -r requirements.txt

# Configure your groups
# Edit config.py and add your WhatsApp group IDs

# Run the dashboard
python app.py
```

Open your browser to: **http://localhost:5000**

## 📱 Configuration

### 1. Get WhatsApp Group IDs

1. Open [WhatsApp Web](https://web.whatsapp.com)
2. Click on your group
3. The URL contains the group ID
4. Add it to `config.py`:

```python
WHATSAPP_GROUPS = [
    "1234567890-1234567890",
    "9876543210-9876543210",
]
```

### 2. Get WhatsApp Channel IDs (Optional)

For channels, you need the Channel ID which ends with `@newsletter`:

```python
WHATSAPP_CHANNELS = [
    "120363171744447809@newsletter",
]
```

### 3. Configure Posting Schedule

```python
POSTING_TIMES = [
    "06:00",  # Fajr
    "09:00",  # Morning
    "12:30",  # Dhuhr
    "15:30",  # Asr
    "18:00",  # Maghrib
    "20:00",  # Isha
    "22:00",  # Night
]
```

## 🎯 Usage

### Web Dashboard

1. **Start the dashboard**: `python app.py`
2. **Open browser**: http://localhost:5000
3. **Control everything** from the beautiful interface:
   - Preview content before posting
   - Post immediately
   - Start/stop scheduler
   - View posting history
   - Monitor statistics

### Command Line

```python
from islamic_content import IslamicContentFetcher
from whatsapp_poster import WhatsAppPoster
from scheduler import IslamicScheduler

# Initialize
fetcher = IslamicContentFetcher()
poster = WhatsAppPoster()
scheduler = IslamicScheduler(fetcher, poster)

# Get content
quran = fetcher.get_random_ayah()
hadith = fetcher.get_random_hadith()
dua = fetcher.get_daily_dua()

# Post manually
message = fetcher.format_for_whatsapp(quran)
poster.send_to_group("GROUP_ID", message)

# Start automatic scheduling
scheduler.start()
```

## 📚 Islamic Content Sources

This system uses free, authentic Islamic APIs:

1. **Quran API**: [alquran.cloud](https://alquran.cloud/api) - Complete Quran with translations
2. **Hadith API**: [GitHub Hadith API](https://github.com/fawazahmed0/hadith-api) - Authentic Hadith collections
3. **Alternative**: [QuranAPI.pages.dev](https://quranapi.pages.dev) - No rate limits
4. **Hadith API**: [hadithapi.com](https://hadithapi.com) - Arabic, Urdu, English

## 🕌 Content Types

### Quran Verses (40%)
- Random verses from all 114 Surahs
- Arabic text + English translation
- Surah name and reference
- Formatted beautifully

### Hadith (30%)
- Sahih Bukhari
- Sahih Muslim
- Abu Dawud
- Tirmidhi
- English translations

### Duas (20%)
- Quranic supplications
- Prophetic Duas
- Arabic + English
- With references

### Names of Allah (10%)
- 99 Beautiful Names
- Arabic + Transliteration
- Meanings explained

## ⚙️ Features

### Web Dashboard
- 🎨 Beautiful Urdu/Arabic interface
- 📊 Real-time statistics
- 🔍 Content preview before posting
- 📝 Posting history
- ⚡ One-click posting
- 🕐 Scheduler control

### Automation
- ⏰ Automatic scheduling at prayer times
- 📅 5-10 posts per day (configurable)
- 🔄 Smart content rotation
- 🎲 Random content selection
- ⚖️ Weighted distribution

### WhatsApp Integration
- 👥 Multiple groups support
- 📢 Channel posting
- 🔁 Bulk messaging
- ⏱️ Rate limiting protection
- 🔒 Secure posting

## 📦 Project Structure

```
islamic-whatsapp-automation/
├── app.py                 # Flask web dashboard
├── islamic_content.py     # Content fetcher (APIs)
├── whatsapp_poster.py     # WhatsApp automation
├── scheduler.py           # Scheduling system
├── config.py             # Configuration
├── requirements.txt      # Dependencies
├── templates/
│   └── index.html        # Web interface
├── static/
│   └── style.css         # Styling
└── README.md
```

## 🔧 Advanced Configuration

### Using WhatsApp Channel API

For professional channel posting, configure API access:

```python
# In config.py
USE_WHATSAPP_API = True
WHATSAPP_API_URL = "https://gate.whapi.cloud"
WHATSAPP_API_TOKEN = "your_token_here"
```

Recommended providers:
- [Whapi.cloud](https://whapi.cloud) - Full WhatsApp API
- [WAHA](https://waha.devlike.pro) - Open source solution

### Custom Content Distribution

```python
CONTENT_DISTRIBUTION = {
    'quran': 50,      # 50% Quran
    'hadith': 30,     # 30% Hadith
    'dua': 15,        # 15% Duas
    'allah_names': 5  # 5% Names
}
```

### Translation Options

```python
# Choose Quran translation
QURAN_TRANSLATION = "en.asad"      # Muhammad Asad
# QURAN_TRANSLATION = "en.sahih"   # Saheeh International
# QURAN_TRANSLATION = "ur.jalandhry" # Urdu
```

## 🤖 Automation Setup

### Linux/Mac (Cron)

```bash
# Run dashboard on system startup
crontab -e

# Add:
@reboot cd /path/to/islamic-whatsapp-automation && python app.py
```

### Windows (Task Scheduler)

1. Open Task Scheduler
2. Create Basic Task
3. Trigger: At startup
4. Action: Start program
5. Program: `python.exe`
6. Arguments: `C:\path\to\app.py`

### Cloud Deployment

Deploy on:
- **Heroku**: Free tier available
- **Railway**: Easy deployment
- **DigitalOcean**: $5/month droplet
- **AWS**: EC2 free tier

## 📊 API Endpoints

```
GET  /                          Dashboard
GET  /api/fetch-content/<type>  Preview content
POST /api/post-now              Post immediately
POST /api/scheduler/start       Start automation
POST /api/scheduler/stop        Stop automation
GET  /api/scheduler/status      Get status
GET  /api/history               Get posting history
```

## 🔒 Security & Privacy

- ✅ Never commit `config.py` with real IDs
- ✅ Use environment variables for sensitive data
- ✅ Keep API tokens secure
- ✅ Follow WhatsApp's Terms of Service
- ✅ Respect rate limits

## ⚠️ Important Notes

1. **Rate Limiting**: 60 seconds delay between posts to avoid bans
2. **WhatsApp Web**: Must be logged in for automation
3. **API Limits**: Free APIs may have rate limits
4. **Browser**: Chrome/Firefox required for pywhatkit
5. **Permissions**: Must be group admin to post

## 🐛 Troubleshooting

### "Failed to send message"
- ✓ Check internet connection
- ✓ Verify group ID is correct
- ✓ Ensure logged into WhatsApp Web
- ✓ Check you're a group member

### "API Error"
- ✓ Check API is accessible
- ✓ Verify API key (if required)
- ✓ Check rate limits

### "Browser doesn't open"
- ✓ Install Chrome or Firefox
- ✓ Update pywhatkit: `pip install --upgrade pywhatkit`

## 📈 Roadmap

- [ ] Multi-language support (Urdu, Arabic, Bangla)
- [ ] Image generation for verses
- [ ] Audio Quran recitation
- [ ] Prayer times integration
- [ ] Mobile app
- [ ] Telegram bot integration
- [ ] Custom templates
- [ ] Analytics dashboard

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📜 License

MIT License - Free for personal and commercial use

## 🤲 Sadaqah Jariyah

This project is created as **Sadaqah Jariyah** (ongoing charity). If it benefits anyone in learning Islam, all rewards go to Allah (SWT).

> "When a person dies, all their deeds end except three: a continuing charity, beneficial knowledge, or a righteous child who prays for them." - Sahih Muslim

## 💚 Support

- ⭐ Star this repository
- 🔄 Share with others
- 🤲 Make dua for the developers
- 📢 Spread authentic Islamic knowledge

## 📧 Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues first

---

**بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ**

*In the name of Allah, the Most Gracious, the Most Merciful*

May Allah accept this work and make it beneficial for the Ummah. Ameen.

---

**Made with ❤️ for the Muslim Ummah**
