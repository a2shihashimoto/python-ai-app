"""
Gemini API クライアントのユーティリティ
"""

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def get_api_key() -> str:
    """APIキーを環境変数またはStreamlit secretsから取得する"""
    # Streamlit secrets を優先（本番環境向け）
    try:
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        pass
    # .env ファイルから取得
    api_key = os.getenv("GEMINI_API_KEY", "")
    return api_key


def get_model(model_name: str = "gemini-2.5-flash") -> genai.GenerativeModel:
    """Geminiモデルを初期化して返す"""
    api_key = get_api_key()
    if not api_key:
        raise ValueError("GEMINI_API_KEY が設定されていません。")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)


def generate_text(
    prompt: str,
    model_name: str = "gemini-2.5-flash",
    temperature: float = 0.7,
    max_output_tokens: int = 4096,
) -> str:
    """
    テキストを生成して返す

    Args:
        prompt: プロンプト文字列
        model_name: 使用するモデル名
        temperature: 生成の多様性（0.0〜1.0）
        max_output_tokens: 最大出力トークン数

    Returns:
        生成されたテキスト
    """
    model = get_model(model_name)
    generation_config = genai.types.GenerationConfig(
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text


def stream_text(
    prompt: str,
    model_name: str = "gemini-2.5-flash",
    temperature: float = 0.7,
    max_output_tokens: int = 4096,
):
    """
    テキストをストリーミングで生成する（Streamlit用）

    Args:
        prompt: プロンプト文字列
        model_name: 使用するモデル名
        temperature: 生成の多様性（0.0〜1.0）
        max_output_tokens: 最大出力トークン数

    Yields:
        生成されたテキストのチャンク
    """
    model = get_model(model_name)
    generation_config = genai.types.GenerationConfig(
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    response = model.generate_content(
        prompt,
        generation_config=generation_config,
        stream=True,
    )
    for chunk in response:
        if chunk.text:
            yield chunk.text


def check_api_key() -> bool:
    """APIキーが設定されているか確認する"""
    return bool(get_api_key())
