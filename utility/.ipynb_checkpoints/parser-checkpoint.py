import csv

label = 'correct'
fname = 'buffer_' + 'correct' + '.txt'

# Define the name of the CSV file
csv_fname = '../dataset.csv' #../result.csv

# Read the multiple-lines text from a file
with open(fname, 'r') as file:
    multiple_lines_text = file.read()
    lines = multiple_lines_text.strip().split('--')

# Open the CSV file in 'write' mode
with open(csv_fname, 'a', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    for line in lines:
        comment, *code = line.strip().split('\n')

        comment = comment.strip('# ')
        code = '\n'.join(code)
        
        # Write the formatted line and label to the CSV file
        csv_writer.writerow([comment, code, label])
