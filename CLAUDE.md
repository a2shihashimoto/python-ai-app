# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 起動コマンド

```bash
# アプリ起動（streamlit が PATH にない場合）
/Users/atsushi.hashimoto/Library/Python/3.9/bin/streamlit run app.py

# パッケージインストール
pip3 install -r requirements.txt
```

## アーキテクチャ

Streamlit のマルチページアプリ構成。`app.py` がホームページ兼エントリーポイント。`pages/` 配下のファイルがサイドバーに自動的にメニューとして追加される（ファイル名の番号順）。

### Gemini API の呼び出し

すべての AI 生成は `utils/gemini_client.py` を経由する。ページファイルから直接 `google.generativeai` をインポートしない。

- `stream_text()` — ストリーミング生成。`st.empty()` と組み合わせてリアルタイム表示する。ほとんどのページで使用。
- `generate_text()` — 一括生成。校正ページのように生成後に左右分割表示するケースで使用。

デフォルトモデルは `gemini-2.0-flash`。呼び出し時に `model_name` で変更可能。

### APIキーの解決順序

`get_api_key()` は以下の順で探す：
1. `st.secrets["GEMINI_API_KEY"]`（`.streamlit/secrets.toml`）
2. 環境変数 `GEMINI_API_KEY`（`.env` から `load_dotenv()` で読み込み）
3. `app.py` のサイドバー入力 → `os.environ["GEMINI_API_KEY"]` に直接セット

## 新しいページを追加するときのルール

1. ファイル名を `pages/NN_🔤_ページ名.py` の形式にする（`NN` で順序が決まる）
2. ファイル先頭で `st.set_page_config()` を呼ぶ（Streamlit の制約）
3. `check_api_key()` でキーを確認し、未設定なら `st.stop()` で処理を止める
4. 長い生成には `stream_text()` を使い、`st.empty()` で差分更新する
5. 生成結果の末尾に `st.expander` でコピー用 `st.text_area` を置く（既存ページのパターンを踏襲）

## 環境

- Python 3.9 (macOS システム Python)
- Streamlit 1.50.0、ポート 8501
- `google-generativeai` 0.8.x（`genai.GenerativeModel` ベースの旧 SDK スタイル）
