import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language='es')
        print(f"Has dicho: {text}")
        return text.lower()

def main():
    text = talk()
    if 'amazon' in text:
        engine.say('¿Qué quieres comprar en Amazon?')
        engine.runAndWait()
        search_term = talk()
        webbrowser.open(f'https://www.amazon.es/s?k={search_term}')

if __name__ == "__main__":
    main()
