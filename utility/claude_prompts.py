RESTRICTED_PROMPT_CORRECT = """
You are an expert programmer with extensive experience and vast knowledge of different industries. You will help me create a dataset for training an ML model to correct a code style according to the PEP 8 Python guideline.

You will be given an example of a stylistically correct code snippet, and your task is to generate a total of 10 similar snippets. When generating snippets, you must strictly adhere to the following instructions:

<instructions>
1. Snippets are valid pieces of Python code that must be identical to the provided <example> in the <style_rule>, but not in all <other_aspects> (all relevant data are provided to you below in the corresponding XML sections). Provided example may contain multiple independent snippets, but your task is to generate one snippet at a time.
2. Generated snippets must be different in <other_aspects> both from the provided <example> and from each other. If some aspects from <other_aspects> are irrelevant to the provided examples, you can safely ignore them, and focus on relevant ones instead. You may change the <example> code in the aspects from the <other_aspects> block **only**, so don't be overly creative.
3. Pay special attention to identation: some <style_rule>s rely on a specific, fixed number of spaces in each new line of code, so pay close attention to keep the identation identical to the one provided in the <example>, if this is what style rule requires.
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
Warning! Provided <example> may contain multiple independent code snippets, but your task is to **generate one snippet at a time**.

<output_instruction>

1. By looking at the <example> and <style_rule>, start your output with carefully refining the <style_rule> by generating <refined_rule> block. In this block, try to explain how to follow the <style_rule> step-by-step. Imagine explaining it to a new employee who has no context on how to use the rule aside from what you explicitly tell them. 
2. By looking at the <other_aspects> block, generate <generation_instructions> block, starting it with a phrase 'I must vary the following aspects in the code snippets I'm going to generate:', and then repeating & refining all the aspects (relevant to the provided example) from the <other_aspects> block in order to make sure you understood the requirements (do not add any new aspects).   
3. Closely following all the information and adhering to all the instructions from the <refined_rule> and <generation_instructions> blocks, generate your samples as described in the <instructions>. You must apply each instruction from the <generation_instructions> to all of your snippets.

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

CREATIVE_PROMPT_CORRECT = """

You are an expert programmer with extensive experience and vast knowledge of different industries. You will help me a dataset for training an ML model to correct a code style according to the PEP 8 Python guideline.

You will be given an example of a stylistically correct code snippet, and your task is to generate a total of 10 similar snippets. When generating snippets, you must strictly adhere to the following instructions:

<instructions>
1. Snippets are valid pieces of Python code that must be identical to the provided <example> in the <style_rule>, but not in all <other_aspects> (all relevant data are provided to you below in the corresponding XML sections).
2. Your generated samples must be as diverse as possible in all <other_aspects>. Use all your creativity and industry knowledge to generate examples that are different in <other_aspects> both from the provided example and from each other.
3. Pay special attention to identation: some <style_rule>s rely on a specific, fixed number of spaces in each new line of code, so pay close attention to keep the identation identical to the one provided in the <example>, if this is what style rule requires.
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
3. Finally, paying close attention to the information from the <refined_rule> and <refined_aspects> blocks, generate your samples (only code, without comments). You must change each aspect from the <refined_aspects> in all of your snippets.

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

PROMPT_WRONG = """
You are an expert programmer with extensive experience and vast knowledge of different industries. You will help me create a dataset for training an ML model to correct a code style according to the PEP 8 Python guideline.

You will be given an example of a stylistically *wrong* snippet, and your task is to generate a total of 10 similar snippets. When generating snippets, you must strictly adhere to the following instructions:

<instructions>
1. Snippets are valid pieces of Python code that must be similar to the provided <wrong_snippet> example in a sense that they *must violate* a certain <style_rule> (all relevant data are provided to you below in the corresponding XML sections). Provided example may contain multiple independent snippets, but your task is to generate one snippet at a time.
2. Snippets will be part of a ML dataset, so they must have some variability, being different both from the provided examples and from each other. To provide this variability, you need to modify the provided examples in the aspects from the <other_aspects> section. If some aspects from <other_aspects> are irrelevant to the provided examples, you can safely ignore them, and focus on relevant ones instead.
3. When generating similar wrong snippets, modifying the provided examples in all the <other_aspects> as described in the previous instruction, you must remember one main rule:
4. Snippets must not be identical to the <correct_snippet> in the <style_rule>.

Summarizing, there are two ways in which you can generate a wrong snippet:
- modifying a <correct_snippet> example by breaking its <style_rule> + applying additional pertrubations in <other_aspects>
- modifying a <wrong_snippet> example where the <style_rule> is already broken + applying additional pertrubations in <other_aspects>
But in either way, you must ensure that the generated snippet *does not follow* the <style_rule> as the <correct_snippet> does.
</instructions>

<style_rule>
{rule}
</style_rule>

<correct_snippet>
{correct_code}
</correct_snippet>

<wrong_snippet>
{wrong_code}
</wrong_snippet>

Warning! Provided examples may contain multiple independent code snippets, but your task is to **generate one snippet at a time**.

<other_aspects>
{aspects}
</other_aspects>

<output_instruction>
1. By comparing the <correct_snippet> and <wrong_snippet>, start your output with defining all possible ways in which you can violate the <style_rule>. Use all your experience of code reviewing to list out all the cases, in which inexperienced programmers could violate the rule, and enclose these cases into the <violate_instructions> tags.
2. Paying close attention in order *not to generate the correct sample* as in in the <correct_snippet> example, and using <other_aspects> and <violate_instructions> you just wrote, start generating stylistically wrong snippets that violate the <style_rule>.
- Each case from the <violate_instructions> must be covered by at least one generated snippet.
- Each generated snippet must be different in each <other_aspect> from other snippets.
3. Generate your snippets (only code, without comments) in the following format:
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

PROMPT_REGENERATE_CORRECT = """
There's a problem with the following snippets you generated:
<wrong_snippets>
{wrong_snippets}
</wrong_snippets>

Now you must correct these snippets, ensuring that all the requirements are met:
1. Snippets have to be consistent with the <style_rule> you were provided with, which you refined in the <refined_rule> block.
2. Snippets have to be different from the provided <example> in all the relevant <other_aspects>, which you listed out in the <generation_instructions>.

Most importantly, you absolutely have to make sure to fix the following issue (ignore this if there's no specific issue specified below):
{issue}

Use the same format to output the corrected snippets (only snippets of code, without comments):
<result>
{{corrected_snippet_1}}
--
...
--
{{corrected_snippet_{wrong_snippets_count}}}
</result>
"""

PROMPT_REGENERATE_WRONG = """
There's a problem with the following snippets you generated:
<wrong_snippets>
{wrong_snippets}
</wrong_snippets>

Now you must correct these snippets, ensuring that all the requirements are met:
1. Snippets absolutely have to violate the <style_rule> you were provided with, implementing one of the violations from <violate_instructions>.
2. Snippets have to be different from the provided examples in all relevant <other_aspects>.

Most importantly, you absolutely have to make sure to fix the following issue (ignore this if there's no specific issue specified below):
{issue}

Use the same format to output the corrected snippets (only snippets of code, without comments):
<result>
{{corrected_snippet_1}}
--
...
--
{{corrected_snippet_{wrong_snippets_count}}}
</result>
"""