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
    oGptHandler = cGptHandler()
    oGptHandler.send_and_acquire_response()
    pass