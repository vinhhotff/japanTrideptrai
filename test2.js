const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const match = content.match(/const romajiMap = \[([\s\S]*?)\];/);
const mapCode = '[' + match[1] + ']';
const romajiMap = eval(mapCode);

function romajiToHiragana(str) {
    let s = str.toLowerCase().trim();
    let result = '';
    let i = 0;
    while (i < s.length) {
        if (i + 1 < s.length && s[i] !== 'n' && s[i] === s[i + 1] && /[bcdfghjklmnpqrstvwxyz]/.test(s[i])) {
            result += 'っ';
            i++;
            continue;
        }
        let matched = false;
        for (let [rom, hira] of romajiMap) {
            if (s.startsWith(rom, i)) {
                result += hira;
                i += rom.length;
                matched = true;
                break;
            }
        }
        if (!matched) {
            result += s[i];
            i++;
        }
    }
    return result;
}

console.log(romajiToHiragana("happyou"));
