from typing import List, Dict
import openai


class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

    def image_generation(self, prompt: str) -> str:
        pass


class OpenAIModel(ModelInterface):
    def __init__(self, api_key: str, model_engine: str, image_size: str = '512x512'):
        openai.api_key = api_key
        self.model_engine = model_engine
        self.image_size = image_size

    def chat_completion(self, messages) -> str:
        return openai.ChatCompletion.create(
            model=self.model_engine, messages=messages
        )

    def image_generation(self, prompt: str) -> str:
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size=self.image_size
            )
        except Exception as e:
            print(e)
            if str(e) == "Your request was rejected as a result of our safety system. Your prompt may contain text that is not allowed by our safety system.":
                return "Your prompt may contain text that is not allowed by our safety system.\nContent Policy: https://labs.openai.com/policies/content-policy"
            return str(e)
        return response.data[0].url
