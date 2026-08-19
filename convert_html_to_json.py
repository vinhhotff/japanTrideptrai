
import json
import re

def clean(text):
    return re.sub(r'<[^>]+>', '', text).strip()

def parse_lln(html):
    rows = re.findall(r'<tr>(.*?)</tr>', html, re.DOTALL)
    results = []
    for row in rows:
        tds = re.findall(r'<td>(.*?)</td>', row, re.DOTALL)
        if len(tds) < 2: continue
        
        jap_side, viet_side = tds[0], tds[1]
        
        # Sentence: all dc-orig spans
        sentence = "".join([clean(p) for p in re.findall(r'class="[^"]*dc-orig[^"]*">(.*?)</span>', jap_side, re.DOTALL)])
        translation = clean(viet_side)
        
        # Word & Reading: find the one inside dc-gap
        word, reading = "", ""
        gap_pos = jap_side.find('class="dc-gap"')
        if gap_pos != -1:
            # Look for the next dc-romaji and dc-orig AFTER the gap start
            rest = jap_side[gap_pos:]
            # Romaji
            r_match = re.search(r'class="[^"]*dc-romaji[^"]*">(.*?)</span>', rest, re.DOTALL)
            if r_match: reading = clean(r_match.group(1))
            # Word
            w_match = re.search(r'class="[^"]*dc-orig[^"]*">(.*?)</span>', rest, re.DOTALL)
            if w_match: word = clean(w_match.group(1))
            
        if not word: word = sentence
        
        results.append({
            "word": word,
            "reading": reading,
            "context": sentence,
            "translation": translation
        })
    return results

def main():
    with open("/Users/thanvinh/Desktop/thư mục không có tiêu đề/lln_print_items_2026-3-11_732091.html", "r") as f:
        data = parse_lln(f.read())
    with open("/Users/thanvinh/Desktop/thư mục không có tiêu đề/lln_items_final.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Done: {len(data)} items")

if __name__ == "__main__":
    main()
