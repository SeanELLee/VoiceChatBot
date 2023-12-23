

class cConstant4Gpt:
    str_openai_model : str = "gpt-3.5-turbo"

class cConstant4VoiceOutput:
    str_voice_actor_elevenlabs : str = "Bella"
    str_language_gTTS : str = "en"
    bool_slow_gTTS : str = "False"
    str_accent : str ="com.au"
    str_standard_greeting_phrase : str = "Yeah?"
    str_standard_ending_phrase : str = "Thank you for using VoiceGPT. Bye!"
    str_standard_dismiss_phrase : str = "I will always be there when you need me."
    str_standard_dismiss_command : str = "bye"
    str_standard_termination_command : str = "terminate"
    str_chatbot_name : str = "Alex"

class cConstant4CleanUp:
    list_directories_of_pycache : list = [
                                            "./VoiceGptLib/Auxiliary",
                                            "./VoiceGptLib/ChatGPT",
                                            "./VoiceGptLib/Runtime",
                                            "./VoiceGptLib/Voice",
                                            "./VoiceGptLib/API"
                                        ]
    