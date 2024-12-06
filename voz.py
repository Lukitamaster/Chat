import pyttsx3

def PreguntarDeNuevo():
        noEntender = "incorrecto vuelve a escribir porfavor:"
        engine = pyttsx3.init()
        engine.say(noEntender)
        engine.runAndWait()


def ChatDeVoz():
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()

def correcto():
        hola = "lo lograste"
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')  # Obtener la velocidad actual
        engine.setProperty('rate', rate - 50)  # Reducir la velocidad (ajusta según sea necesario)
        engine.say(hola)
        engine.runAndWait()



verdura = "papa"
texto = input("escribi papa porfavor: ")
while texto != verdura:
    PreguntarDeNuevo()
    texto = input(": ")

else:
    correcto()


