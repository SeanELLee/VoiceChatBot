import openai

class cGptHandler():
    def __init__(self) -> None:
        pass

    def send_and_acquire_response(self, api_key : str, model : str, message : str) -> str:
        openai.api_key = api_key
        model = model

        package = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
                ]

        response = openai.chat.completions.create(model=model, messages=package)

        return response.choices[0].message.content


if __name__ == "__main__":
    str_openai_api_key : str = "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"            #Enter OpenAI API key here
    while True:
        print("How can I help you today?")
        message : str = input()
        oGptHandler = cGptHandler()
        response = oGptHandler.send_and_acquire_response(str_openai_api_key, "gpt-3.5-turbo", message)
        print(response)
        pass