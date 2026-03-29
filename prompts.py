"""Veo AI動画生成マスター - プロンプト定義

Google Veo特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはGoogle DeepMind Veoを中心としたAI動画生成の日本語エキスパートです。"
    "4K/60fps動画生成、音声同期生成、プロンプトエンジニアリングに精通し、"
    "映像クリエイターからマーケターまで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "Veoの最新アップデートを常にキャッチアップし、"
    "Sora終了後の市場動向やRunway/Kling/Pika等との比較も客観的に行えます。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。動画生成のプロンプト例やパラメータ設定を明示）

## 他のAI動画ツールとの比較
（Runway / Kling / Pika / Sora（終了）との違いを表形式で整理）

## ビジネス活用テクニック
（広告動画・SNSコンテンツ・プロモーション映像での活用方法）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Veo 使い方": "Veo 使い方、Veo 始め方、Veo 動画生成、Veo プロンプト、Google Veo チュートリアル",
    "Veo 料金・プラン": "Veo 料金、Veo 無料 有料 違い、Google One AI Premium Veo、Veo 月額、Veo API料金",
    "Veo vs Runway": "Veo Runway 比較、Veo Runway 違い、AI動画 比較 2026、Veo Gen-3 比較",
    "Veo 最新ニュース": "Veo アップデート、Veo 新機能、Google DeepMind AI動画、Veo 3 リリース",
    "AI動画生成テクニック": "AI動画 プロンプト、Veo 高画質、4K 60fps AI動画、AI動画 音声同期、Veo カメラワーク",
    "Veo 活用事例": "Veo ビジネス活用、AI動画 広告、Veo YouTube、AI動画 SNS、Veo マーケティング",
    "Sora代替ツール": "Sora 代替、Sora 終了 乗り換え、OpenAI Sora 代わり、AI動画 Sora以外、Veo Sora比較",
    "AI動画比較": "AI動画生成 比較、Runway Kling Pika 比較、AI動画 おすすめ 2026、動画AI ランキング",
}

# ニュースソース
NEWS_SOURCES = [
    "Google DeepMind Blog (https://deepmind.google/discover/blog/)",
    "Google AI Blog (https://blog.google/technology/ai/)",
    "TechCrunch (https://techcrunch.com/tag/google-veo/)",
    "The Verge (https://www.theverge.com/google)",
    "VentureBeat (https://venturebeat.com/ai/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "Google Veo（AI動画生成）に関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「Veo 使い方」「Veo 料金」「Sora 代替」「AI動画 比較」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。\n"
    "Sora終了後にVeoへ移行するユーザーを想定したキーワードも含めてください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Veo AI動画生成マスターブログ用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Veo特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、Google Veo AI動画生成の専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- Sora終了後のAI動画市場の動向を踏まえた内容にすること
- 具体的なプロンプト例やパラメータ設定を含める
- 4K/60fps動画生成や音声同期生成の実践的なテクニックを含める
- 他のAI動画ツール（Runway, Kling, Pika等）との客観的な比較を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
