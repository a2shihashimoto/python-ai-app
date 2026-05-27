# 🧑‍💻 `app.py` を読み解く — Streamlitアプリのホームページはこう作る

---

## 📌 このファイルの役割

`app.py` はアプリの **玄関ページ**です。
ツール一覧を表示し、APIキーを設定するサイドバーを持っています。

---

## 1️⃣ ページ全体の設定

```python
st.set_page_config(
    page_title="AI ライティングツール",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)
```

ブラウザのタブに表示されるタイトルやアイコン、レイアウトをここで決めます。
**必ずファイルの先頭で呼ばないといけない**というStreamlitのルールがあります。

---

## 2️⃣ カスタムCSS でデザインを整える

```python
st.markdown("""
    <style>
    .tool-card {
        background: #f8f9fa;
        border-radius: 12px;
        ...
    }
    </style>
""", unsafe_allow_html=True)
```

Streamlit は標準でも見た目を整えられますが、細かいデザインは **HTMLとCSSを直接埋め込む**ことで実現しています。
`unsafe_allow_html=True` をつけないと、HTMLがそのまま文字として表示されてしまいます。

---

## 3️⃣ APIキーが設定されているか確認する

```python
if not check_api_key():
    # ⚠️ 警告を表示
else:
    # ✅ OKメッセージを表示
```

`utils/gemini_client.py` の `check_api_key()` を呼んで、キーが存在するかを確認します。
**未設定でもアプリは止まらず**、警告バナーを表示するだけにしています（ホームページなので）。
※ 各ツールページでは未設定なら `st.stop()` で処理を止めています。

---

## 4️⃣ ツールカードを2列で並べる

```python
col1, col2 = st.columns(2)

for i, tool in enumerate(tools):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f'<div class="tool-card">...</div>', unsafe_allow_html=True)
```

`st.columns(2)` で画面を左右2列に分割しています。
`i % 2 == 0`（偶数番目）なら左列、奇数番目なら右列に置くことで、
リストを自動的に **2列のカードレイアウト** にしています。

---

## 5️⃣ サイドバーでAPIキーを受け取る

```python
with st.sidebar:
    api_key_input = st.text_input("Gemini API キー", type="password")
    if api_key_input:
        os.environ["GEMINI_API_KEY"] = api_key_input
```

`with st.sidebar:` の中に書いたUIは、すべてサイドバーに表示されます。
`type="password"` で入力内容が `●●●` にマスクされます。
入力されたら `os.environ` に直接セットすることで、`.env` なしでもAPIキーが使えるようになります。

---

## 🗺️ 全体の流れ まとめ

```
app.py 起動
  ↓
ページ設定（タイトル・レイアウト）
  ↓
CSSでデザイン適用
  ↓
APIキーの有無を確認 → バナー表示
  ↓
ツール一覧を2列カードで表示
  ↓
サイドバー：APIキー入力を受け付ける
```

---

## 💡 Streamlitの基本ルール（このコードから学べること）

| ルール | 内容 |
|------|------|
| `set_page_config` は先頭 | 他のst.〇〇より前に書く |
| `st.columns()` で横並び | 数字で列数を指定 |
| `with st.sidebar:` でサイドバー | インデント内がサイドバーに入る |
| HTML埋め込みは `unsafe_allow_html=True` | 細かいデザインに使う |
| `os.environ` でAPIキーを動的にセット | .envなしでも動くようにする工夫 |
