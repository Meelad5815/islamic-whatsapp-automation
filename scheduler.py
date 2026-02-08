"""Scheduling System for Islamic Content

Automatically posts content at specified times throughout the day.
"""

import schedule
import time
import threading
import logging
from datetime import datetime
import random

class IslamicScheduler:
    """Schedule and automate Islamic content posting"""
    
    def __init__(self, content_fetcher, whatsapp_poster):
        self.content_fetcher = content_fetcher
        self.whatsapp_poster = whatsapp_poster
        self.is_running = False
        self.thread = None
        logging.info("Islamic Scheduler initialized")
    
    def post_random_content(self, targets):
        """Post random Islamic content"""
        try:
            # Choose random content type
            content_types = ['quran', 'hadith', 'dua', 'allah_name']
            weights = [0.4, 0.3, 0.2, 0.1]  # 40% Quran, 30% Hadith, etc.
            content_type = random.choices(content_types, weights=weights)[0]
            
            logging.info(f"Posting {content_type} content")
            
            # Fetch content
            if content_type == 'quran':
                content = self.content_fetcher.get_random_ayah()
            elif content_type == 'hadith':
                content = self.content_fetcher.get_random_hadith()
            elif content_type == 'dua':
                content = self.content_fetcher.get_daily_dua()
            else:
                content = self.content_fetcher.get_allah_name()
            
            # Format message
            message = self.content_fetcher.format_for_whatsapp(content)
            
            # Post to all targets
            results = self.whatsapp_poster.send_bulk(targets, message)
            
            logging.info(f"Posted {content_type} to {len(targets)} targets")
            return results
        
        except Exception as e:
            logging.error(f"Error posting content: {str(e)}")
            return []
    
    def setup_schedule(self, targets, posting_times):
        """Setup posting schedule"""
        schedule.clear()
        
        for post_time in posting_times:
            schedule.every().day.at(post_time).do(
                self.post_random_content,
                targets=targets
            )
            logging.info(f"Scheduled post at {post_time}")
    
    def run_schedule(self):
        """Run the schedule in a loop"""
        while self.is_running:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def start(self, targets=None, posting_times=None):
        """Start the scheduler"""
        if self.is_running:
            logging.warning("Scheduler already running")
            return
        
        # Import config here to avoid circular import
        from config import WHATSAPP_GROUPS, WHATSAPP_CHANNELS, POSTING_TIMES
        
        if targets is None:
            targets = WHATSAPP_GROUPS + WHATSAPP_CHANNELS
        
        if posting_times is None:
            posting_times = POSTING_TIMES
        
        self.setup_schedule(targets, posting_times)
        
        self.is_running = True
        self.thread = threading.Thread(target=self.run_schedule, daemon=True)
        self.thread.start()
        
        logging.info("Scheduler started")
        print(f"\n✅ Scheduler started!")
        print(f"📅 Will post {len(posting_times)} times per day")
        print(f"⏰ Posting times: {', '.join(posting_times)}")
        print(f"📱 Targets: {len(targets)} groups/channels\n")
    
    def stop(self):
        """Stop the scheduler"""
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=5)
        schedule.clear()
        logging.info("Scheduler stopped")
        print("\n❌ Scheduler stopped\n")
    
    def get_next_run_time(self):
        """Get next scheduled run time"""
        jobs = schedule.get_jobs()
        if jobs:
            next_job = min(jobs, key=lambda j: j.next_run)
            return next_job.next_run.isoformat()
        return None


if __name__ == "__main__":
    # Test scheduler
    from islamic_content import IslamicContentFetcher
    from whatsapp_poster import WhatsAppPoster
    
    fetcher = IslamicContentFetcher()
    poster = WhatsAppPoster()
    scheduler = IslamicScheduler(fetcher, poster)
    
    print("Scheduler test mode")
    print("Configure targets in config.py and call scheduler.start()")
