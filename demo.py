#!/usr/bin/env python3
"""
🎨 Text Visual Discord Bot - Demo Script
Demonstrates various features and capabilities of the bot
"""

import sys
import os
import time

# Add parent directory to path to import the bot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from text_visual_bot import TextVisualBot

def demo_ascii_art(bot):
    """Demonstrate ASCII art generation"""
    print("🎨 Demo: ASCII Art Generation")
    print("=" * 40)
    
    texts = ["Hello", "Python", "Discord"]
    fonts = ["standard", "block", "bubble"]
    
    for text, font in zip(texts, fonts):
        print(f"\n📝 Text: '{text}' with font: {font}")
        success = bot.process_text(text, "ascii", font, embed=True, color="blue")
        if success:
            print("✅ Success!")
        else:
            print("❌ Failed!")
        time.sleep(2)

def demo_rainbow_text(bot):
    """Demonstrate rainbow text"""
    print("\n🌈 Demo: Rainbow Text")
    print("=" * 30)
    
    text = "Rainbow Magic"
    print(f"📝 Text: '{text}'")
    success = bot.process_text(text, "rainbow", embed=True, color="purple")
    if success:
        print("✅ Success!")
    else:
        print("❌ Failed!")

def demo_glitch_effect(bot):
    """Demonstrate glitch effect"""
    print("\n⚡ Demo: Glitch Effect")
    print("=" * 30)
    
    text = "Glitch Mode"
    print(f"📝 Text: '{text}'")
    success = bot.process_text(text, "glitch", embed=True, color="red")
    if success:
        print("✅ Success!")
    else:
        print("❌ Failed!")

def demo_batch_processing(bot):
    """Demonstrate batch processing"""
    print("\n📦 Demo: Batch Processing")
    print("=" * 35)
    
    texts = ["Batch", "Processing", "Demo"]
    print(f"📝 Processing {len(texts)} texts...")
    
    results = bot.batch_process(texts, "ascii", "standard", delay=1.5)
    
    successful = sum(1 for success in results.values() if success)
    print(f"✅ Successfully processed {successful}/{len(texts)} texts")

def main():
    """Main demo function"""
    print("🎨" + "="*50)
    print("🎨 TEXT VISUAL DISCORD BOT - DEMO")
    print("🎨" + "="*50)
    print("This demo will showcase various features of the bot.")
    print("Make sure you have set up your Discord webhook URL!")
    print()
    
    # Get webhook URL
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    if not webhook_url:
        print("❌ Discord webhook URL not found in environment variables.")
        webhook_url = input("Enter your Discord webhook URL: ").strip()
        
        if not webhook_url:
            print("❌ No webhook URL provided. Exiting demo.")
            return
    
    try:
        # Initialize bot
        bot = TextVisualBot(webhook_url, "🎨 Demo Bot")
        print("✅ Bot initialized successfully!")
        print()
        
        # Run demos
        demo_ascii_art(bot)
        demo_rainbow_text(bot)
        demo_glitch_effect(bot)
        demo_batch_processing(bot)
        
        print("\n🎉 Demo completed!")
        print("Check your Discord channel to see the results!")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")

if __name__ == "__main__":
    main()

