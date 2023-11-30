from VoiceGptLib.Voice.VoiceRecognition import cVoiceRecognition
from VoiceGptLib.ChatGPT.GptHandler import cGptHandler
from VoiceGptLib.Voice.VoiceOutput import cVoiceOutput
from VoiceGptLib.Runtime.Constants import cConstant4Gpt, cConstant4VoiceOutput

if __name__ == "__main__":
    oVoiceRegcognition = cVoiceRecognition()
    oGptHandler = cGptHandler()
    oVoiceOutput = cVoiceOutput()

    elevenlab : bool = True
    gTTS : bool = False

    while True:

        # Computer Response:
        text_from_speech = oVoiceRegcognition.record_speech_to_text()
        print(text_from_speech)
        if text_from_speech != cConstant4VoiceOutput.str_standard_termination_command:
            input_for_gpt = str(text_from_speech)
            message = oGptHandler.send_and_acquire_response(cConstant4Gpt.str_openai_api_key, cConstant4Gpt.str_openai_model, input_for_gpt)
            print(message)

            if elevenlab == True:
                input_for_voice_output = message
                oVoiceOutput.speak_to_audience_elevenlabs(cConstant4VoiceOutput.str_api_key_elevenlabs, cConstant4VoiceOutput.str_voice_actor_elevenlabs, input_for_voice_output)
                print("end")
            elif gTTS == True:
                input_for_voice_output = message
                oVoiceOutput.speak_to_audience_gTTS(cConstant4VoiceOutput.str_language_gTTS, cConstant4VoiceOutput.bool_slow_gTTS, cConstant4VoiceOutput.str_accent, input_for_voice_output)
                print("end")
            else:
                print("No speaker is active")
                pass
        
        elif text_from_speech == cConstant4VoiceOutput.str_standard_termination_command:
            input_for_voice_output = cConstant4VoiceOutput.str_standard_ending_phrase
            oVoiceOutput.speak_to_audience_elevenlabs(cConstant4VoiceOutput.str_api_key_elevenlabs, cConstant4VoiceOutput.str_voice_actor_elevenlabs, input_for_voice_output)
            break
    pass