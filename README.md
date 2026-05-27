# ✍️ AI ライティングツール

Gemini API を使った個人用 AI ライティング支援ツールです。

## 🛠️ 機能一覧

| ページ | 機能 |
|-------|------|
| 📝 ブログ記事執筆 | テーマ・ターゲット・文字数を指定してブログ記事を自動生成 |
| 📧 メール返信 | 受信メールを貼り付けると返信文を生成 |
| 📄 文章要約 | 長文を指定した長さ・形式で要約 |
| ✏️ 文章校正 | 誤字脱字チェックと文章表現の改善提案 |
| 📱 SNS投稿文生成 | X・Instagram向け投稿文とハッシュタグを生成 |
| 🏷️ タイトル・キャッチコピー生成 | タイトルやキャッチコピーを複数パターン提案 |
| 🔄 文体変換 | フォーマル・カジュアル・丁寧などに文体を変換 |

## 🚀 セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. API キーの設定

`.env.example` をコピーして `.env` ファイルを作成します：

```bash
cp .env.example .env
```

`.env` ファイルを編集して API キーを設定します：

```
GEMINI_API_KEY=your_api_key_here
```

> API キーは [Google AI Studio](https://aistudio.google.com/app/apikey) から無料で取得できます。

### 3. アプリの起動

```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` が自動的に開きます。

## 📁 ファイル構成

```
python-ai-app/
├── app.py                      # ホームページ
├── requirements.txt            # 依存パッケージ
├── .env                        # API キー（要作成）
├── .env.example                # .env のサンプル
├── .streamlit/
│   └── config.toml             # Streamlit 設定
├── utils/
│   └── gemini_client.py        # Gemini API クライアント
└── pages/
    ├── 01_📝_ブログ記事執筆.py
    ├── 02_📧_メール返信.py
    ├── 03_📄_文章要約.py
    ├── 04_✏️_文章校正.py
    ├── 05_📱_SNS投稿文生成.py
    ├── 06_🏷️_タイトル生成.py
    └── 07_🔄_文体変換.py
```

## 💡 使い方

1. アプリを起動してホームページを開く
2. サイドバーの「⚙️ API設定」に Gemini API キーを入力（`.env` で設定済みの場合は不要）
3. 左のサイドバーから使いたいツールを選択
4. 各ページのフォームに内容を入力して生成ボタンをクリック
