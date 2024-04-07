import csv

def load_csv_to_dict(csv_fname):
    comments_dict = {}

    with open(csv_fname, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if row:  # Ensure it's not an empty row
                comment = row[0]
                comments_dict[comment] = row
    return comments_dict

def is_comment_in_dict(comments_dict, comment):
    return comment in comments_dict

label = 'correct'
fname = 'buffer_' + 'correct' + '.txt'

# Define the name of the CSV file
csv_fname = '../dataset.csv'

# Read the multiple-lines text from a file
with open(fname, 'r') as file:
    multiple_lines_text = file.read()
    lines = multiple_lines_text.strip().split('--')

comments_dict = load_csv_to_dict(csv_fname)
with open(csv_fname, 'a', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    for line in lines:
        # Extract relevant sections
        comment, aspects, *code = line.strip().split('\n')
        # Preprocess comment and changeable aspects
        comment = comment.strip('# ')
        aspects = aspects.strip('# ')
        # Preprocess code snippet
        code = '\n'.join(code)

        if not is_comment_in_dict(comments_dict, comment):
            # Append the new row to the CSV file
            new_row = [comment, code, aspects, label, 'false']
            csv_writer.writerow(new_row)
