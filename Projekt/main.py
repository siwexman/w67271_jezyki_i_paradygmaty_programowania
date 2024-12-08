from prepareText import prepareText, readFile, analyzeText
from displayText import displayAndSave

if __name__ == "__main__":
    filename = input("Wpisz nazwę pliku txt: ").strip()

    text = readFile(filename)
    prepText = prepareText(text)

    analysis = analyzeText(prepText)
    displayAndSave(analysis)