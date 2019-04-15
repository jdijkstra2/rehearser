import string

def convert(filename):
    """ Converts a wikipedia table of kanji characters to a rehearsable list of pairs [kanji, meaning]"""
    
    lines = open(filename, encoding='utf-8')
    pairs = []
    for line in lines:
        line = line.replace("; ", ",")
        list = line.split()
        list[3] = list[3].replace(",", ", ")
        pairs.append([list[1], list[3]])
    return pairs

