import os
from openai import OpenAI
from dotenv import load_dotenv

from utility.changeable_aspects import get_aspects
from utility.claude_prompts import RESTRICTED_PROMPT_CORRECT as PROMPT_CORRECT, PROMPT_WRONG, PROMPT_REGENERATE_CORRECT

load_dotenv()

class GPTClient:
    def __init__(self) -> None:
        self._client = OpenAI()
        self._history = []

    def _get_response(self, prompt_text, 
                      model = "gpt-3.5-turbo-16k-0613",
                      max_tokens = 2000,
                      temperature = 0, **kwargs):
        new_message = { "role": "user",
                        "content": prompt_text
        }
        self._history.append(new_message)

        response = self._client.chat.completions.create(model=model, messages=self._history,
                                                        temperature=temperature, max_tokens=max_tokens,
                                                        top_p=1, frequency_penalty=0, presence_penalty=0, **kwargs)
        message = response.choices[0].message
        self._history.append({
            "role": message.role,
            "content": message.content
        })

        return response

    def generate_correct_samples(self, prompt_rule: str, prompt_code: str, aspects_list: list[str], verbose=True, **kwargs):
        prompt_text = PROMPT_CORRECT.format(rule=prompt_rule, code=prompt_code, 
                                            aspects=get_aspects(aspects_list))
        if verbose:
            self._print_chat(prompt_text)

        return self._get_response(prompt_text, **kwargs)

    def generate_wrong_samples(self, prompt_rule: str, wrong_code: str, aspects_list: list[str], correct_code: str, verbose=True, **kwargs):
        prompt_text = PROMPT_WRONG.format(rule=prompt_rule, aspects=get_aspects(aspects_list),
                                          wrong_code=wrong_code, correct_code=correct_code)

        if verbose:
            self._print_chat(prompt_text)
        return self._get_response(prompt_text, **kwargs)
    
    def regenerate_correct_samples(self, wrong_snippets_list: list[str], verbose=True, **kwargs):
        wrong_snippets_str = '\n--\n'.join(wrong_snippets_list)

        prompt_text = PROMPT_REGENERATE_CORRECT.format(wrong_snippets=wrong_snippets_str,
                                                       wrong_snippets_count=len(wrong_snippets_list))
        if verbose:
            self._print_chat(prompt_text)

        return self._get_response(prompt_text, **kwargs)
    
    def _print_chat(self, new_prompt):
        for item in self._history:
            print(f'\n{item['role'].upper()}:\n', item['content'])
        print(f'\nUSER:\n', new_prompt)
        
    def clear_history(self):
        self._history = []