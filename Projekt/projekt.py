import re 
from collections import Counter
from langdetect import detect # type: ignore
from stopWords import stopWords

def detectLanguage(text):
    lang = detect(text)

    return lang

def isStopWord(word):
    if word in stopWords:
        return True
    else:
        return False
    
def countCharacters(text):
    characters = len(text.replace(" ",""))
    return characters


def analyzeText(text):
    lang = detectLanguage(text)
    characters = countCharacters(text)
    senteces = re.split(r'[.!?]+', text.strip())
    senteces = [sentence.strip() for sentence in senteces if sentence.strip()]
    words = re.findall(r'\b\w+\b',text.lower())

    wordCount = len(words)
    senteceCount = len(senteces)

    noStopWords = []

    for word in words:
        if isStopWord(word):
            continue
        noStopWords.append(word)

    wordFrequency = Counter(words)
    mostCommonWord = wordFrequency.most_common(5)

    longestSentence = max(senteces, key=len) if senteces else ""
    longestSentenceLength = len(longestSentence.split())

    result = {
        "characterCount": characters,
        "wordCount": wordCount,
        "sentenceCount": senteceCount,
        "mostCommonWords": mostCommonWord,
        "longestSentence": longestSentence,
        "longestSentenceLength": longestSentenceLength        
    }

    return result

def readFile(filename):
    with open(filename + '.txt', 'r', encoding='utf-8') as file:
        lines = file.read()

    print(lines)
    return lines

if __name__ == "__main__":
    filename = input("Wpisz nazwę pliku txt: ").strip()

    text = readFile(filename)

    analysis = analyzeText(text)


    # print("Statystki tekstu:")
    # print(f"Liczba wszystkich znaków: {analysis['characterCount']}")
    # print(f"Liczba słów: {analysis['wordCount']}")
    # print(f"Liczba zdań: {analysis['sentenceCount']}")
    # print("Pięć najczęściej występujących słów:")
    # for word, freq in analysis['mostCommonWords']:
    #     print(f"{word}: {freq}")
    # print(f"Najdłuższe zdanie: {analysis['longestSentence']}")
    # print(f"Długość najdłużeszego zdania: {analysis['longestSentenceLength']} słów")

    # text to display in txt file
    commonWords = ""
    for word, freq in analysis['mostCommonWords']:
        if commonWords == "":
            commonWords = commonWords + f"{word}: {freq}"
        else:
            commonWords = commonWords + f"\n{word}: {freq}"
    
    analitics = [
        "Statystki tekstu:",
        f"Liczba wszystkich znaków: {analysis['characterCount']}",
        f"Liczba słów: {analysis['wordCount']}",
        f"Liczba zdań: {analysis['sentenceCount']}",
        "Pięć najczęściej występujących słów:",
        commonWords,
        f"Najdłuższe zdanie: {analysis['longestSentence']}",
        f"Długość najdłużeszego zdania: {analysis['longestSentenceLength']} słów"
        ]

    stringAnalitics = ''

    for sentence in analitics:
        if stringAnalitics == '':
            stringAnalitics = stringAnalitics + sentence
        else:
            stringAnalitics = stringAnalitics + '\n' + sentence
    
            

    with open('analitics.txt', 'w',encoding='utf-8') as file:
        file.write(stringAnalitics)