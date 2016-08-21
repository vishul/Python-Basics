def break_words(stuff):
    words=stuff.split(' ')
    return words
def sorted_words(words):
    return sorted(words)
def print_first_word(words):
    w=words.pop(0)
    print w
def print_last_word(words):
    w=words.pop(-1)
    print w
def sort_sentence(sentence):
    word=break_words(sentence)
    word=sorted_words(word)
    return word
def print_first_and_last(sentence):
    word=break_word(sentence)
    print_first_word(word)
    print_last_word(word)
def print_first_and_last_sorted(sentence):
    word=break_word(sentence)
    word=sorted_word(word)
    print_first_word(word);
    print_last_word(word);
