#!/usr/bin/env python3
"""
🎨 Text Visual Discord Bot
A powerful tool that transforms your text into stunning visual art and shares it on Discord!

Features:
- Multiple ASCII art fonts and styles
- Emoji and Unicode support
- Batch text processing
- Color-coded output
- Advanced Discord integration
- Command-line interface with arguments

Author: Your Name
Version: 2.0.0
"""

import requests
import json
import os
import sys
import argparse
import logging
from datetime import datetime
from typing import Optional, List, Dict
import pyfiglet
from art import text2art
import random
import time

class TextVisualBot:
    def __init__(self, webhook_url: Optional[str] = None, username: str = "🎨 Text Visual Bot"):
        self.webhook_url = webhook_url or os.getenv('DISCORD_WEBHOOK_URL')
        self.username = username
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'TextVisualBot/2.0.0',
            'Content-Type': 'application/json'
        })
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('text_visual_bot.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        if not self.webhook_url:
            raise ValueError("Discord webhook URL is required. Set DISCORD_WEBHOOK_URL environment variable or pass it to constructor.")
    
    def create_ascii_art(self, text: str, font: str = 'standard') -> Optional[str]:
        """Convert text to ASCII art using pyfiglet with enhanced error handling"""
        try:
            # Handle emojis and special characters
            clean_text = self._clean_text_for_ascii(text)
            ascii_art = pyfiglet.figlet_format(clean_text, font=font)
            return ascii_art
        except Exception as e:
            self.logger.error(f"Error creating ASCII art with font '{font}': {e}")
            # Try with a fallback font
            try:
                ascii_art = pyfiglet.figlet_format(text, font='standard')
                self.logger.info("Used fallback font 'standard'")
                return ascii_art
            except Exception as e2:
                self.logger.error(f"Fallback font also failed: {e2}")
                return None
    
    def create_art_text(self, text: str, font: str = 'block') -> Optional[str]:
        """Convert text to art using art library with enhanced features"""
        try:
            art_text = text2art(text, font=font)
            return art_text
        except Exception as e:
            self.logger.error(f"Error creating art text with font '{font}': {e}")
            return None
    
    def _clean_text_for_ascii(self, text: str) -> str:
        """Clean text for ASCII art generation"""
        # Replace common emojis with text equivalents
        emoji_replacements = {
            '😀': 'happy', '😊': 'smile', '❤️': 'heart', '🔥': 'fire',
            '💯': '100', '🎉': 'party', '🚀': 'rocket', '⭐': 'star',
            '💪': 'muscle', '🎨': 'art', '🎵': 'music', '🎮': 'game'
        }
        
        clean_text = text
        for emoji, replacement in emoji_replacements.items():
            clean_text = clean_text.replace(emoji, replacement)
        
        return clean_text
    
    def create_rainbow_text(self, text: str) -> str:
        """Create rainbow-colored text for Discord (using Discord's markdown)"""
        colors = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣']
        rainbow_text = ""
        for i, char in enumerate(text):
            if char != ' ':
                color = colors[i % len(colors)]
                rainbow_text += f"{color} {char} "
            else:
                rainbow_text += "  "
        return rainbow_text
    
    def create_glitch_text(self, text: str) -> str:
        """Create glitch-style text effect"""
        glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        glitch_text = ""
        for char in text:
            if random.random() < 0.1:  # 10% chance to glitch
                glitch_text += random.choice(glitch_chars)
            else:
                glitch_text += char
        return glitch_text
    
    def send_to_discord(self, content: str, username: Optional[str] = None, 
                       embed: bool = False, color: str = "random") -> bool:
        """Send message to Discord via webhook with enhanced features"""
        if not self.webhook_url:
            self.logger.error("No webhook URL configured")
            return False
        
        username = username or self.username
        
        # Handle message length limits
        if len(content) > 2000:
            content = content[:1990] + "\n... (truncated)"
        
        # Create payload
        payload = {
            "content": f"```\n{content}\n```",
            "username": username,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # Add embed if requested
        if embed:
            embed_color = self._get_color_code(color)
            payload["embeds"] = [{
                "title": "🎨 Visual Art Generated",
                "description": f"```\n{content}\n```",
                "color": embed_color,
                "timestamp": datetime.utcnow().isoformat(),
                "footer": {
                    "text": "Created by Text Visual Bot"
                }
            }]
            payload["content"] = None  # Remove content when using embed
        
        try:
            response = self.session.post(self.webhook_url, json=payload, timeout=10)
            if response.status_code == 204:
                self.logger.info("Message sent to Discord successfully!")
                return True
            else:
                self.logger.error(f"Failed to send message. Status code: {response.status_code}")
                self.logger.error(f"Response: {response.text}")
                return False
        except requests.exceptions.Timeout:
            self.logger.error("Request timed out")
            return False
        except Exception as e:
            self.logger.error(f"Error sending to Discord: {e}")
            return False
    
    def _get_color_code(self, color: str) -> int:
        """Get Discord color code"""
        colors = {
            "red": 0xFF0000,
            "green": 0x00FF00,
            "blue": 0x0000FF,
            "yellow": 0xFFFF00,
            "purple": 0x800080,
            "orange": 0xFFA500,
            "pink": 0xFFC0CB,
            "cyan": 0x00FFFF,
            "random": random.randint(0, 0xFFFFFF)
        }
        return colors.get(color.lower(), colors["random"])
    
    def process_text(self, text: str, visual_type: str = 'ascii', font: str = 'standard',
                    embed: bool = False, color: str = "random", effect: str = None) -> bool:
        """Process text and create visual representation with enhanced options"""
        self.logger.info(f"Processing text: '{text}' with type: {visual_type}, font: {font}")
        
        visual = None
        
        if visual_type == 'ascii':
            visual = self.create_ascii_art(text, font)
        elif visual_type == 'art':
            visual = self.create_art_text(text, font)
        elif visual_type == 'rainbow':
            visual = self.create_rainbow_text(text)
        elif visual_type == 'glitch':
            visual = self.create_glitch_text(text)
        else:
            self.logger.error(f"Unknown visual type: {visual_type}")
            return False
        
        if visual:
            print("🎨 Visual representation created:")
            print(visual)
            
            # Apply additional effects
            if effect == 'bold':
                visual = f"**{visual}**"
            elif effect == 'italic':
                visual = f"*{visual}*"
            
            # Send to Discord
            success = self.send_to_discord(visual, embed=embed, color=color)
            return success
        else:
            self.logger.error("Failed to create visual representation")
            return False
    
    def batch_process(self, texts: List[str], visual_type: str = 'ascii', 
                     font: str = 'standard', delay: float = 1.0) -> Dict[str, bool]:
        """Process multiple texts in batch"""
        results = {}
        self.logger.info(f"Starting batch processing of {len(texts)} texts")
        
        for i, text in enumerate(texts, 1):
            self.logger.info(f"Processing {i}/{len(texts)}: {text[:20]}...")
            success = self.process_text(text, visual_type, font)
            results[text] = success
            
            if i < len(texts) and delay > 0:
                time.sleep(delay)
        
        return results
    
    def interactive_mode(self):
        """Run the bot in interactive mode with enhanced features"""
        print("🎨" + "="*50)
        print("🎨 TEXT VISUAL DISCORD BOT v2.0")
        print("🎨" + "="*50)
        print("✨ Transform your text into stunning visual art!")
        print("📤 Automatically share on Discord via webhook")
        print()
        print("🎯 Available Commands:")
        print("  • Type 'quit' or 'exit' to stop")
        print("  • Type 'help' for detailed help")
        print("  • Type 'fonts' to see available fonts")
        print("  • Type 'effects' to see available effects")
        print()
        print("🎨 Visual Types: ascii, art, rainbow, glitch")
        print("🎭 Effects: bold, italic")
        print("🌈 Colors: red, green, blue, yellow, purple, orange, pink, cyan, random")
        print()
        
        while True:
            try:
                # Get user input
                text = input("🎨 Enter text to visualize: ").strip()
                
                if text.lower() in ['quit', 'exit', 'q']:
                    print("👋 Thanks for using Text Visual Bot! Goodbye!")
                    break
                
                if text.lower() == 'help':
                    self._show_help()
                    continue
                
                if text.lower() == 'fonts':
                    self._show_fonts()
                    continue
                
                if text.lower() == 'effects':
                    self._show_effects()
                    continue
                
                if not text:
                    print("❌ Please enter some text.")
                    continue
                
                # Get visual type
                visual_type = input("🎨 Visual type (ascii/art/rainbow/glitch) [ascii]: ").strip().lower()
                if not visual_type:
                    visual_type = 'ascii'
                
                # Get font (only for ascii/art)
                if visual_type in ['ascii', 'art']:
                    font = input("🎭 Font [standard]: ").strip().lower()
                    if not font:
                        font = 'standard'
                else:
                    font = 'standard'
                
                # Get embed option
                embed_input = input("📦 Use embed? (y/n) [n]: ").strip().lower()
                embed = embed_input in ['y', 'yes', '1', 'true']
                
                # Get color
                color = input("🌈 Color [random]: ").strip().lower()
                if not color:
                    color = 'random'
                
                # Get effect
                effect = input("✨ Effect (bold/italic/none) [none]: ").strip().lower()
                if effect == 'none':
                    effect = None
                
                # Process the text
                print("🚀 Processing...")
                success = self.process_text(text, visual_type, font, embed, color, effect)
                
                if success:
                    print("✅ Successfully sent to Discord!")
                else:
                    print("❌ Failed to send to Discord. Check logs for details.")
                
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Thanks for using Text Visual Bot! Goodbye!")
                break
            except Exception as e:
                self.logger.error(f"Error in interactive mode: {e}")
                print(f"❌ Error: {e}")
    
    def _show_help(self):
        """Show detailed help information"""
        print("\n📚 HELP - Text Visual Discord Bot")
        print("="*40)
        print("🎨 Visual Types:")
        print("  • ascii  - Traditional ASCII art (supports fonts)")
        print("  • art    - Artistic text representations")
        print("  • rainbow - Colorful emoji-based text")
        print("  • glitch - Glitch-style text with random characters")
        print()
        print("🎭 Popular Fonts:")
        print("  • standard, block, bubble, slant, digital")
        print("  • letters, alligator, dotmatrix, graffiti")
        print()
        print("🌈 Colors: red, green, blue, yellow, purple, orange, pink, cyan, random")
        print("✨ Effects: bold, italic")
        print()
    
    def _show_fonts(self):
        """Show available fonts"""
        print("\n🎭 AVAILABLE FONTS")
        print("="*30)
        fonts = [
            "standard", "slant", "block", "bubble", "digital", "letters",
            "alligator", "dotmatrix", "bubblehead", "graffiti", "isometric1"
        ]
        for i, font in enumerate(fonts, 1):
            print(f"  {i:2d}. {font}")
        print()
    
    def _show_effects(self):
        """Show available effects"""
        print("\n✨ AVAILABLE EFFECTS")
        print("="*25)
        print("  • bold   - Makes text bold in Discord")
        print("  • italic - Makes text italic in Discord")
        print("  • none   - No special formatting")
        print()

def main():
    """Main function with command-line argument support"""
    parser = argparse.ArgumentParser(
        description="🎨 Text Visual Discord Bot - Transform text into visual art and share on Discord",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Interactive mode
  %(prog)s -t "Hello World" -f block         # Quick ASCII art
  %(prog)s -t "Amazing" -v rainbow -e        # Rainbow text with embed
  %(prog)s -t "Glitch" -v glitch -c red      # Glitch effect with red color
  %(prog)s --batch file.txt                  # Process multiple texts from file
        """
    )
    
    parser.add_argument('-t', '--text', help='Text to visualize')
    parser.add_argument('-v', '--visual-type', choices=['ascii', 'art', 'rainbow', 'glitch'], 
                       default='ascii', help='Visual type (default: ascii)')
    parser.add_argument('-f', '--font', default='standard', 
                       help='Font for ASCII art (default: standard)')
    parser.add_argument('-c', '--color', default='random',
                       help='Color for Discord embed (default: random)')
    parser.add_argument('-e', '--embed', action='store_true',
                       help='Use Discord embed format')
    parser.add_argument('--effect', choices=['bold', 'italic'], 
                       help='Text effect')
    parser.add_argument('--batch', help='Process multiple texts from file (one per line)')
    parser.add_argument('--delay', type=float, default=1.0,
                       help='Delay between batch messages (default: 1.0s)')
    parser.add_argument('--webhook', help='Discord webhook URL (overrides env var)')
    parser.add_argument('--username', default='🎨 Text Visual Bot',
                       help='Discord bot username')
    parser.add_argument('--version', action='version', version='Text Visual Bot 2.0.0')
    
    args = parser.parse_args()
    
    # Get webhook URL
    webhook_url = args.webhook or os.getenv('DISCORD_WEBHOOK_URL')
    
    if not webhook_url:
        print("❌ Discord webhook URL not found!")
        print("Set DISCORD_WEBHOOK_URL environment variable or use --webhook argument")
        webhook_url = input("Enter your Discord webhook URL: ").strip()
        
        if not webhook_url:
            print("❌ No webhook URL provided. Exiting.")
            return 1
    
    try:
        bot = TextVisualBot(webhook_url, args.username)
        
        # Batch processing
        if args.batch:
            if not os.path.exists(args.batch):
                print(f"❌ File not found: {args.batch}")
                return 1
            
            with open(args.batch, 'r', encoding='utf-8') as f:
                texts = [line.strip() for line in f if line.strip()]
            
            if not texts:
                print("❌ No texts found in file")
                return 1
            
            print(f"🚀 Processing {len(texts)} texts from {args.batch}")
            results = bot.batch_process(texts, args.visual_type, args.font, args.delay)
            
            successful = sum(1 for success in results.values() if success)
            print(f"✅ Successfully processed {successful}/{len(texts)} texts")
            return 0 if successful == len(texts) else 1
        
        # Single text processing
        elif args.text:
            success = bot.process_text(
                args.text, args.visual_type, args.font, 
                args.embed, args.color, args.effect
            )
            return 0 if success else 1
        
        # Interactive mode
        else:
            bot.interactive_mode()
            return 0
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
