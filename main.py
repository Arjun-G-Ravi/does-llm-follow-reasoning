#!/usr/bin/env python3
# Minimal Ollama REPL with character-level streaming and optional reasoning tag injection.
import subprocess
import sys
import json
import os
import re

MODEL = "kaggle-gpt:latest"
SHOW_THINKING = True          # If True, we prepend a prompt instruction to show reasoning.
dataset_file = 'combined'
def clean_terminal_output(text):
    """Remove terminal control characters and spinner animations."""
    # Remove ANSI escape sequences
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', text)
    
    # Remove spinner characters and control sequences
    spinner_chars = ['⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠋', '⠏']
    for char in spinner_chars:
        text = text.replace(char, '')
    
    # Remove other control sequences
    text = re.sub(r'\[?\?25[lh]', '', text)  # cursor visibility
    text = re.sub(r'\[?\?2026[lh]', '', text)  # bracketed paste mode
    text = re.sub(r'\[1G', '', text)  # cursor to column 1
    text = re.sub(r'\[K', '', text)   # clear to end of line
    text = re.sub(r'\[2K', '', text)  # clear entire line
    
    # Clean up extra whitespace and newlines
    text = re.sub(r'\n\s*\n', '\n', text)  # multiple newlines
    text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)  # leading whitespace
    
    return text.strip()

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
    response = ""
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
            # Successfully decoded; add to response but don't print
            response += s
            buf.clear()
    finally:
        p.wait()

    if p.returncode != 0:
        print(f"\n[error] ollama exited with code {p.returncode}", file=sys.stderr)
    
    # Clean the response before returning
    return clean_terminal_output(response)

def process_dataset():
    print(f"Ollama model: {MODEL}")
    print("Processing dataset...")
    
    # Load JSON data
    with open(f"/home/arjun/dev/Kaggle-competitions/7-openai-gpt-oss/dataset/{dataset_file}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Prepare results list
    results = []
    json_file = "/home/arjun/dev/Kaggle-competitions/7-openai-gpt-oss/results.json"
        
    for i, entry in enumerate(data):
        print(f"Processing entry {i+1}/{len(data)}: {entry['question'][:50]}...")
        question = entry['question']
        wrong_reasoning = entry['wrong_reasoning']
        
        # Write wrong reasoning to modelfile
        with open("/home/arjun/dev/Kaggle-competitions/7-openai-gpt-oss/changing-model-file.txt", "w", encoding="utf-8") as f:
            f.write(f'''FROM /home/arjun/.ollama/models/blobs/sha256-b112e727c6f18875636c56a779790a590d705aec9e1c0eb5a97d51fc2a778583

TEMPLATE """<|start|>system<|message|>
You are ChatGPT from OpenAI.

Knowledge cutoff: 2024-06
Current date: {{ currentDate }}

Reasoning: medium

# Valid channels: analysis, commentary, final. Channel must be included for every message.
<|end|>
{{- range $i, $msg := .Messages }}
  {{- if eq $msg.Role "user" -}}
    <|start|>user<|message|>{{ $msg.Content }}<|end|>
  {{- else if eq $msg.Role "assistant" -}}
    {{- if gt (len $msg.Thinking) 0 -}}
      <|start|>assistant<|channel|>analysis<|message|>{{ $msg.Thinking }}<|end|>
    {{- end -}}
    {{- if gt (len $msg.Content) 0 -}}
      <|start|>assistant<|channel|>final<|message|>{{ $msg.Content }}<|end|>
    {{- end -}}
  {{- end }}
{{- end -}}
<|start|>assistant<|channel|>analysis<|message|>{wrong_reasoning}Now answer.<|end|>
"""

PARAMETER temperature 1''')
        
        os.system('ollama create kaggle-gpt -f /home/arjun/dev/Kaggle-competitions/7-openai-gpt-oss/changing-model-file.txt')
        # Get model answer (no terminal output during streaming)
        model_answer = stream(question)
        
        # Add to results
        result_entry = {
            "question": question,
            "wrong_reasoning": wrong_reasoning,
            "model_answer": model_answer
        }
        results.append(result_entry)
        
        # Save results after each entry (incremental save)
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"Completed entry {i+1}")
    
    print(f"\nProcessing complete. Results saved to {json_file}")

if __name__ == "__main__":
    process_dataset()