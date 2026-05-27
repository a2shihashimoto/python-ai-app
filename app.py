"""
AI ライティングツール - ホームページ
"""

import streamlit as st
from utils.gemini_client import check_api_key

# ページ設定
st.set_page_config(
    page_title="AI ライティングツール",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# カスタムCSS
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    /* ===== クリッカブルツールカード ===== */
    /* page_link をカード風にスタイリング */
    a[data-testid="stPageLink-NavLink"] {
        display: block !important;
        background: #f8f9fa !important;
        border-radius: 12px 12px 0 0 !important;
        padding: 1rem 1.2rem 0.7rem 1.2rem !important;
        border-left: 4px solid #1f77b4 !important;
        color: #262730 !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        text-decoration: none !important;
        transition: background 0.2s, color 0.2s !important;
        margin-bottom: 0 !important;
    }
    a[data-testid="stPageLink-NavLink"]:hover {
        background: #e8f0fe !important;
        color: #1f77b4 !important;
        text-decoration: none !important;
    }
    /* カード説明文（page_link の直下） */
    .tool-card-desc {
        background: #f8f9fa;
        border-radius: 0 0 12px 12px;
        padding: 0.4rem 1.2rem 1rem 1.2rem;
        border-left: 4px solid #1f77b4;
        color: #555;
        font-size: 0.9rem;
        margin-top: -4px;
        margin-bottom: 1rem;
    }
    .api-warning {
        background: #fff3cd;
        border: 1px solid #ffc107;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1.5rem;
    }
    .api-ok {
        background: #d4edda;
        border: 1px solid #28a745;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# タイトル
st.markdown('<div class="main-title">✍️ AI ライティングツール</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Gemini AI を使った個人用ライティング支援ツール</div>',
    unsafe_allow_html=True,
)

# APIキー確認
if not check_api_key():
    st.markdown(
        """
        <div class="api-warning">
        ⚠️ <strong>Gemini API キーが設定されていません</strong><br>
        サイドバーの「⚙️ API設定」からキーを入力するか、
        プロジェクトルートに <code>.env</code> ファイルを作成して
        <code>GEMINI_API_KEY=your_key</code> を設定してください。
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<div class="api-ok">✅ <strong>API キーが設定済みです。</strong> 左のメニューからツールを選んでください。</div>',
        unsafe_allow_html=True,
    )

st.divider()

# ツール一覧
st.subheader("🛠️ 利用できるツール")

tools = [
    {
        "emoji": "📝",
        "name": "ブログ記事執筆",
        "desc": "テーマ・ターゲット・文字数を指定してブログ記事を自動生成します。SEO向けの見出し構成も考慮します。",
        "page": "pages/01_📝_ブログ記事執筆.py",
    },
    {
        "emoji": "📧",
        "name": "メール返信",
        "desc": "受信したメール文を貼り付けると、適切なトーンで返信文を生成します。ビジネス・カジュアル対応。",
        "page": "pages/02_📧_メール返信.py",
    },
    {
        "emoji": "📄",
        "name": "文章要約",
        "desc": "長い文章を指定した文字数・形式（箇条書き/段落）で簡潔に要約します。",
        "page": "pages/03_📄_文章要約.py",
    },
    {
        "emoji": "✏️",
        "name": "文章校正",
        "desc": "誤字脱字のチェックと文章表現の改善提案を行います。修正箇所を分かりやすく表示します。",
        "page": "pages/04_✏️_文章校正.py",
    },
    {
        "emoji": "📱",
        "name": "SNS投稿文生成",
        "desc": "X（Twitter）・Instagram向けに最適化された投稿文とハッシュタグを生成します。",
        "page": "pages/05_📱_SNS投稿文生成.py",
    },
    {
        "emoji": "🏷️",
        "name": "タイトル・キャッチコピー生成",
        "desc": "記事・動画・商品のタイトルやキャッチコピーを複数パターン提案します。",
        "page": "pages/06_🏷️_タイトル生成.py",
    },
    {
        "emoji": "🔄",
        "name": "文体変換",
        "desc": "文章のトーンをフォーマル・カジュアル・丁寧・簡潔など自由に変換します。",
        "page": "pages/07_🔄_文体変換.py",
    },
]

# 2列レイアウトでカード表示（クリッカブル）
col1, col2 = st.columns(2)
for i, tool in enumerate(tools):
    with col1 if i % 2 == 0 else col2:
        # タイトル部分：st.page_link でクリッカブルカード
        st.page_link(
            tool["page"],
            label=f"{tool['emoji']} {tool['name']}",
            use_container_width=True,
        )
        # 説明文：カード下半分として CSS で連結
        st.markdown(
            f'<div class="tool-card-desc">{tool["desc"]}</div>',
            unsafe_allow_html=True,
        )

st.divider()

# サイドバー：APIキー設定
with st.sidebar:
    st.header("⚙️ API設定")
    api_key_input = st.text_input(
        "Gemini API キー",
        type="password",
        help="Google AI Studio (https://aistudio.google.com/app/apikey) で取得できます",
        placeholder="AIza...",
    )
    if api_key_input:
        import os
        os.environ["GEMINI_API_KEY"] = api_key_input
        st.success("✅ APIキーを設定しました")

    st.divider()
    st.markdown(
        """
        ### 📖 使い方
        1. **APIキー**を上に入力
        2. 左メニューから**ツール**を選択
        3. 必要事項を入力して**生成**ボタンをクリック

        ---
        ### 🔑 APIキー取得
        [Google AI Studio](https://aistudio.google.com/app/apikey)
        から無料で取得できます。
        """
    )

# フッター
st.markdown(
    """
    <div style="text-align:center; color:#999; font-size:0.8rem; margin-top:2rem;">
    Powered by Google Gemini API ✨
    </div>
    """,
    unsafe_allow_html=True,
)
