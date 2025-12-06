#!/usr/bin/env python3
"""
🚀 Quick Test Script for Text Visual Discord Bot
Simple script to test the bot functionality
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from text_visual_bot import TextVisualBot

def quick_test():
    """Quick test of the bot"""
    print("🚀 Quick Test - Text Visual Discord Bot")
    print("=" * 45)
    
    # Get webhook URL
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    if not webhook_url:
        print("❌ Please set DISCORD_WEBHOOK_URL environment variable")
        return False
    
    try:
        # Initialize bot
        bot = TextVisualBot(webhook_url, "🧪 Test Bot")
        
        # Test basic ASCII art
        print("📝 Testing ASCII art...")
        success = bot.process_text("Test", "ascii", "standard")
        
        if success:
            print("✅ Test passed! Check your Discord channel.")
            return True
        else:
            print("❌ Test failed!")
            return False
            
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

if __name__ == "__main__":
    success = quick_test()
    sys.exit(0 if success else 1)

