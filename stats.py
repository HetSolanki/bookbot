def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    chars = {}
    for c in text:
        c = c.lower()
        if (c in chars):
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_dir(dict):
    list = []
    for key, value in dict.items():
       if (key.isalpha()):
           list.append({"key": key, "value": value})
    list.sort(reverse=True, key=sort_on)    
    return list

def sort_on(list):
    return list['value']
