import re 
from collections import Counter
from langdetect import detect # type: ignore
from stopWords import stopWords

def detectLanguage(text):
    return detect(text)

def isStopWord(word):
    if word in stopWords:
        return True
    else:
        return False
    
def countCharacters(text):
    characters = len(text.replace(" ",""))
    return characters


def analyzeText(text):
    language = detectLanguage(text)
    characters = countCharacters(text)
    senteces = re.split(r'[.!?]+', text.strip())
    senteces = [sentence.strip() for sentence in senteces if sentence.strip()]
    words = re.findall(r'\b\w+\b', text.lower())

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
        "language": language,
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
        lines = file.readlines()

    print(len(lines))
    return lines

if __name__ == "__main__":
    filename = input("Wpisz nazwę pliku txt: ").strip()

    text = readFile(filename)

    analysis = analyzeText(text)

    # text to display in txt file
    commonWords = ""
    for word, freq in analysis['mostCommonWords']:
        if commonWords == "":
            commonWords = commonWords + f"{word}: {freq}"
        else:
            commonWords = commonWords + f"\n{word}: {freq}"
    
    analitics = [
        "Statystki tekstu:",
        f"Język tekstu: {analysis['language']}",
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