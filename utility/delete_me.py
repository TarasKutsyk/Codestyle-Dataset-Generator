import xmltodict

def extract_style_rule_and_snippets(xml_string):
    parsed_xml = xmltodict.parse(xml_string)
    style_rule = parsed_xml['root']['style_rule']
    snippets = parsed_xml['root']['result']['snippet']
    return style_rule.strip(), snippets

xml_string = '''
<root>
    <style_rule>
    The style rule demonstrated in the example is to add extra indentation (4 spaces) on the continuation line of a conditional statement when it spans multiple lines.
    </style_rule>
    
    <other_aspects>
    Other aspects that can be changed include:
    - Function/variable names
    - Number of conditions in the conditional statement
    - Logical operators used (and, or, not)
    - Length of variable/function names
    - Types of values used (strings, numbers, booleans)
    - Use of parentheses around the conditions
    </other_aspects>

    <result>
    <snippet>
    if (long_variable_name_1 is not None
            and very_long_function_call(arg1, arg2, arg3)):
        do_something_else()
    </snippet>

    <snippet>
    if (user_authenticated
            or admin_override):
        grant_access()
    </snippet>

    <snippet>
    if (check_password("mypassword")
            and validate_email("user@example.com")):
        create_account()
    </snippet>

    <snippet>
    if (temperature > 30
            and humidity < 40):
        turn_on_ac()
    </snippet>

    <snippet>
    if (is_weekend()
            or is_holiday(today)):
        send_notification("Enjoy your day off!")
    </snippet>

    <snippet>
    if (x < min_value
            or x > max_value):
        raise ValueError("Value out of range")
    </snippet>

    <snippet>
    if (process_data(input_file)
            and generate_report(output_file)):
        print("Success!")
    </snippet>

    <snippet>
    if (check_inventory(product_id)
            and validate_payment(amount)):
        complete_order()
    </snippet>

    <snippet>
    if (is_prime(num)
            or is_even(num)):
        print(f"{num} is prime or even")
    </snippet>

    <snippet>
    if (connect_to_database()
            and run_queries(sql_script)):
        commit_changes()
    </snippet>
    </result>
</root>
'''

style_rule, snippets = extract_style_rule_and_snippets(xml_string)

print("Style Rule:")
print(style_rule)
print("\nSnippets:")
for i, snippet in enumerate(snippets, 1):
    print(f"Snippet {i}:")
    print(snippet.strip())
    print()
