import os
import anthropic
from dotenv import load_dotenv

from utility.changeable_aspects import get_aspects
from utility.claude_prompts import RESTRICTED_PROMPT_CORRECT as PROMPT_CORRECT, PROMPT_WRONG 

load_dotenv()
CLIENT = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def get_response(prompt_text, 
                 model = "claude-3-sonnet-20240229",
                 max_tokens = 2000,
                 temperature = 0, **kwargs):
    message = CLIENT.messages.create(
        model=model, max_tokens=max_tokens, temperature=temperature, **kwargs,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_text
                    }
                ]
            }
        ],
    )
    return message.content

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
