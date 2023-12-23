from VoiceGptLib.Voice.VoiceOutput import cVoiceOutput
from VoiceGptLib.Voice.VoiceRecognition import cVoiceRecognition
from VoiceGptLib.ChatGPT.GptHandler import cGptHandler
from VoiceGptLib.Auxiliary.Cleanup import cCleanUp
from VoiceGptLib.Runtime.Constants import cConstant4Gpt, cConstant4VoiceOutput, cConstant4CleanUp

class cPackager():
    def __init__(self) -> None:
        self.oVoiceOutput = cVoiceOutput()
        self.oVoiceRecognition = cVoiceRecognition()
        self.oGptHandler = cGptHandler()
        self.oCleanUp = cCleanUp()
        pass

    def clean_up(self) -> None:
        self.oCleanUp.delete_pycache(cConstant4CleanUp.list_directories_of_pycache)
        pass

    def main_loop(self, str_open_ai_api_key : str, str_elevenlabs_api_key : str) -> None:
        while True:
            # Computer Response:
            text_from_speech = self.oVoiceRecognition.record_speech_to_text()
            print(text_from_speech)
            if text_from_speech == cConstant4VoiceOutput.str_chatbot_name:
                input_for_voice_output = cConstant4VoiceOutput.str_standard_greeting_phrase
                self.oVoiceOutput.speak_to_audience_elevenlabs(str_elevenlabs_api_key, cConstant4VoiceOutput.str_voice_actor_elevenlabs, input_for_voice_output)
                while True:
                    text_from_speech = self.oVoiceRecognition.record_speech_to_text()
                    print(text_from_speech)
                    if text_from_speech != cConstant4VoiceOutput.str_standard_dismiss_command:
                        input_for_gpt = str(text_from_speech)
                        message = self.oGptHandler.send_and_acquire_response(str_open_ai_api_key, cConstant4Gpt.str_openai_model, input_for_gpt)
                        print(message)

                        #Speaker
                        input_for_voice_output = message
                        self.oVoiceOutput.speak_to_audience_elevenlabs(str_elevenlabs_api_key, cConstant4VoiceOutput.str_voice_actor_elevenlabs, input_for_voice_output)
                        print("end")
                    
                    elif text_from_speech == cConstant4VoiceOutput.str_standard_dismiss_command:
                        input_for_voice_output = cConstant4VoiceOutput.str_standard_dismiss_phrase
                        self.oVoiceOutput.speak_to_audience_elevenlabs(str_elevenlabs_api_key, cConstant4VoiceOutput.str_voice_actor_elevenlabs, input_for_voice_output)
                        break
            elif text_from_speech == cConstant4VoiceOutput.str_standard_termination_command:
                input_for_voice_output = cConstant4VoiceOutput.str_standard_ending_phrase
                self.oVoiceOutput.speak_to_audience_elevenlabs(str_elevenlabs_api_key, cConstant4VoiceOutput.str_voice_actor_elevenlabs, input_for_voice_output)
                break
    pass

if __name__ == "__main__":
    oPackager = cPackager()
    oPackager.clean_up()
    oPackager.main_loop()
    pass

