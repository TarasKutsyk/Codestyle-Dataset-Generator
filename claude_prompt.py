import os
from dotenv import load_dotenv
import anthropic

from utility.changeable_aspects import get_aspects
from utility.claude_prompts import RESTRICTED_PROMPT as PROMPT

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def claude_prompt(prompt_rule: str, prompt_code: str, aspects_list: list[str], verbose=True):
    prompt_text = PROMPT.format(rule=prompt_rule, code=prompt_code, 
                                aspects=get_aspects(aspects_list))
    if verbose:
        print('PROMPT:\n' + prompt_text)

    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        temperature=0,
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
        ]
    )
    return message.content