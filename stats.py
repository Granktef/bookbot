
def get_word_count(words):
    single_words = words.split()
    return len(single_words)

def get_character_count(words):
    character_count = {}
    low_words = words.lower()
    for char in low_words:
        if char not in character_count:
            character_count[char] = 1
        else :            
            character_count[char] += 1
    return character_count

def sort_on(dict):
    return dict["num"]


def sort_counts(counts):
    count_list = []
    for count in counts:
        count_list.append({
            "letter" : count,
            "num" : counts[count]
        })

    count_list.sort(key=sort_on, reverse=True)
    return count_list   

    