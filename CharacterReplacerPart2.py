import csv
import re

# Open the input CSV file
with open('output_file.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)

    # Open the output CSV file
    with open('final_CleanDATA.csv', 'w') as output_file:
        csv_writer = csv.writer(output_file)

        # Iterate over the rows in the input CSV file
        for row in csv_reader:
            # Remove any white space from the row
            row = [re.sub(r'\s+', '', cell) for cell in row]

            # Replace the letter w with the number 15
            row = [re.sub(r'w', '15', cell) for cell in row]

            # Remove the characters e, v, a, l, %, [, ], /
            row = [re.sub(r'[-dfhgceval%\[\]/]', '', cell) for cell in row]

            # Write the modified row to the output CSV file
            csv_writer.writerow(row)
