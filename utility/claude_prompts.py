RESTRICTED_PROMPT = """
You are an expert programmer with extensive experience and vast knowledge of different industries. You will help me create a dataset for correcting a code style according to the PEP 8 Python guideline.

You will be given an example of a stylistically correct code snippet, and your task is to generate a total of 10 similar snippets. When generating snippets, you must strictly adhere to the following instructions:

<instructions>
1. Snippets are valid pieces of Python code that must be identical to the provided <example> in the <style_rule>, but not in all <other_aspects> (all relevant data are provided to you below in the corresponding XML sections).
2. Generated snippets must be different in <other_aspects> both from the provided <example> and from each other. You may change the <example> code in the aspects from the <other_aspects> block **only**, so don't be overly creative.
3. Pay special attention to identation: some <style_rule>s rely on a specific, fixed number of spaces in each new line of code (starting from '\\n' symbol), so pay close attention to keep the identation identical to the one provided in the <example>.
</instructions>

<style_rule>
{rule}
</style_rule>

<other_aspects>
{aspects}
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

CREATIVE_PROMPT = """

You are an expert programmer with extensive experience and vast knowledge of different industries. You will help me create a dataset for correcting a code style according to the PEP 8 Python guideline.

You will be given an example of a stylistically correct code snippet, and your task is to generate a total of 10 similar snippets. When generating snippets, you must strictly adhere to the following instructions:

<instructions>
1. Snippets are valid pieces of Python code that must be identical to the provided <example> in the <style_rule>, but not in all <other_aspects> (all relevant data are provided to you below in the corresponding XML sections).
2. Your generated samples must be as diverse as possible in all <other_aspects>. Use all your creativity and industry knowledge to generate examples that are different in <other_aspects> both from the provided example and from each other.
3. Pay special attention to identation: some <style_rule>s rely on a specific, fixed number of spaces in each new line of code (starting from '\\n' symbol), so pay close attention to keep the identation identical to the one provided in the <example>.
</instructions>

<style_rule>
{rule}
</style_rule>

<other_aspects>
{aspects}
</other_aspects>

<example>
{code}
</example>

<output_instruction>
1. By looking at the <example> and <style_rule>, start your output with carefully refining the <style_rule> by generating <refined_rule> block. In this block, try to explain how to follow the <style_rule> step-by-step. Imagine explaining it to a new employee who has no context on how to use the rule aside from what you explicitly tell them. 
2. Then refine the <other_aspects> you can change in your samples by looking at the <example>, and noticing all the features apart from <style_rule> you can change in this <example>. Wrap this section into <refined_aspects> tags.
3. Finally, paying close attention to the information from the <refined_rule> and <refined_aspects> blocks, generate your samples (only code, without comments). The output result should be in the JSON format:

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
</output_instruction>"""