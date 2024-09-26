from english_words import get_english_words_set

uppercase_charset = list(map(chr, range(ord("A"), ord("Z") + 1)))
lowercase_charset = list(map(chr, range(ord("a"), ord("z") + 1)))
numeric_charset = list(map(chr, range(ord("0"), ord("9") + 1)))

words = get_english_words_set(["web2"])

class Caesar:
    @staticmethod
    def caesar(message: str, *, key: int, charset: list):
        words = message.split()
        return " ".join(Caesar.caesar_word(word, key=key, charset=charset) for word in words)


    @staticmethod
    def caesar_word(word: str, *, key: int, charset: list):
        return "".join(
            charset[(charset.index(char) + key) % len(charset)] if char in charset else char
            for char in word
        )


    @staticmethod
    def find(encrypted: str, *, charset: list, wordset: set[str]):
        best_matching: int = 0
        best_key: int | None = None
        best_result: str | None = None

        for i in range(len(charset)):
            shifted = Caesar.caesar(encrypted, key=i, charset=charset)
            if (amt := n_real_words(shifted, wordset)) > best_matching:
                best_matching = amt
                best_result = shifted
                best_key = i
        return best_result, best_key


class Vigenere:
    @staticmethod
    def make_keymap(message:str, key: str, charset: list):
        return [charset.index(k) if k in charset else 0 for k in "".join(key[(n - message[:n].count(" ")) % len(key)] if message[n] != " " else " " for n in range(len(message)))]
    
    @staticmethod
    def encrypt(message: str, key: str, charset: list):
        keymap = Vigenere.make_keymap(message, key, charset)
        return "".join(
            charset[(charset.index(char) + keymap[n]) % len(charset)] if char in charset else char
            for n, char in enumerate(message)
        )
    
    @staticmethod
    def decrypt(message: str, key: str, charset: list):
        keymap = Vigenere.make_keymap(message, key, charset)
        return "".join(
            charset[(charset.index(char) - keymap[n]) % len(charset)] if char in charset else char
            for n, char in enumerate(message)
        )
        
        

def n_real_words(message: str, wordset: set[str]):
    return sum(word in wordset for word in message.split())


if __name__ == "__main__":
    pass