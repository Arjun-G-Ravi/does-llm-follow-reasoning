#!/usr/bin/env python3
# Minimal Ollama REPL with character-level streaming and optional reasoning tag injection.

import subprocess
import sys
import json

MODEL = "kaggle-gpt:latest"
SHOW_THINKING = True          # If True, we prepend a prompt instruction to show reasoning.

def stream(prompt: str, model: str = MODEL):

    # Use unbuffered binary stdout (bufsize=0) so we can print tokens as they come.
    p = subprocess.Popen(
        ["ollama", "run", model, prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=0,          # unbuffered
        text=False          # get raw bytes
    )

    decoder = sys.stdout.encoding or "utf-8"
    try:
        buf = bytearray()
        while True:
            chunk = p.stdout.read(1)  # read single byte
            if not chunk:
                break
            buf += chunk
            # Try to decode what we have; if it fails (incomplete multibyte), wait for more.
            try:
                s = buf.decode(decoder)
            except UnicodeDecodeError:
                continue
            # Successfully decoded; print and clear buffer.
            print(s, end="", flush=True)
            buf.clear()
    finally:
        p.wait()

    if p.returncode != 0:
        print(f"\n[error] ollama exited with code {p.returncode}", file=sys.stderr)

def repl():
    print(f"Ollama model: {MODEL}")
    print("Type prompt (empty line / quit / exit to stop).")
    while True:
        try:
            prompt = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        prompt = prompt.strip()
        if not prompt or prompt.lower() in {"quit", "exit"}:
            break
        stream(prompt)
        print()  # newline after each response

if __name__ == "__main__":
    repl()