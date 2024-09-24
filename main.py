from enum import Enum
from english_words import get_english_words_set

capital_letters = list(map(chr, range(ord("A"), ord("Z")+1)))
lowercase = list(map(chr, range(ord("a"), ord("z")+1)))
numbers = list(map(chr, range(ord("0"), ord("9")+1)))

words = get_english_words_set(["web2"])

# print(words)

def caesar(message: str, *, key: int, keyset: list):
    words = message.split()
    return " ".join(caesar_word(word, key=key, keyset=keyset) for word in words)
    

def caesar_word(word: str, *, key: int, keyset: list):
    return "".join(
        keyset[(keyset.index(char) + key) % len(keyset)]
        if char in keyset
        else char
        for char in word
    )



def n_real_words(message: str, wordset: set[str]):
    return sum(word in wordset for word in message.split())

def find(encrypted: str, *, keyset: list, wordset: set[str]):
    best_matching: int = 0
    best_key: int | None = None
    best_result: str | None = None
    
    for i in range(len(keyset)):
        shifted = caesar(encrypted, key=i, keyset=keyset)
        if (amt := n_real_words(shifted, wordset)) > best_matching:
            best_matching = amt
            best_result = shifted   
            best_key = i
    return best_result, best_key


capitals_wordset = set(map(str.upper, words))
message = "AOHA'Z AOL TVZA MVBS, JYBLS, HUK IHK-ALTWLYLK YVKLUA FVB LCLY ZLA FVBY LFLZ VU"

result, key = find(message, keyset=capital_letters, wordset=capitals_wordset)
print(message, caesar(message, key=key, keyset=capital_letters))