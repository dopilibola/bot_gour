from uzwords import words
from difflib import get_close_matches

def checkWord12(word, words=words):  # Funksiya nomi to'g'ri
    word = word.lower()
    matches = set(get_close_matches(word, words))  # Funksiyani to'g'ri chaqiramiz
    available = word in words  # So‘z mavjudligini tekshiramiz

    if 'x' in word:
        word_variant = word.replace('x', 'x')  # Hech qanday o‘zgarish bo‘lmayapti, kerak emas
        matches.update(get_close_matches(word_variant, words))

    return {'available': available, 'matches': list(matches)}  # JSON uchun setni listga aylantiramiz