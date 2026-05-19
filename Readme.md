# 🔊 Accent Pronunciator

A web app that lets you hear any word or phrase spoken in different English accents using neural text-to-speech.

## Accents Supported
- 🇺🇸 US English
- 🇬🇧 UK English
- 🇮🇳 Indian English

## Features
- Works for any word — names, startups, slang, technical terms
- IPA phonetic transcription shown for every word
- Powered by ElevenLabs neural TTS

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **TTS API:** ElevenLabs

## Project Structure
```
PRONUNCIATION_SITE/
├── accent_app/
│   ├── backend/
│   │   └── main.py
│   └── frontend/
│       └── index.html
├── .env          ← not committed, contains API key
├── .gitignore
└── requirements.txt
```

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/pronunciation-site.git
cd pronunciation-site
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API key
Create a `.env` file in the root:
```
ELEVENLABS_API_KEY=your-key-here
```

### 4. Start the backend
```bash
cd accent_app/backend
uvicorn main:app --reload
```

### 5. Open the frontend
Open `accent_app/frontend/index.html` in your browser.

## Coming Soon
- [ ] Download audio as MP3
- [ ] Syllable breakdown
- [ ] Deploy to Vercel + Render