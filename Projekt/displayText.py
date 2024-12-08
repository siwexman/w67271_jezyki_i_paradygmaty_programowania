# text to display in txt file
def displayAndSave(analysis):
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