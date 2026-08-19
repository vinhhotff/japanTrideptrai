import json

with open('compiled_kanji_dict.json', 'r', encoding='utf-8') as f:
    dict_data = json.load(f)

# Comprehensive Han-Viet map for most common Kanji
hanviet_map = {
    '一': 'NHẤT', '二': 'NHỊ', '三': 'TAM', '四': 'TỨ', '五': 'NGŨ', '六': 'LỤC', '七': 'THẤT', '八': 'BÁT', '九': 'CỬU', '十': 'THẬP',
    '百': 'BÁCH', '千': 'THIÊN', '万': 'VẠN', '円': 'VIÊN', '日': 'NHẬT', '月': 'NGUYỆT', '火': 'HỎA', '水': 'THỦY', '木': 'MỘC', '金': 'KIM',
    '土': 'THỔ', '年': 'NIÊN', '今': 'KIM', '時': 'THỜI', '分': 'PHÂN', '半': 'BÁN', '前': 'TIỀN', '後': 'HẬU', '上': 'THƯỢNG', '下': 'HẠ',
    '中': 'TRUNG', '右': 'HỮU', '左': 'TẢ', '大': 'ĐẠI', '小': 'TIỂU', '長': 'TRƯỞNG', '高': 'CAO', '安': 'AN', '新': 'TÂN', '古': 'CỔ',
    '多': 'ĐA', '少': 'THIỂU', '行': 'HÀNH', '来': 'LAI', '帰': 'QUY', '食': 'THỰC', '飲': 'ẨM', '見': 'KIẾN', '聞': 'VĂN', '読': 'ĐỘC',
    '書': 'THƯ', '話': 'THOẠI', '買': 'MÃI', '物': 'VẬT', '立': 'LẬP', '座': 'TỌA', '入': 'NHẬP', '出': 'XUẤT', '休': 'HƯU', '言': 'NGÔN',
    '思': 'TƯ', '知': 'TRI', '作': 'TÁC', '使': 'SỬ', '持': 'TRÌ', '待': 'ĐÃI', '教': 'GIÁO', '習': 'TẬP', '学': 'HỌC', '校': 'HIỆU',
    '先': 'TIÊN', '生': 'SINH', '父': 'PHỤ', '母': 'MẪU', '兄': 'HUYNH', '弟': 'ĐỆ', '姉': 'TỶ', '妹': 'MUỘI', '友': 'HỮU', '達': 'ĐẠT',
    '車': 'XA', '電': 'ĐIỆN', '駅': 'DỊCH', '道': 'ĐẠO', '店': 'ĐIẾM', '屋': 'ỐC', '家': 'GIA', '間': 'GIAN', '手': 'THỦ', '足': 'TÚC',
    '目': 'MỤC', '口': 'KHẨU', '耳': 'NHĨ', '心': 'TÂM', '体': 'THỂ', '力': 'LỰC', '気': 'KHÍ', '元': 'NGUYÊN', '天': 'THIÊN', '雨': 'VŨ',
    '雪': 'TUYẾT', '風': 'PHONG', '空': 'KHÔNG', '海': 'HẢI', '山': 'SƠN', '川': 'XUYÊN', '花': 'HOA', '魚': 'NGƯ', '肉': 'NHỤC', '茶': 'TRÀ',
    '飯': 'PHẠN', '朝': 'TRIÊU', '昼': 'TRÚ', '晩': 'VÃN', '夜': 'DẠ', '春': 'XUÂN', '夏': 'HẠ', '秋': 'THU', '冬': 'ĐÔNG', '男': 'NAM',
    '女': 'NỮ', '子': 'TỬ', '弁': 'BIỆN', '当': 'ĐƯƠNG', '温': 'ÔN', '袋': 'ĐẠI', '用': 'DỤNG', '利': 'LỢI', '席': 'TỊCH', '注': 'CHÚ',
    '文': 'VĂN', '員': 'VIÊN', '客': 'KHÁCH', '名': 'DANH', '様': 'DẠNG', '決': 'QUYẾT', '面': 'DIỆN', '接': 'TIẾP', '自': 'TỰ', '己': 'KỶ',
    '紹': 'THIỆU', '介': 'GIỚI', '志': 'CHÍ', '望': 'VỌNG', '動': 'ĐỘNG', '機': 'CƠ', '長': 'TRƯỞNG', '病': 'BỆNH', '院': 'VIỆN', '診': 'CHẨN',
    '察': 'SÁT', '医': 'Y', '者': 'GIẢ', '患': 'HOẠN', '症': 'CHỨNG', '状': 'TRẠNG', '熱': 'NHIỆT', '頭': 'ĐẦU', '痛': 'THỐNG', '薬': 'DƯỢC',
    '切': 'THIẾT', '符': 'PHÙ', '乗': 'THỪA', '換': 'HOÁN', '勉': 'MIỄN', '強': 'CƯỜNG', '最': 'TỐI', '近': 'CẬN', '趣': 'THÚ', '味': 'VỊ',
    '会': 'HỘI', '試': 'THÍ', '験': 'NGHIỆM', '答': 'ĐÁP', '問': 'VẤN', '題': 'ĐỀ', '意': 'Ý', '思': 'TƯ', '感': 'CẢM', '情': 'TÌNH',
    '愛': 'ÁI', '好': 'HẢO', '嫌': 'HIỀM', '楽': 'LẠC', '苦': 'KHỔ', '難': 'NAN', '易': 'DỊ', '重': 'TRỌNG', '軽': 'KHINH', '早': 'TẢO',
    '遅': 'TRÌ', '速': 'TỐC', '遠': 'VIỄN', '広': 'QUẢNG', '狭': 'HIỆP', '明': 'MINH', '暗': 'ÁM', '白': 'BẠCH', '黒': 'HẮC', '赤': 'XÍCH',
    '青': 'THANH', '黄': 'HOÀNG', '緑': 'LỤC', '色': 'SẮC', '音': 'ÂM', '声': 'THANH', '歌': 'CA', '画': 'HỌA', '真': 'CHÂN', '写': 'TẢ',
    '映': 'ÁNH', '旅': 'LỮ', '仕': 'SĨ', '事': 'SỰ', '忙': 'MANG', '暇': 'HẠ', '運': 'VẬN', '転': 'CHUYỂN', '歩': 'BỘ', '走': 'TẨU',
    '泳': 'VỊNH', '洗': 'TẨY', '使': 'SỬ', '着': 'TRƯỚC', '脱': 'THOÁT', '開': 'KHAI', '閉': 'BẾ', '始': 'THỦY', '終': 'CHUNG', '死': 'TỬ',
    '活': 'HOẠT', '私': 'TƯ', '彼': 'BỈ', '誰': 'THÙY', '何': 'HÀ', '同': 'ĐỒNG', '違': 'VI', '正': 'CHÍNH', '変': 'BIẾN', '特': 'ĐẶC'
}

