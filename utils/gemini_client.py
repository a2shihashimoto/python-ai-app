"""
Gemini API クライアントのユーティリティ（google-genai SDK v2.x）
"""

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def get_api_key() -> str:
    """APIキーを環境変数またはStreamlit secretsから取得する"""
    try:
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        pass
    return os.getenv("GEMINI_API_KEY", "")


def get_client() -> genai.Client:
    """Gemini クライアントを初期化して返す"""
    api_key = get_api_key()
    if not api_key:
        raise ValueError("GEMINI_API_KEY が設定されていません。")
    return genai.Client(api_key=api_key)


def generate_text(
    prompt: str,
    model_name: str = "gemini-2.0-flash",
    temperature: float = 0.7,
    max_output_tokens: int = 4096,
) -> str:
    """
    テキストを生成して返す（一括生成）

    Args:
        prompt: プロンプト文字列
        model_name: 使用するモデル名
        temperature: 生成の多様性（0.0〜1.0）
        max_output_tokens: 最大出力トークン数

    Returns:
        生成されたテキスト
    """
    client = get_client()
    response = client.models.generate_content(
        model=model_name,
        contents=types.Content(
            role="user",
            parts=[types.Part(text=prompt)],
        ),
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ),
    )
    return response.text


def stream_text(
    prompt: str,
    model_name: str = "gemini-2.0-flash",
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
    client = get_client()
    for chunk in client.models.generate_content_stream(
        model=model_name,
        contents=types.Content(
            role="user",
            parts=[types.Part(text=prompt)],
        ),
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ),
    ):
        if chunk.text:
            yield chunk.text


def check_api_key() -> bool:
    """APIキーが設定されているか確認する"""
    return bool(get_api_key())
