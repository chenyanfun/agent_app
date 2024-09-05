
# analysis data, get prompt&& web pages to openai
# import openai
import os
import yaml

from openai import OpenAI

current_path = os.path.abspath(__file__)
config_file_path=os.path.join(os.path.abspath(os.path.dirname(current_path)
                                              + os.path.sep), '../conf/config_info.yaml')


class AnalysisData:
    def __init__(self, prompt):
        # Read the key from the configuration file
        self.config_info = self.get_config()
        self.api_key = self.config_info.get("api_key")
        self.openai_model = self.config_info.get("model")
        self.prompt = prompt

    def get_config(self, config_path=config_file_path):
        with open(config_path, 'rb') as f:
            configs = yaml.load(f, Loader=yaml.FullLoader)
            config_info = configs.get('deploy')
        return config_info

    def build_tips(self, filePath=None, prompt=None):
        """
        Combine the crawled text content with the user input prompt word
        :param filePath:
        :param prompt:
        :return:
        """
        with open(filePath, 'rb') as file:
            html_content = file.read()
        prompt_content = f"{prompt},The following is the content of the webpage: {html_content}"
        return prompt_content

    async def analysis_content(self,filePath):
        try:
            prompt_content = self.build_tips(filePath=filePath, prompt=self.prompt)
            client = OpenAI(
                api_key=self.api_key
            )
            response = client.chat.completions.create(
                model=self.openai_model,
                messages=[{"role": "user", "content": prompt_content}]
            )
            generated_text = response.choices[0].message.content.strip()
            # openai.api_key = self.api_key
            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     message=[
            #         {"role": "user", "content": prompt_content}
            #     ],
            #     max_tokens=100
            # )
            # generated_text = response['choices'][0]['message']['content']
            return generated_text
        except Exception as e:
            raise e
        finally:
            os.remove(filePath)
