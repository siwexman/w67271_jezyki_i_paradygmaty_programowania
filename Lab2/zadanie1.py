def analyze_text(text):
    # Zliczanie słów, zdań i akapitów
    sentences = text.split('.')
    paragraphs = text.split('\n')

    word_list = text.lower().split()
    words_count = len(word_list)
    sentences_count = len([s for s in sentences if s.strip()])
    paragraphs_count = len([p for p in paragraphs if p.strip()])

    # Lista stop words
    stop_words = {
        "i", "a", "the", "to", "w", "z", "na", "o", "za", "przez",
        "dla", "jak", "że", "co", "się", "ale", "wtedy", "jako",
        "taki", "ten", "która"
    }

    # Wyszukiwanie najczęściej występujących słów
    filtered_words = [word for word in word_list if word not in stop_words]
    word_counts = {}
    for word in filtered_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    most_common_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]

    # Transformacja słów rozpoczynających się na "a" lub "A"
    transformed_words = [
        word[::-1] if word.startswith('a') or word.startswith('A') else word
        for word in word_list
    ]

    return {
        'words_count': words_count,
        'sentences_count': sentences_count,
        'paragraphs_count': paragraphs_count,
        'most_common_words': most_common_words,
        'transformed_text': ' '.join(transformed_words)
    }


# Przykładowe użycie
text = """Ala ma kota. Kot ma na imię Mruczek.
To jest przykład tekstu, który analizujemy. 
Czy nie jest to ciekawa analiza?"""

result = analyze_text(text)

print("Liczba słów:", result['words_count'])
print("Liczba zdań:", result['sentences_count'])
print("Liczba akapitów:", result['paragraphs_count'])
print("Najczęściej występujące słowa:", result['most_common_words'])
print("Przekształcony tekst:", result['transformed_text'])
