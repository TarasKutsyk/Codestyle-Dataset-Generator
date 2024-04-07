import csv

def load_csv_to_dict(csv_fname):
    """Builds a dictionary out of the CSV, using comment field as a key"""

    csv_dict = {}

    with open(csv_fname, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if row:  # Ensure it's not an empty row
                comment = row[1]
                csv_dict[comment] = row
    return csv_dict

def does_row_exist(csv_dict, comment):
    """Checks whether a row exists in a dictionary csv_dict based on the comment field"""
    return comment in csv_dict

def get_buffer_name(label):
    return f'./buffer_{label}.txt'

def get_csv_name(label):
    return f'../dataset_{label}.csv'

LABELS = {'correct', 'wrong'}

items = []
for label in LABELS:
    buffer_name = get_buffer_name(label)

    with open(buffer_name, 'r') as file:
        multiple_lines_text = file.read()
        lines = multiple_lines_text.strip().split('--')
        items.append(lines)

correct_items, wrong_items = items
 # 1st validity check: the buffers must contain the same number of elements
assert len(correct_items) == len(wrong_items), "The buffers must contain the same number of elements" 

N_items = len(correct_items)

csv_correct_name = get_csv_name('correct')
csv_wrong_name = get_csv_name('wrong')

correct_writer = csv.writer(open(csv_correct_name, 'a'), quoting=csv.QUOTE_ALL)
wrong_writer = csv.writer(open(csv_wrong_name, 'a'), quoting=csv.QUOTE_ALL)

correct_csv_dict = load_csv_to_dict(csv_correct_name)
wrong_csv_dict = load_csv_to_dict(csv_wrong_name)

for i in range(N_items):
    correct_sample = correct_items[i]
    wrong_sample = wrong_items[i]

    # Extract relevant sections
    correct_comment, aspects, *correct_code = correct_sample.strip().split('\n')
    wrong_comment, *wrong_code = wrong_sample.strip().split('\n')

    # 2nd validity check: ensure that the corresponding samples are correct & wrong examples for the *same* style rule
    assert correct_comment == wrong_comment, \
        f"The buffers contain different style rules on position #{i}:\n\tcorrect style rule: {correct_comment}\n\twrong style rule: {wrong_comment}"

    # Preprocess comments changeable aspects
    correct_comment, wrong_comment = correct_comment.strip('# '), wrong_comment.strip('# ')
    aspects = aspects.strip('# ')
    # Preprocess code snippets
    correct_code, wrong_code = '\n'.join(correct_code) ,'\n'.join(wrong_code)

    new_row_id = hash(correct_comment)

    if not does_row_exist(correct_csv_dict, correct_comment):
        # Append the new row to the CSV file with correct samples
        new_row = [new_row_id, correct_comment, correct_code, aspects, 'correct', 'False']
        correct_writer.writerow(new_row)

    if not does_row_exist(wrong_csv_dict, wrong_comment):
        new_row = [new_row_id, wrong_comment, wrong_code, 'wrong', 'False']
        wrong_writer.writerow(new_row)