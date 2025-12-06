<div align="center">

# 🎨 Text Visual Discord Bot

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Webhook-7289DA.svg)](https://discord.com)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange.svg)](https://github.com/yourusername/text-visual-bot)

**Transform your text into stunning visual art and share it on Discord!**

[🚀 Quick Start](#-quick-start) • [📖 Features](#-features) • [🎯 Usage](#-usage) • [⚙️ Installation](#️-installation) • [📚 Documentation](#-documentation)

</div>

---

## ✨ Features

🎨 **Multiple Visual Types**
- ASCII Art with 15+ fonts
- Artistic text representations  
- Rainbow emoji text
- Glitch-style effects

🚀 **Advanced Discord Integration**
- Rich embeds with custom colors
- Batch processing support
- Automatic message formatting
- Error handling & logging

💻 **Powerful CLI Interface**
- Interactive mode with emojis
- Command-line arguments
- Batch file processing
- Real-time feedback

🎭 **Creative Effects**
- Bold & italic formatting
- Custom color schemes
- Emoji support
- Special character handling

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/text-visual-bot.git
cd text-visual-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up Discord webhook (see Installation section)

# 4. Run the bot
python text_visual_bot.py
```

## ⚙️ Installation

### Prerequisites
- 🐍 Python 3.7 or higher
- 💬 Discord server with webhook permissions
- 🌐 Internet connection

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/text-visual-bot.git
cd text-visual-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Discord Webhook Setup
1. Go to your Discord server
2. Right-click on the target channel → **Edit Channel**
3. Navigate to **Integrations** → **Webhooks**
4. Click **Create Webhook**
5. Copy the webhook URL

### Step 4: Configuration

**Option A: Environment Variable (Recommended)**
```bash
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

**Option B: Command Line**
```bash
python text_visual_bot.py --webhook "YOUR_WEBHOOK_URL"
```

**Option C: Interactive Setup**
The bot will prompt you for the webhook URL on first run.

## 🎯 Usage

### Interactive Mode
```bash
python text_visual_bot.py
```

**Example Session:**
```
🎨==================================================
🎨 TEXT VISUAL DISCORD BOT v2.0
🎨==================================================
✨ Transform your text into stunning visual art!
📤 Automatically share on Discord via webhook

🎨 Enter text to visualize: Hello World
🎨 Visual type (ascii/art/rainbow/glitch) [ascii]: ascii
🎭 Font [standard]: block
📦 Use embed? (y/n) [n]: y
🌈 Color [random]: blue
✨ Effect (bold/italic/none) [none]: none
🚀 Processing...
🎨 Visual representation created:
██████╗ ███████╗██╗     ██╗      ██████╗     ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ 
██╔══██╗██╔════╝██║     ██║     ██╔═══██╗    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗
██████╔╝█████╗  ██║     ██║     ██║   ██║    ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║
██╔══██╗██╔══╝  ██║     ██║     ██║   ██║    ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ 
✅ Successfully sent to Discord!
```

### Command Line Usage

**Quick ASCII Art:**
```bash
python text_visual_bot.py -t "Hello World" -f block
```

**Rainbow Text with Embed:**
```bash
python text_visual_bot.py -t "Amazing" -v rainbow -e -c purple
```

**Glitch Effect:**
```bash
python text_visual_bot.py -t "Glitch" -v glitch -c red
```

**Batch Processing:**
```bash
python text_visual_bot.py --batch texts.txt --delay 2.0
```

## 📚 Documentation

### 🎭 Available Fonts
| Font | Description | Example |
|------|-------------|---------|
| `standard` | Classic ASCII art | `Hello` |
| `block` | Bold block letters | `HELLO` |
| `bubble` | Rounded bubble style | `Hello` |
| `slant` | Slanted italic style | `Hello` |
| `digital` | Computer/digital style | `HELLO` |
| `letters` | Letter-based art | `Hello` |
| `alligator` | Alligator teeth style | `HELLO` |
| `dotmatrix` | Dot matrix printer style | `HELLO` |
| `graffiti` | Street graffiti style | `Hello` |
| `isometric1` | 3D isometric style | `HELLO` |

### 🎨 Visual Types

| Type | Description | Best For |
|------|-------------|----------|
| `ascii` | Traditional ASCII art with fonts | Headers, titles |
| `art` | Artistic text representations | Decorative text |
| `rainbow` | Colorful emoji-based text | Fun messages |
| `glitch` | Glitch-style with random chars | Cyberpunk themes |

### 🌈 Color Options
- `red`, `green`, `blue`, `yellow`
- `purple`, `orange`, `pink`, `cyan`
- `random` - Random color each time

### ✨ Text Effects
- `bold` - **Bold formatting**
- `italic` - *Italic formatting*
- `none` - No special formatting

## 🛠️ Configuration

Customize your bot by editing `config.py`:

```python
# Bot settings
BOT_USERNAME = "🎨 Your Custom Bot"
DEFAULT_FONT = "block"
DEFAULT_VISUAL_TYPE = "ascii"

# Discord settings
MAX_MESSAGE_LENGTH = 2000
CODE_BLOCK_PADDING = 4
```

## 🐛 Troubleshooting

### Common Issues

<details>
<summary><strong>❌ "No webhook URL configured"</strong></summary>

**Solution:**
```bash
# Set environment variable
export DISCORD_WEBHOOK_URL="your_webhook_url"

# Or use command line
python text_visual_bot.py --webhook "your_webhook_url"
```
</details>

<details>
<summary><strong>❌ "Failed to send message"</strong></summary>

**Solutions:**
- ✅ Verify webhook URL is correct
- ✅ Check Discord server permissions
- ✅ Ensure internet connection
- ✅ Try with shorter text
</details>

<details>
<summary><strong>❌ "Error creating ASCII art"</strong></summary>

**Solutions:**
- ✅ Try different font: `-f standard`
- ✅ Use simpler text without special characters
- ✅ Check text length (keep under 20 characters for best results)
</details>

<details>
<summary><strong>❌ Import errors</strong></summary>

**Solution:**
```bash
pip install -r requirements.txt
```
</details>

## 📁 Project Structure

```
text-visual-bot/
├── 🎨 text_visual_bot.py    # Main bot script
├── ⚙️ config.py             # Configuration settings  
├── 📦 requirements.txt      # Python dependencies
├── 📖 README.md            # Documentation
├── 📝 text_visual_bot.log  # Log file (auto-generated)
└── 📄 examples/            # Example files
    ├── sample_texts.txt    # Sample texts for batch processing
    └── demo.py            # Demo script
```

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | ≥2.31.0 | Discord webhook HTTP requests |
| `pyfiglet` | ≥0.8.1 | ASCII art generation |
| `art` | ≥5.8 | Additional text art styles |

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)
5. 🔄 **Open** a Pull Request

### 🎯 Areas for Contribution
- 🎨 New visual effects and fonts
- 🐛 Bug fixes and improvements
- 📚 Documentation enhancements
- 🧪 Test coverage
- 🌐 Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [pyfiglet](https://github.com/pwaller/pyfiglet) for ASCII art generation
- [art](https://github.com/sepandhaghighi/art) for additional text art
- [Discord](https://discord.com) for the amazing platform

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[🐛 Report Bug](https://github.com/yourusername/text-visual-bot/issues) • [💡 Request Feature](https://github.com/yourusername/text-visual-bot/issues) • [📖 Documentation](https://github.com/yourusername/text-visual-bot/wiki)

Made with ❤️ by [Your Name](https://github.com/yourusername)

</div>
# Discord-bot
