const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
eval(content.substring(content.indexOf('const romajiMap'), content.indexOf('// Double consonant') - 1));

function r2h(str) {
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

console.log(r2h("happyou"));
