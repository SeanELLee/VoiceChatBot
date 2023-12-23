from VoiceGptLib.API.Packager import cPackager

str_openai_api_key : str = "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"            #Enter OpenAI API key here
str_api_key_elevenlabs : str = "321007b577b720d45aa0da87a1b4bccd"                           #Enter Elevenlabs API key here

if __name__ == "__main__":
    oPackager = cPackager()
    oPackager.clean_up()
    oPackager.main_loop(str_openai_api_key, str_api_key_elevenlabs)
    pass