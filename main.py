# implement the following functions
# each must use the max() function in its implementation

WORDS = ["jumps", "laziest", "brown", "a", "quick", "fox", "the", "dog", "over"]

# find the word that is alphabetically "highest" (comes last alphabetically)
def get_last_word_alphabetically(words):
    pass

# find the longest word
def get_longest_word(words):
    pass

# find the shortest word (still using max)
# this is a little sneaky!
def get_shortest_word(words):
    pass

# BONUS: now using sorted, put the jumbled sentence into this order:
# a quick brown fox jumps over the laziest dog
# this should still be a list of words, not a single string
# this is a very sneaky!
def get_ordered_words(words):
    pass

# BONUS BONUS BONUS: Back to using max! How can we get the _first_ word
# alphabetically in the list? This one is _very_ sneaky (and
# absolutely not recommended in real code. Just use min!).

# This is very challenging and requires concepts not covered in the
# curriculum! Feel no pressure to attempt this at all!

def get_first_word_alphabetically(words):
    pass

def main():
    assert get_last_word_alphabetically(WORDS) == "the"
    print("get_last_word_alphabetically PASSED!")
    assert get_longest_word(WORDS) == "laziest"
    print("get_longest_word PASSED!")
    assert get_shortest_word(WORDS) == "a"
    print("get_shortest_word PASSED!")

    # BONUS
    # assert get_ordered_words(WORDS) == [
    #     "a", "quick", "brown", "fox", "jumps", 
    #     "over", "the", "laziest", "dog"
    # ]
    # print("get_ordered_words PASSED!")

    # BONUS BONUS BONUS
    # assert get_first_word_alphabetically(WORDS) == "a"
    # print("get_first_word_alphabetically PASSED!")

    
    print("All tests PASSED!")

if __name__ == "__main__":
    main()
