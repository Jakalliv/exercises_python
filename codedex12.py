def translator(language):
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}
    return translations.get(language)

def translate_word(language, word):
    return language.get(word)

x = translate_word(translator("italian"), "hello")

if __name__ == "__main__":
    print(x)