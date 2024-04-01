import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

prompt = """
You are an expert programmer with extensive experience and vast knowledge of different industries. You will help me create a dataset for correcting a code style according to the PEP 8 Python guideline. The dataset will be in the format "code snippet - correct/wrong label"

You will be given an example of a stylistically correct code snippet, and your task is to generate a total of 10 similar snippets. When generating snippets, you must strictly adhere to the following instructions:

<instructions>

1. Snippets should be identical to the provided <example> in the <style_rule>, but not in all <other_aspects> (all relevant XML-sections are provided to you below)

2. Generate examples that are different in <other_aspects> both from the provided <example> and from each other. You may only change the aspects from the <other_aspects> block, so don't be overly creative.

3. Pay special attention to identation: some <style_rule>s rely on a specific number of spaces/tabs in each new line of code (starting from '\n' symbol), so you want to keep the identation identical to the one provided in the <example>.

</instructions>

<style_rule>
{rule}
</style_rule>

<other_aspects>
- function naming, 
- number of function arguments (i.e. function signature), 
- names of function arguments (must be of different length)
</other_aspects>

<example>
{code}
</example>

<output_instruction>

1. By looking at the <example> and <style_rule>, start your output with carefully refining the <style_rule> by generating <refined_rule> block. In this block, try to explain how to follow the <style_rule> step-by-step. Imagine explaining it to a new employee who has no context on how to use the rule aside from what you explicitly tell them. 

2. Paying close attention to the information from the <refined_rule> and <other_aspects> blocks, generate your samples as described in the <instructions>. 

3. Double-check your generated samples by counting whitespaces to make the identation correct (see rule #3).

The output result should be in the following format:

<result>
{{code_snippet_1}}
--
{{code_snippet_2}}
--
...
--
{{code_snippet_10}}
</result>
</output_instruction>
"""

def claude_prompt(prompt_rule: str, prompt_code: str, verbose=True):
    prompt_text = prompt.format(rule=prompt_rule, code=prompt_code)
    if verbose:
        print('Prompt:\n' + prompt_text)

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