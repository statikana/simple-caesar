from english_words import get_english_words_set

uppercase_charset = list(map(chr, range(ord("A"), ord("Z") + 1)))
lowercase_charset = list(map(chr, range(ord("a"), ord("z") + 1)))
numeric_charset = list(map(chr, range(ord("0"), ord("9") + 1)))

words = get_english_words_set(["web2"])


def caesar(message: str, *, key: int, charset: list):
    words = message.split()
    return " ".join(caesar_word(word, key=key, charset=charset) for word in words)


def caesar_word(word: str, *, key: int, charset: list):
    return "".join(
        charset[(charset.index(char) + key) % len(charset)] if char in charset else char
        for char in word
    )


def n_real_words(message: str, wordset: set[str]):
    return sum(word in wordset for word in message.split())


def find(encrypted: str, *, charset: list, wordset: set[str]):
    best_matching: int = 0
    best_key: int | None = None
    best_result: str | None = None

    for i in range(len(charset)):
        shifted = caesar(encrypted, key=i, charset=charset)
        if (amt := n_real_words(shifted, wordset)) > best_matching:
            best_matching = amt
            best_result = shifted
            best_key = i
    return best_result, best_key



if __name__ == "__main__":
    capitals_wordset = set(map(str.upper, words))
    message = (
        "AOHA'Z AOL TVZA MVBS, JYBLS, HUK IHK-ALTWLYLK YVKLUA FVB LCLY ZLA FVBY LFLZ VU"
    )
    result, key = find(message, charset=uppercase_charset, wordset=capitals_wordset)
    print(message, caesar(message, key=key, charset=uppercase_charset))
