"""WhatsApp Posting Module

Handles posting to WhatsApp groups and channels.
"""

import pywhatkit as kit
import pyautogui
import time
import logging
from datetime import datetime, timedelta
import requests

class WhatsAppPoster:
    """Post content to WhatsApp groups and channels"""
    
    def __init__(self, wait_time=15):
        self.wait_time = wait_time
        self.use_api = False  # Set to True if using API
        self.api_url = None
        self.api_token = None
        logging.info("WhatsApp Poster initialized")
    
    def configure_api(self, api_url, api_token):
        """Configure API for channel posting (optional)"""
        self.use_api = True
        self.api_url = api_url
        self.api_token = api_token
        logging.info("API configured for channel posting")
    
    def send_to_group(self, group_id, message):
        """Send message to WhatsApp group"""
        try:
            logging.info(f"Sending to group: {group_id}")
            
            # Calculate time 1 minute from now
            now = datetime.now()
            send_time = now + timedelta(minutes=1)
            
            kit.sendwhatmsg_to_group(
                group_id=group_id,
                message=message,
                time_hour=send_time.hour,
                time_min=send_time.minute,
                wait_time=self.wait_time,
                tab_close=True
            )
            
            # Wait and send
            time.sleep(self.wait_time + 5)
            pyautogui.press('enter')
            
            logging.info(f"Message sent to group: {group_id}")
            return True
        
        except Exception as e:
            logging.error(f"Error sending to group {group_id}: {str(e)}")
            return False
    
    def send_to_channel(self, channel_id, message):
        """Send message to WhatsApp channel"""
        if self.use_api and self.api_url:
            return self._send_via_api(channel_id, message)
        else:
            # Channels work similar to groups with pywhatkit
            return self.send_to_group(channel_id, message)
    
    def _send_via_api(self, channel_id, message):
        """Send via WhatsApp API (for channels)"""
        try:
            headers = {
                'accept': 'application/json',
                'content-type': 'application/json',
                'authorization': f'Bearer {self.api_token}'
            }
            
            payload = {
                'to': channel_id,
                'body': message,
                'typing_time': 0
            }
            
            response = requests.post(
                f"{self.api_url}/messages/text",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                logging.info(f"Message sent via API to: {channel_id}")
                return True
            else:
                logging.error(f"API error: {response.text}")
                return False
        
        except Exception as e:
            logging.error(f"Error sending via API: {str(e)}")
            return False
    
    def send_bulk(self, targets, message, delay=60):
        """Send to multiple groups/channels with delay"""
        results = []
        
        for target in targets:
            if target.endswith('@newsletter'):
                # It's a channel
                success = self.send_to_channel(target, message)
            else:
                # It's a group
                success = self.send_to_group(target, message)
            
            results.append({
                'target': target,
                'success': success,
                'timestamp': datetime.now().isoformat()
            })
            
            # Wait between sends
            if len(targets) > 1:
                time.sleep(delay)
        
        return results


if __name__ == "__main__":
    # Test poster
    poster = WhatsAppPoster()
    print("WhatsApp Poster ready")
    print("Configure your groups in config.py to test")
