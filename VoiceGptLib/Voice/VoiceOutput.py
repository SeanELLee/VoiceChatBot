import elevenlabs
from gtts import gTTS
import playsound

class cVoiceOutput():
    def __init__(self) -> None:
        pass

    def speak_to_audience_elevenlabs(self, api_key, voice_actor : str, input : str) -> str:
        elevenlabs.set_api_key = api_key
        audio = elevenlabs.generate(text = input,  voice = voice_actor)
        elevenlabs.play(audio)
        return "done"
    
    def speak_to_audience_gTTS(self, language : str, slow : str, accent : str, input : str) -> str:
        tts = gTTS(text = input, lang = language, slow = slow, tld = accent)
        playsound.playsound(tts)
        return "done"