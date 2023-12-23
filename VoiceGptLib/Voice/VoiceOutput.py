import elevenlabs
import pyttsx3

class cVoiceOutput():
    def __init__(self) -> None:
        # self.pyttsx3_engine = pyttsx3.init()
        pass

    def speak_to_audience_elevenlabs(self, api_key, voice_actor : str, input : str) -> str:
        elevenlabs.set_api_key = api_key
        audio = elevenlabs.generate(text = input,  voice = voice_actor)
        elevenlabs.play(audio)
        return "done"
    
    def speak_to_audience_pyttsx3(self, input : str) -> str:
        # self.pyttsx3_engine.say(input)
        # self.pyttsx3_engine.runAndWait()
        return "done"
    
if __name__ == "__main__":
    input = "Hello, how are you today?"
    oVoiceOutput = cVoiceOutput()
    oVoiceOutput.speak_to_audience_pyttsx3(input)
    pass