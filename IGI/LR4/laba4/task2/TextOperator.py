import re


class TextOperator:
    '''Class for operating with text.'''

    def __init__(self, text='') -> None:
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, input_text):
        self.__text = input_text

    def sentencesCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!?.]', self.__text)
        return len(sentences)

    def declSentCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[.]', self.__text)
        return len(sentences)

    def exclSentCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!]', self.__text)
        return len(sentences)

    def interrogSentCount(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[?]', self.__text)
        return len(sentences)

    def medSentSize(self):
        sentences = re.findall(r'[A-Z0-9][^?!.]*[!?.]', self.__text)
        sizesum = 0
        for snt in sentences:
            snt = snt.replace(',', '').replace(';', '')
            sizesum += len(snt.split())
        return sizesum / len(sentences)

    def medWordSize(self):
        text = self.__text.replace(',', '') \
            .replace(';', '').replace('.', '') \
            .replace('!', '').replace('?', '').replace('\n', '')
        wordCounter = 0
        sizeSum = 0
        for w in text.split():
            if (w == ''):
                continue
            wordCounter += 1
            sizeSum += len(w)
        return sizeSum / wordCounter

    def emojisCount(self):
        emojis = re.findall(r"(:|;)(\-*)(\(+|\)+|\[+|\]+)",self.__text)
        return len(emojis)

    def binaryList(self):
        return re.findall(r'\b[01]+\b', self.__text)

    def vowelConsonantWords(self):
        return re.findall(r'\b[aeiouAEIOU][bcdfghjklmnpqrstvwxyz]\w*', self.__text)

    def wordsWithVowel(self):
        words_with_vowel = re.findall(r'\b[aeiouAEIOU]|\b\w*[aeiouAEIOU]\b', self.__text)
        return len(words_with_vowel)

    def charCount(self):
        char_counts = {}
        for char in self.__text:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return char_counts
    def wordsAfterComma(self):
        words_after_comma = sorted(re.findall(r', (\w+)', self.__text))
        return words_after_comma
