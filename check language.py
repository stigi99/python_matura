from googletrans import Translator
translator = Translator()
y_n = ""
while y_n !="Y" or y_n !="y":
    verb = input("Podaj jakieś słowo a powiem Ci w jakim ono jest języku: ")

    try:
        translated = translator.detect(verb)
        print(translated)
    except:
        print("Złe dane")
    y_n = input("Czy chcesz przerwac Y/N ")


