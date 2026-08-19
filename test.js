const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

const mapStart = content.indexOf('const romajiMap = [');
const mapEnd = content.indexOf('];', mapStart) + 2;
const mapStr = content.substring(mapStart, mapEnd);
let romajiMap;
eval("romajiMap = " + mapStr.replace('const romajiMap =', '').trim());

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

console.log("happyou ->", r2h("happyou"));
