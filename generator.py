import json

source_cedict = open('cedict_ts.u8', encoding='utf-8')
output_cedict = open('cedict_en-gb.u8', 'w', encoding='utf-8')

with open('replacements/replacements.json', encoding='utf-8') as file:
    line_replacements = json.load(file)

for line in source_cedict:
    line = line.rstrip('\n')
    replaced = False
    for replacement_set in line_replacements['data']:
        if(line == replacement_set['original']):
            # TODO:optimise by removing item from the list as soon as it is matched
            output_cedict.write(replacement_set['en-GB'] + '\n')
            replaced = True
            break
    if not replaced:
        output_cedict.write(line + '\n')