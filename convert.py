import csv
import json

data = []
with open('Từ vựng N3 - N3.tsv', 'r', encoding='utf-8') as f:
    # Use tab as delimiter
    reader = csv.reader(f, delimiter='\t')
    header = next(reader)
    for row in reader:
        # Check if the row has enough columns
        if len(row) >= 5:
            kanji = row[1].strip()
            hiragana = row[3].strip()
            meaning = row[4].strip()
            # If Kanji is empty but Hiragana is not, map it
            if not kanji and hiragana:
                kanji = hiragana
            
            if kanji and meaning:
                data.append({
                    "kanji": kanji,
                    "hiragana": hiragana,
                    "romaji": "",
                    "meaning": meaning
                })

with open('n3_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Generated {len(data)} words in n3_vocab.json")
