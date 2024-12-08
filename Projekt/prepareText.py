import re 
from collections import Counter
from langdetect import detect # type: ignore
from stopWords import stopWords

def detectLanguage(text):
    return detect(text)

def isStopWord(word, language):
    return word in stopWords[language]
    
def countCharacters(text):
    clean = re.sub(r"[,.;@#?!&$]+\ *", " ", text)
    characters = len(clean.replace(" ",""))
    
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
        if not isStopWord(word, language):
            noStopWords.append(word)

    wordFrequency = Counter(noStopWords)
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
    
    return lines

def cleanLines(lines):
    cleanList = [line.replace('\n','') for line in lines]

    for line in cleanList:
        if line == '':
            cleanList.pop(cleanList.index(line))
        else:
            if line.endswith(('?','!',':',';')):
                line.pop()
            elif line.endswith(('.')):
                continue

            line = line + '.'
        
    return cleanList

def makeBigString(lines):
    bigString = ''

    for line in lines:
        bigString = bigString + line

    return bigString

def prepareText(text):
    cleanText = cleanLines(text)
    bigString = makeBigString(cleanText)
    return bigString
