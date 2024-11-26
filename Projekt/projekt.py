import re 
from collections import Counter
from langdetect import detect
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
    return len(text.replace(" ",""))


def analyzeText(text):
    lang = detectLanguage(text)
    characters = countCharacters(text)
    senteces = re.split(r'[.!?]+', text.strip())
    senteces = [sentence.strip() for sentence in senteces if sentence.strip()]

    words = re.findall(r'\b\w+\b',text.lower())

    countCharacters(words)

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

if __name__ == "__main__":
    sample =  """Python is a powerful programming language. It is widely used in data analysis, machine learning, and web development. Python's simplicity makes it popular among beginners and experts alike!"""

    analysis = analyzeText(sample)

    print("Statystki tekstu:")
    print(f"Liczba znaków: {analysis['characterCount']}")
    print(f"Liczba słów: {analysis['wordCount']}")
    print(f"Liczba zdań: {analysis['sentenceCount']}")
    print("Najczęściej występujące słowa:")
    for word, freq in analysis['mostCommonWords']:
        print(f"{word}: {freq}")
    print(f"Najdłuższe zdanie: {analysis['longestSentence']}")
    print(f"Długość najdłużeszego zdania: {analysis['longestSentenceLength']} słów")