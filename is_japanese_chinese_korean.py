# -*- coding:utf-8 -*-
# # from https://stackoverflow.com/questions/30069846/how-to-find-out-chinese-or-japanese-character-in-a-string-in-python
# ranges = [
#   {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
#   {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
#   {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
#   {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
#   {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
#   {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
#   {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
#   {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
#   {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
#   {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
#   {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
#   {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
#   {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
# ]

# def is_cjk(char):
#   print(char)
#   return any([range["from"] <= ord(char) <= range["to"] for range in ranges])

# def cjk_substrings(string):
#   i = 0
#   while i<len(string):
#     if is_cjk(string[i]):
#       start = i
#       while is_cjk(string[i]): i += 1
#       yield string[start:i]
#     i += 1

# string = "sdf344asfasf天地方益3権sdfsdf".encode("utf-8")
# for sub in cjk_substrings(string):
#   string = string.replace(sub, "(" + sub + ")")
# print (string)


def is_cjk(character):
    """"
    Checks whether character is CJK.

        >>> is_cjk(u'\u33fe')
        True
        >>> is_cjk(u'\uFE5F')
        False

    :param character: The character that needs to be checked.
    :type character: char
    :return: bool
    """
    return any([start <= ord(character) <= end for start, end in 
                [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215), 
                 (63744, 64255), (65072, 65103), (65381, 65500), 
                 (131072, 196607)]
                ])
  

class CJKChars(object):
    """
    An object that enumerates the code points of the CJK characters as listed on
    http://en.wikipedia.org/wiki/Basic_Multilingual_Plane#Basic_Multilingual_Plane

    This is a Python port of the CJK code point enumerations of Moses tokenizer:
    https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/detokenizer.perl#L309
    """
    # Hangul Jamo (1100–11FF)
    Hangul_Jamo = (4352, 4607) # (ord(u"\u1100"), ord(u"\u11ff"))

    # CJK Radicals Supplement (2E80–2EFF)
    # Kangxi Radicals (2F00–2FDF)
    # Ideographic Description Characters (2FF0–2FFF)
    # CJK Symbols and Punctuation (3000–303F)
    # Hiragana (3040–309F)
    # Katakana (30A0–30FF)
    # Bopomofo (3100–312F)
    # Hangul Compatibility Jamo (3130–318F)
    # Kanbun (3190–319F)
    # Bopomofo Extended (31A0–31BF)
    # CJK Strokes (31C0–31EF)
    # Katakana Phonetic Extensions (31F0–31FF)
    # Enclosed CJK Letters and Months (3200–32FF)
    # CJK Compatibility (3300–33FF)
    # CJK Unified Ideographs Extension A (3400–4DBF)
    # Yijing Hexagram Symbols (4DC0–4DFF)
    # CJK Unified Ideographs (4E00–9FFF)
    # Yi Syllables (A000–A48F)
    # Yi Radicals (A490–A4CF)
    CJK_Radicals = (11904, 42191) # (ord(u"\u2e80"), ord(u"\ua4cf"))

    # Phags-pa (A840–A87F)
    Phags_Pa = (43072, 43135) # (ord(u"\ua840"), ord(u"\ua87f"))

    # Hangul Syllables (AC00–D7AF)
    Hangul_Syllables = (44032, 55215) # (ord(u"\uAC00"), ord(u"\uD7AF"))

    # CJK Compatibility Ideographs (F900–FAFF)
    CJK_Compatibility_Ideographs = (63744, 64255) # (ord(u"\uF900"), ord(u"\uFAFF"))

    # CJK Compatibility Forms (FE30–FE4F)
    CJK_Compatibility_Forms = (65072, 65103) # (ord(u"\uFE30"), ord(u"\uFE4F"))

    # Range U+FF65–FFDC encodes halfwidth forms, of Katakana and Hangul characters
    Katakana_Hangul_Halfwidth = (65381, 65500) # (ord(u"\uFF65"), ord(u"\uFFDC"))

    # Supplementary Ideographic Plane 20000–2FFFF
    Supplementary_Ideographic_Plane = (131072, 196607) # (ord(u"\U00020000"), ord(u"\U0002FFFF"))

    ranges = [Hangul_Jamo, CJK_Radicals, Phags_Pa, Hangul_Syllables, 
              CJK_Compatibility_Ideographs, CJK_Compatibility_Forms, 
              Katakana_Hangul_Halfwidth, Supplementary_Ideographic_Plane]

def is_kanji(character):
  
  return any([ord(u"\u4e00") <= ord(character) <= ord(u"\u9faf")])
#4e00 - 9faf
print(is_kanji('a'))
print(is_kanji('歯'))
print(is_kanji('水'))
print(is_kanji('书'))
print(is_kanji('は'))
print(is_kanji('、'))
print(is_kanji('a'))
