# load words

def load_custom_words(position="usr/words.txt", word_len=5):
    with open(position, 'r') as words:
        return sorted([word.strip().lower() for word in words.readlines()
                       if (len(word) == word_len+1 and "\n" in word) or (len(word) == word_len and "\n" not in word)])

lcw = load_custom_words

with open("default_words.txt", 'r') as f:
    dw = default_words = [line.strip() for line in f.readlines()]
