from TextOperator import TextOperator
import zipfile


def task2():
    top = TextOperator()
    with open('text.txt', 'r') as f:
        text = f.read()
        top.text = text
    with open('output.txt', 'w') as f:
        print(f"Sentences count: {top.sentencesCount()}\n")
        f.write(f"Sentences count: {top.sentencesCount()}\n")

        print(f"Declaritive sentences count: {top.declSentCount()}\n")
        f.write(f"Declaritive sentences count: {top.declSentCount()}\n")

        print(f"Exclamation sentences count: {top.exclSentCount()}\n")
        f.write(f"Exclamation sentences count: {top.exclSentCount()}\n")

        print(f"Interrogative sentences count: {top.interrogSentCount()}\n")
        f.write(f"Interrogative sentences count: {top.interrogSentCount()}\n")

        print(f"Median of sentences size: {top.medSentSize()}\n")
        f.write(f"Median of sentences size: {top.medSentSize()}\n")

        print(f"Median word: {top.medWordSize()}\n")
        f.write(f"Median word: {top.medWordSize()}\n")

        print(f"Emojis count: {top.emojisCount()}\n")
        f.write(f"Emojis count: {top.emojisCount()}\n")

        print(f"Binary list: {top.binaryList()}\n")
        f.write(f"Binary list: {top.binaryList()}\n")

        print(f"Vowel and consonant: {top.vowelConsonantWords()}\n")
        f.write(f"Vowel and consonant: {top.vowelConsonantWords()}\n")

        print(f"Words with vowel: {top.wordsWithVowel()}\n")
        f.write(f"Words with vowel: {top.wordsWithVowel()}\n")

        print(f"Chars: {top.charCount()}\n")
        f.write(f"Chars: {top.charCount()}\n")

        print(f"Words after comma: {top.wordsAfterComma()}\n")
        f.write(f"words after comma: {top.wordsAfterComma()}\n")
    with zipfile.ZipFile("myzip.zip", 'w') as myzip:
        myzip.write("output.txt")

task2()