js_content = f'''// Japanese Kanji & Word Dictionary Dataset for Hover Translation
const KANJI_DICTIONARY = {json.dumps(dict_data, ensure_ascii=False)};
const KANJI_HANVIET_MAP = {json.dumps(hanviet_map, ensure_ascii=False)};

// Helper to extract Han-Viet for any Kanji string
function getHanvietForString(str) {{
    if (!str) return '';
    let result = [];
    for (let char of str) {{
        if (KANJI_HANVIET_MAP[char]) {{
            result.push(KANJI_HANVIET_MAP[char]);
        }}
    }}
    return result.join(' ');
}}

// Comprehensive word lookup
function lookupJapaneseWord(word) {{
    if (!word) return null;
    let clean = word.trim();
    
    // 1. Direct match
    if (KANJI_DICTIONARY[clean]) {{
        let item = KANJI_DICTIONARY[clean];
        return {{
            word: clean,
            h: item.h || '',
            m: item.m || '',
            hv: item.hv || getHanvietForString(clean),
            lvl: item.lvl || 'N3'
        }};
    }}

    // 2. Try stripping honorific prefix お/ご
    let stripped = clean.replace(/^[おご御]/, '');
    if (KANJI_DICTIONARY[stripped]) {{
        let item = KANJI_DICTIONARY[stripped];
        return {{
            word: clean,
            h: item.h ? (clean.startsWith('お') ? 'お' + item.h : (clean.startsWith('ご') ? 'ご' + item.h : item.h)) : '',
            m: item.m || '',
            hv: item.hv || getHanvietForString(clean),
            lvl: item.lvl || 'N3'
        }};
    }}

    // 3. Try removing common verb/adj inflections (ます, ました, ません, て, た, い, く, ない)
    let stem = clean.replace(/(ます|ました|ません|ましょう|て|た|ない|れる|られる|せる|させる|そう|たい|がる)$/, '');
    if (stem && KANJI_DICTIONARY[stem]) {{
        let item = KANJI_DICTIONARY[stem];
        return {{
            word: clean,
            h: item.h || '',
            m: item.m || '',
            hv: item.hv || getHanvietForString(clean),
            lvl: item.lvl || 'N3'
        }};
    }}

    // 4. Fallback: extract Kanji characters & build definition
    let kanjiOnly = clean.replace(/[^一-龥々]/g, '');
    if (kanjiOnly && kanjiOnly.length > 0) {{
        let hv = getHanvietForString(kanjiOnly);
        if (hv) {{
            return {{
                word: clean,
                h: '',
                m: 'Âm Hán: ' + hv,
                hv: hv,
                lvl: 'Kanji'
            }};
        }}
    }}

    return null;
}}

// Tokenize text: wrap Kanji words with interactive hover spans, keep Hiragana untouched
function renderInteractiveJapaneseText(text) {{
    if (!text) return '';
    
    // Regex matching sequences that contain at least one Kanji [一-龥々]
    const kanjiRegex = /([一-龥々]+[ぁ-んァ-ン]*|[ぁ-ん]*[一-龥々]+[ぁ-ん]*)/g;
    
    return text.replace(kanjiRegex, (match) => {{
        const info = lookupJapaneseWord(match);
        if (!info) {{
            // If contains kanji, still add basic han-viet hover
            const hv = getHanvietForString(match);
            if (hv) {{
                const fallbackData = encodeURIComponent(JSON.stringify({{
                    word: match,
                    reading: '',
                    meaning: 'Hán Việt: ' + hv,
                    hanviet: hv,
                    level: 'Kanji'
                }}));
                return `<span class="kanji-interactive-word" data-info="${{fallbackData}}" onmouseenter="showKanjiHoverTooltip(event, this)" onmouseleave="hideKanjiHoverTooltip()">${{escapeHtml(match)}}</span>`;
            }}
            return escapeHtml(match);
        }}

        const dataStr = encodeURIComponent(JSON.stringify({{
            word: info.word || match,
            reading: info.h || '',
            meaning: info.m || '',
            hanviet: info.hv || getHanvietForString(match),
            level: info.lvl || ''
        }}));

        return `<span class="kanji-interactive-word" data-info="${{dataStr}}" onmouseenter="showKanjiHoverTooltip(event, this)" onmouseleave="hideKanjiHoverTooltip()">${{escapeHtml(match)}}</span>`;
    }});
}}

// Tooltip positioning & display handlers
function showKanjiHoverTooltip(event, el) {{
    let tooltip = document.getElementById('kanji-hover-tooltip');
    if (!tooltip) {{
        tooltip = document.createElement('div');
        tooltip.id = 'kanji-hover-tooltip';
        document.body.appendChild(tooltip);
    }}

    const rawData = el.getAttribute('data-info');
    if (!rawData) return;

    try {{
        const data = JSON.parse(decodeURIComponent(rawData));
        
        let levelBadge = data.level ? `<span class="kt-badge">${{escapeHtml(data.level)}}</span>` : '';
        let readingHtml = data.reading ? `<span class="kt-reading">${{escapeHtml(data.reading)}}</span>` : '';
        let hanvietHtml = data.hanviet ? `<div class="kt-hanviet">Âm Hán: <strong>${{escapeHtml(data.hanviet)}}</strong></div>` : '';
        let meaningHtml = data.meaning ? `<div class="kt-meaning">${{escapeHtml(data.meaning)}}</div>` : '';

        tooltip.innerHTML = `
            <div class="kt-header">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span class="kt-word">${{escapeHtml(data.word)}}</span>
                    ${{readingHtml}}
                </div>
                ${{levelBadge}}
            </div>
            ${{hanvietHtml}}
            ${{meaningHtml}}
        `;

        tooltip.style.display = 'flex';

        // Calculate position relative to element
        const rect = el.getBoundingClientRect();
        const tooltipWidth = 260;
        let left = rect.left + (rect.width / 2) - (tooltipWidth / 2);
        let top = rect.top - 85;

        // Prevent off-screen
        if (left < 10) left = 10;
        if (left + tooltipWidth > window.innerWidth - 10) {{
            left = window.innerWidth - tooltipWidth - 10;
        }}
        if (top < 10) {{
            top = rect.bottom + 8; // Show below if too close to top
        }}

        tooltip.style.left = left + 'px';
        tooltip.style.top = top + 'px';
    }} catch(e) {{
        console.error('Tooltip parse error:', e);
    }}
}}

function hideKanjiHoverTooltip() {{
    const tooltip = document.getElementById('kanji-hover-tooltip');
    if (tooltip) {{
        tooltip.style.display = 'none';
    }}
}}
'''

with open('kanji_dict_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print('kanji_dict_data.js successfully generated!')
