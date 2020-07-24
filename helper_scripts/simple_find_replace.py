#NOTE: USE WITH CARE - ALL ENTRIES MUST BE HAND-CHECKED
dict= open('../cedict_ts.u8', encoding='utf-8')

from_word = 'color'
to_word = 'colour'
locale = 'en-GB'

for line in dict:
    line = line.rstrip('\n')
    if from_word in line:
        print('{\n"original": "' + line + '",\n"' + locale + '": "' + line.replace(from_word, to_word) + '"\n},')