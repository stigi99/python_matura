from googletrans import Translator
translator = Translator()
y_n = ""
while y_n !="Y" or y_n !="y":
    verb = input("Podaj swoje imie: ")
    language= input("Podaj wyroznik jezyka: ")
    try:
        translated = translator.translate(verb , dest=language)
        print(translated.origin, "=>" , translated.text)
    except:
        print("Złe dane")
    y_n = input("Czy chcesz przerwac Y/N ")


