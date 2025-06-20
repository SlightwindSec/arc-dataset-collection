import os
import json
from tqdm import tqdm

input_root = 'data_100k'
output_path = 'a.jsonl'

json_files = []
for root, dirs, files in os.walk(input_root):
    for filename in files:
        if filename.endswith('.json'):
            json_files.append(os.path.join(root, filename))

with open(output_path, 'w', encoding='utf-8') as outfile:
    for file_path in tqdm(json_files, desc='Processing JSON files'):
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                data = json.load(infile)
                json_line = json.dumps(data, separators=(',', ':'))
                outfile.write(json_line + '\n')
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
