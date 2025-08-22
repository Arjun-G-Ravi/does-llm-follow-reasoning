import os
import json

def combine_json_files(input_dir, output_file):
    combined_data = []
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        combined_data.extend(data)
                    else:
                        combined_data.append(data)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON file: {filename}")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        json.dump(combined_data, out_f, ensure_ascii=False, indent=2)

# Example usage:
combine_json_files('/home/arjun/dev/does-llm-follow-reasoning/dataset', 'combined.json')