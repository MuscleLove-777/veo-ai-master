"""Veo AI動画生成マスター - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Veo AI動画生成マスター"
BLOG_DESCRIPTION = "Google DeepMind Veoの使い方・最新情報・Sora代替比較を毎日更新。4K/60fps AI動画生成の最前線を解説。"
BLOG_URL = "https://musclelove-777.github.io/veo-ai-master"
BLOG_TAGLINE = "Google Veoで始めるAI動画生成の日本語完全ガイド"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/veo-ai-master"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Veo 使い方",
    "Veo 料金・プラン",
    "Veo vs Runway",
    "Veo 最新ニュース",
    "AI動画生成テクニック",
    "Veo 活用事例",
    "Sora代替ツール",
    "AI動画比較",
]

THEME = {
    "primary": "#ea4335",
    "accent": "#fbbc04",
    "gradient_start": "#ea4335",
    "gradient_end": "#fbbc04",
    "dark_bg": "#1a0a0a",
    "dark_surface": "#2d1515",
    "light_bg": "#fff5f5",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [12]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Google One AI Premium": [
        {"service": "Google One AI Premium", "url": "https://one.google.com", "description": "Google One AI Premiumプランに登録"},
    ],
    "YouTube Premium": [
        {"service": "YouTube Premium", "url": "https://www.youtube.com/premium", "description": "YouTube Premiumに登録する"},
    ],
    "動画編集ソフト": [
        {"service": "Adobe Creative Cloud", "url": "https://www.adobe.com/jp/creativecloud.html", "description": "Adobe Creative Cloudを始める"},
        {"service": "DaVinci Resolve", "url": "https://www.blackmagicdesign.com/jp/products/davinciresolve", "description": "DaVinci Resolveを試す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI動画講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI動画生成関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI動画生成関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8094

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
