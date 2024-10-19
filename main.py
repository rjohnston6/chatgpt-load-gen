#!/usr/bin/env python3
# www.github.com/pl247/ai-toolkit

import time
import logging

import click
from openai import OpenAI
from rich import print
from rich.logging import RichHandler

openai_api_key = "LLM"
openai_api_base = "http://64.101.169.102:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

chat_response = client.chat.completions.create(
    model="/ai/models/Meta-Llama-3-8B-Instruct/",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "write me an approx 500 word poem about a pirate"},
    ],
)
print("Chat response:", chat_response)
