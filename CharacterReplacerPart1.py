import csv
import re

regex = re.compile(r'[prnbqkPRNBQK]')  # regex to match chess pieces

with open('Chess_DatasetCSV (version 1).csv', 'r') as input_file, open('output_file.csv', 'w') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        # convert non-numeric characters to numerics
        converted = [regex.sub(lambda match: str(ord(match.group(0)) - 96), cell) for cell in row]

        # write out converted row to new file
        writer.writerow(converted)
