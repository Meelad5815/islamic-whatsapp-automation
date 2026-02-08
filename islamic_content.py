"""Islamic Content Fetcher

Fetches Quran verses, Hadith, and other Islamic content from various APIs.
"""

import requests
import random
import logging
from datetime import datetime

class IslamicContentFetcher:
    """Fetch Islamic content from various APIs"""
    
    def __init__(self):
        self.quran_api = "https://api.alquran.cloud/v1"
        self.hadith_api = "https://hadithapi.com/api"
        self.hadith_api_key = "YOUR_API_KEY"  # Get from hadithapi.com
        
        # Alternative free APIs
        self.quran_api_alt = "https://quranapi.pages.dev/api"
        self.hadith_github = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1"
        
        logging.info("Islamic Content Fetcher initialized")
    
    def get_random_ayah(self):
        """Get random Quran verse with Arabic and English"""
        try:
            # Random surah (1-114) and ayah
            surah = random.randint(1, 114)
            
            # Get surah info first to know max ayahs
            response = requests.get(f"{self.quran_api}/surah/{surah}")
            surah_data = response.json()['data']
            
            max_ayahs = surah_data['numberOfAyahs']
            ayah = random.randint(1, max_ayahs)
            
            # Get Arabic
            arabic_response = requests.get(
                f"{self.quran_api}/ayah/{surah}:{ayah}/ar.alafasy"
            )
            arabic_data = arabic_response.json()['data']
            
            # Get English translation
            english_response = requests.get(
                f"{self.quran_api}/ayah/{surah}:{ayah}/en.asad"
            )
            english_data = english_response.json()['data']
            
            return {
                'type': 'quran',
                'arabic': arabic_data['text'],
                'translation': english_data['text'],
                'surah': surah_data['englishName'],
                'surah_arabic': surah_data['name'],
                'ayah': ayah,
                'reference': f"{surah}:{ayah}"
            }
        
        except Exception as e:
            logging.error(f"Error fetching Quran verse: {str(e)}")
            return self._get_fallback_quran()
    
    def get_random_hadith(self):
        """Get random Hadith from Sahih Bukhari or Muslim"""
        try:
            # Using free GitHub API
            collections = ['bukhari', 'muslim', 'abudawud', 'tirmidhi']
            collection = random.choice(collections)
            
            # Get random hadith number (Bukhari has ~7000 hadiths)
            hadith_num = random.randint(1, 50)  # Keep low for reliability
            
            url = f"{self.hadith_github}/editions/{collection}-{hadith_num}.json"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                hadith = data['hadiths'][0]
                
                return {
                    'type': 'hadith',
                    'text': hadith['text'],
                    'reference': f"{collection.title()} - Hadith {hadith_num}",
                    'collection': collection.title()
                }
            else:
                return self._get_fallback_hadith()
        
        except Exception as e:
            logging.error(f"Error fetching Hadith: {str(e)}")
            return self._get_fallback_hadith()
    
    def get_daily_dua(self):
        """Get a daily dua/supplication"""
        duas = [
            {
                'arabic': 'رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ',
                'translation': 'Our Lord, give us good in this world and good in the Hereafter, and protect us from the punishment of the Fire.',
                'reference': 'Quran 2:201'
            },
            {
                'arabic': 'رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي',
                'translation': 'My Lord, expand for me my breast and ease for me my task.',
                'reference': 'Quran 20:25-26'
            },
            {
                'arabic': 'رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً',
                'translation': 'Our Lord, do not let our hearts deviate after You have guided us, and grant us mercy from Yourself.',
                'reference': 'Quran 3:8'
            },
            {
                'arabic': 'اللَّهُمَّ إِنِّي أَسْأَلُكَ الْهُدَىٰ وَالتُّقَىٰ وَالْعَفَافَ وَالْغِنَىٰ',
                'translation': 'O Allah, I ask You for guidance, piety, chastity, and sufficiency.',
                'reference': 'Sahih Muslim'
            },
            {
                'arabic': 'حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ',
                'translation': 'Sufficient for us is Allah, and He is the best Disposer of affairs.',
                'reference': 'Quran 3:173'
            }
        ]
        
        dua = random.choice(duas)
        return {
            'type': 'dua',
            'arabic': dua['arabic'],
            'translation': dua['translation'],
            'reference': dua['reference']
        }
    
    def get_allah_name(self):
        """Get one of the 99 names of Allah"""
        names = [
            {'arabic': 'ٱلرَّحْمَـٰنُ', 'english': 'Ar-Rahman', 'meaning': 'The Most Merciful'},
            {'arabic': 'ٱلرَّحِيمُ', 'english': 'Ar-Raheem', 'meaning': 'The Bestower of Mercy'},
            {'arabic': 'ٱلْمَلِكُ', 'english': 'Al-Malik', 'meaning': 'The King'},
            {'arabic': 'ٱلْقُدُّوسُ', 'english': 'Al-Quddus', 'meaning': 'The Most Holy'},
            {'arabic': 'ٱلسَّلَامُ', 'english': 'As-Salam', 'meaning': 'The Source of Peace'},
            {'arabic': 'ٱلْعَزِيزُ', 'english': 'Al-Aziz', 'meaning': 'The All Mighty'},
            {'arabic': 'ٱلْحَكِيمُ', 'english': 'Al-Hakim', 'meaning': 'The All Wise'},
            {'arabic': 'ٱللَّطِيفُ', 'english': 'Al-Latif', 'meaning': 'The Subtle One'},
            {'arabic': 'ٱلْخَبِيرُ', 'english': 'Al-Khabir', 'meaning': 'The All Aware'},
            {'arabic': 'ٱلْغَفُورُ', 'english': 'Al-Ghafoor', 'meaning': 'The All Forgiving'}
        ]
        
        name = random.choice(names)
        return {
            'type': 'allah_name',
            'arabic': name['arabic'],
            'english': name['english'],
            'meaning': name['meaning']
        }
    
    def format_for_whatsapp(self, content):
        """Format content for WhatsApp posting"""
        if content['type'] == 'quran':
            return f"""🕌 *Quran Verse of the Day*

📖 _{content['surah']}_ ({content['surah_arabic']})
🔢 Ayah {content['ayah']}

*Arabic:*
{content['arabic']}

*Translation:*
{content['translation']}

━━━━━━━━━━━━━━━
📚 Reference: {content['reference']}
💚 Share the knowledge
"""
        
        elif content['type'] == 'hadith':
            return f"""📜 *Hadith of the Day*

{content['text']}

━━━━━━━━━━━━━━━
📚 {content['reference']}
🤲 May Allah guide us all
"""
        
        elif content['type'] == 'dua':
            return f"""🤲 *Dua of the Day*

*Arabic:*
{content['arabic']}

*Translation:*
{content['translation']}

━━━━━━━━━━━━━━━
📚 {content['reference']}
💚 Ameen
"""
        
        elif content['type'] == 'allah_name':
            return f"""✨ *Name of Allah*

{content['arabic']}
*{content['english']}*

📖 Meaning: {content['meaning']}

━━━━━━━━━━━━━━━
🤲 SubhanAllah
"""
        
        return str(content)
    
    def _get_fallback_quran(self):
        """Fallback Quran verse if API fails"""
        return {
            'type': 'quran',
            'arabic': 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
            'translation': 'In the name of Allah, the Most Gracious, the Most Merciful',
            'surah': 'Al-Fatihah',
            'surah_arabic': 'الفاتحة',
            'ayah': 1,
            'reference': '1:1'
        }
    
    def _get_fallback_hadith(self):
        """Fallback Hadith if API fails"""
        return {
            'type': 'hadith',
            'text': 'The best among you are those who have the best manners and character.',
            'reference': 'Sahih Bukhari',
            'collection': 'Bukhari'
        }


if __name__ == "__main__":
    # Test the fetcher
    fetcher = IslamicContentFetcher()
    
    print("\n" + "="*50)
    print("Testing Quran Verse:")
    print("="*50)
    quran = fetcher.get_random_ayah()
    print(fetcher.format_for_whatsapp(quran))
    
    print("\n" + "="*50)
    print("Testing Hadith:")
    print("="*50)
    hadith = fetcher.get_random_hadith()
    print(fetcher.format_for_whatsapp(hadith))
