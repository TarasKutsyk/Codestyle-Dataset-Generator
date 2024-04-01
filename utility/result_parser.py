import json

def parse_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        
        style_rule = data["style_rule"]
        examples = data["examples"]
        
        return style_rule, examples

filename = "buffer_result.json" # Replace with your JSON file path

style_rule, examples = parse_json_file(filename)

print("Style Rule:", style_rule)
print("Examples:")
for i, example in enumerate(examples, start=1):
    print(f"Example {i}:\n{example}", end='\n\n')