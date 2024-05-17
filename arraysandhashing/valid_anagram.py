def is_anagram_sorting(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    This implementation first sorts each string and traverse them with two pointers, if the characters of the
    sorted string at pointer's position are different, then this is not an anagram
    :param s:
    :param t:
    :return:
    """

    if len(s) != len(t):
        return False

    s_array = [char for char in s]
    t_array = [char for char in t]
    s_array.sort()
    t_array.sort()
    s_ptr = t_ptr = 0

    while s_ptr < len(s) and t_ptr < len(t):
        if s_array[s_ptr] != t_array[t_ptr]:
            return False
        s_ptr += 1
        t_ptr += 1

    return True


def is_anagram_dictionary(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Using a dictionary for s ant for t, first it populates both dictionaries, and then if the number of key in s_map is
    different from the number of unique elements in t is not an anagram. After it checks the keys in one of the
    dictionaries, if the key is not in the second dictionary this is not an anagram, else checks if the number of
    occurrences in the key are the same
    :param s:
    :param t:
    :return:
    """
    s_map = {}
    for s_char in s:
        if s_char not in s_map:
            s_map[s_char] = 0
        s_map[s_char] += 1

    t_map = {}
    for t_char in t:
        if t_char not in t_map:
            t_map[t_char] = 0
        t_map[t_char] += 1

    if len(s_map.keys()) != len(set(t)):
        return False

    for key in s_map.keys():
        if key not in t_map:
            return False
        if s_map[key] != t_map[key]:
            return False

    return True


def is_anagram_count_occurrences(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    This implementation uses an array of the size of characters from a to z, then checks each character from each string
    and for s characters it adds one to the counter at the character position in the counter array, and for t characters
    it subtracts one to the counter at the character position in the counter array. If any of the values in the counter
    is not 0 then this is not an anagram.
    :param s:
    :param t:
    :return:
    """
    if len(s) != len(t):
        return False

    counter = [0] * 26
    a = ord('a')

    for ptr in range(len(s)):
        s_char_at = ord(s[ptr]) - a
        t_char_at = ord(t[ptr]) - a
        counter[s_char_at] += 1
        counter[t_char_at] -= 1

    for count in counter:
        if count != 0:
            return False

    return True
