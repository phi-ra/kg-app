import re

def isolate_related_concepts(legal_key, full_legal_set):
    art_dict_fin = {}
    art_dict = {}

    for entry_ in full_legal_set[legal_key]['citing_article']:
        if entry_['citing_title'] in art_dict.keys():
            art_dict[entry_['citing_title']].append(entry_['citing_article'])
        else:
            art_dict[entry_['citing_title']] = [entry_['citing_article']]

    for key, val in art_dict.items():
        art_dict[key] = list(set(val))

    for key, val in art_dict.items():
        val_c = []
        for it_ in val:
            if re.match('Art.(\s+)?\d+ ', it_):
                val_c.append(it_)
        
        art_dict_fin[key] = val_c

    return art_dict_fin
    
