import pyttsx3
def ChatDeVoz():
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()

texto = input("escribi: ")
ChatDeVoz()