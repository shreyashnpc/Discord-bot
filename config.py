"""
Configuration file for Text Visual Discord Bot
"""

import os

# Discord Webhook Configuration
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')

# Bot Configuration
BOT_USERNAME = "Text Visual Bot"
DEFAULT_FONT = "standard"
DEFAULT_VISUAL_TYPE = "ascii"

# Available fonts for ASCII art
AVAILABLE_FONTS = [
    "standard", "slant", "block", "bubble", "digital", "letters", 
    "alligator", "dotmatrix", "bubblehead", "graffiti", "isometric1",
    "letters", "alligator2", "dotmatrix", "bubblehead", "graffiti"
]

# Available visual types
VISUAL_TYPES = ["ascii", "art"]

# Discord message settings
MAX_MESSAGE_LENGTH = 2000  # Discord's message limit
CODE_BLOCK_PADDING = 4     # Extra characters for code block formatting

