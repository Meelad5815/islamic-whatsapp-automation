"""Flask Web Dashboard for Islamic WhatsApp Automation

Web interface to manage and monitor automated Islamic content posting.
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from islamic_content import IslamicContentFetcher
from whatsapp_poster import WhatsAppPoster
from scheduler import IslamicScheduler
from config import *
import logging
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('islamic_automation.log'),
        logging.StreamHandler()
    ]
)

# Initialize components
content_fetcher = IslamicContentFetcher()
whatsapp_poster = WhatsAppPoster()
scheduler = IslamicScheduler(content_fetcher, whatsapp_poster)

# Store posting history
POST_HISTORY_FILE = 'post_history.json'

def load_history():
    """Load posting history from file"""
    if os.path.exists(POST_HISTORY_FILE):
        with open(POST_HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(entry):
    """Save posting entry to history"""
    history = load_history()
    history.insert(0, entry)  # Add to beginning
    # Keep only last 100 entries
    history = history[:100]
    with open(POST_HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Main dashboard page"""
    history = load_history()
    stats = {
        'total_posts': len(history),
        'today_posts': len([h for h in history if h.get('date', '').startswith(datetime.now().strftime('%Y-%m-%d'))]),
        'total_groups': len(WHATSAPP_GROUPS) + len(WHATSAPP_CHANNELS),
        'scheduler_status': 'Active' if scheduler.is_running else 'Stopped'
    }
    return render_template('index.html', 
                         history=history[:10],  # Show last 10
                         stats=stats,
                         config={
                             'daily_posts': POSTS_PER_DAY,
                             'posting_times': POSTING_TIMES,
                             'groups': WHATSAPP_GROUPS,
                             'channels': WHATSAPP_CHANNELS
                         })

@app.route('/api/fetch-content/<content_type>')
def fetch_content_preview(content_type):
    """Fetch and preview Islamic content"""
    try:
        if content_type == 'quran':
            content = content_fetcher.get_random_ayah()
        elif content_type == 'hadith':
            content = content_fetcher.get_random_hadith()
        elif content_type == 'dua':
            content = content_fetcher.get_daily_dua()
        elif content_type == 'name':
            content = content_fetcher.get_allah_name()
        else:
            return jsonify({'error': 'Invalid content type'}), 400
        
        return jsonify({
            'success': True,
            'content': content,
            'formatted': content_fetcher.format_for_whatsapp(content)
        })
    except Exception as e:
        logging.error(f"Error fetching {content_type}: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/post-now', methods=['POST'])
def post_now():
    """Post content immediately to WhatsApp"""
    try:
        data = request.json
        content_type = data.get('content_type', 'quran')
        
        # Fetch content
        if content_type == 'quran':
            content = content_fetcher.get_random_ayah()
        elif content_type == 'hadith':
            content = content_fetcher.get_random_hadith()
        elif content_type == 'dua':
            content = content_fetcher.get_daily_dua()
        elif content_type == 'name':
            content = content_fetcher.get_allah_name()
        else:
            return jsonify({'error': 'Invalid content type'}), 400
        
        message = content_fetcher.format_for_whatsapp(content)
        
        # Post to groups
        results = []
        for group_id in WHATSAPP_GROUPS:
            success = whatsapp_poster.send_to_group(group_id, message)
            results.append({'group_id': group_id, 'success': success})
        
        # Post to channels
        for channel_id in WHATSAPP_CHANNELS:
            success = whatsapp_poster.send_to_channel(channel_id, message)
            results.append({'channel_id': channel_id, 'success': success})
        
        # Save to history
        save_history({
            'date': datetime.now().isoformat(),
            'type': content_type,
            'content': content.get('text', '')[:100] + '...',
            'targets': len(results),
            'successful': len([r for r in results if r.get('success')])
        })
        
        return jsonify({
            'success': True,
            'results': results,
            'message': 'Posted successfully'
        })
    
    except Exception as e:
        logging.error(f"Error posting: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/scheduler/start', methods=['POST'])
def start_scheduler():
    """Start the automatic scheduler"""
    try:
        scheduler.start()
        return jsonify({'success': True, 'message': 'Scheduler started'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/scheduler/stop', methods=['POST'])
def stop_scheduler():
    """Stop the automatic scheduler"""
    try:
        scheduler.stop()
        return jsonify({'success': True, 'message': 'Scheduler stopped'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/scheduler/status')
def scheduler_status():
    """Get scheduler status"""
    return jsonify({
        'running': scheduler.is_running,
        'next_run': scheduler.get_next_run_time()
    })

@app.route('/api/history')
def get_history():
    """Get full posting history"""
    history = load_history()
    return jsonify(history)

@app.route('/api/test-whatsapp')
def test_whatsapp():
    """Test WhatsApp connection"""
    try:
        test_message = "🧪 Test message from Islamic Automation System\n\nConnection successful! ✅"
        if WHATSAPP_GROUPS:
            result = whatsapp_poster.send_to_group(WHATSAPP_GROUPS[0], test_message)
            return jsonify({
                'success': result,
                'message': 'Test message sent to first group'
            })
        else:
            return jsonify({'error': 'No groups configured'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    """Settings page"""
    if request.method == 'POST':
        # Handle settings update
        # This would update config.py or a separate settings file
        return redirect(url_for('index'))
    
    return render_template('settings.html', config={
        'groups': WHATSAPP_GROUPS,
        'channels': WHATSAPP_CHANNELS,
        'posting_times': POSTING_TIMES,
        'posts_per_day': POSTS_PER_DAY
    })

if __name__ == '__main__':
    print("="*50)
    print("🕌 Islamic WhatsApp Automation System")
    print("="*50)
    print(f"\n📱 Dashboard: http://localhost:5000")
    print(f"📊 Configured Groups: {len(WHATSAPP_GROUPS)}")
    print(f"📢 Configured Channels: {len(WHATSAPP_CHANNELS)}")
    print(f"📅 Daily Posts: {POSTS_PER_DAY}")
    print(f"⏰ Posting Times: {POSTING_TIMES}")
    print("\n" + "="*50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
