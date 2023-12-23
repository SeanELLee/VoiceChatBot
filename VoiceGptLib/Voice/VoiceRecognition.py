import speech_recognition as sr


class cVoiceRecognition():
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        pass

    def record_speech_to_text(self) -> str:
        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    return text
                
            except sr.UnknownValueError:
                continue

            
    pass

if __name__ == "__main__":
    while True:
        oVoiceRecognition = cVoiceRecognition()
        message = oVoiceRecognition.record_speech_to_text()
        print(message)
        if message == "over":
            break
    pass
