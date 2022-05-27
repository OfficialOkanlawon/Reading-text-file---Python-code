# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    read_file_content = open("story.txt", "r") 
    return read_file_content.read()

all_words = read_file_content()
print(all_words)


def count_words():
    text = read_file_content()
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

all_word = count_words()
print(all_word)