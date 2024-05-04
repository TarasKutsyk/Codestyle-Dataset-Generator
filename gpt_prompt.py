import os
from openai import OpenAI
from dotenv import load_dotenv

from utility.changeable_aspects import get_aspects
from utility.claude_prompts import RESTRICTED_PROMPT_CORRECT as PROMPT_CORRECT, PROMPT_WRONG 

load_dotenv()

CLIENT = OpenAI()

def get_response(prompt_text, 
                 model = "gpt-3.5-turbo-16k-0613",
                 max_tokens = 2000,
                 temperature = 0, **kwargs):
    response = CLIENT.chat.completions.create(
                    model=model,
                    messages=[
                      {
                        "role": "user",
                        "content": prompt_text
                      }
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0, **kwargs
                )                   
    return response

def generate_correct_samples(prompt_rule: str, prompt_code: str, aspects_list: list[str], verbose=True, **kwargs):
    prompt_text = PROMPT_CORRECT.format(rule=prompt_rule, code=prompt_code, 
                                        aspects=get_aspects(aspects_list))
    if verbose:
        print('PROMPT:\n' + prompt_text)

    return get_response(prompt_text, **kwargs)

def generate_wrong_samples(prompt_rule: str, wrong_code: str, aspects_list: list[str], correct_code: str, verbose=True, **kwargs):
    prompt_text = PROMPT_WRONG.format(rule=prompt_rule, aspects=get_aspects(aspects_list),
                                      wrong_code=wrong_code, correct_code=correct_code)
    
    if verbose:
        print('PROMPT:\n' + prompt_text)

    return get_response(prompt_text, **kwargs)
