import replacements.en_GB as engb

source_cedict = open('cedict_ts.u8', encoding='utf-8')
output_cedict = open('cedict_en-gb.u8', 'w', encoding='utf-8')

line_replacements = engb.getReplacements()

for line in source_cedict:
    line = line.rstrip('\n')
    replaced = False
    for replacement_pair in line_replacements:
        if(line == replacement_pair[0]):
            output_cedict.write(replacement_pair[1] + '\n')
            replaced = True
    if not replaced:
        output_cedict.write(line + '\n')