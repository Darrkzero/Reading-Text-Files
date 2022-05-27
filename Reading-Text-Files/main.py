# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string


def read_file_content(filename):
    # [assignment] Add your code here
    return open(filename, "r")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text_list = text.read()
    new_textlist = text_list.translate(str.maketrans('', '', string.punctuation)).split()
    text_dict = {}
    for words in new_textlist:
        if words in text_dict:
            text_dict[words] += 1
        else:
            text_dict[words] = 1
    return text_dict


print(count_words())
