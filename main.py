""" IMPLEMENTATION:
    Read file path from cmd arguments
    Store all the lines in the file on first read
    Write the lines read to the output file in reverse order (start from the bottom of the list)
    While writing, reverse the words in the sentence
"""

""" ASSUMPTIONS:
    - The input file should be a text file
    - The first argument should be the input file path and the second argument should be the output file path
    - The file path should be entered correctly
"""

import time
import argparse

parser = argparse.ArgumentParser(
    prog='main',
    description='Reverse the lines of a file, the sentences in a line, and the words in a sentence',
    epilog='Please make sure you entered the correct file path.'
)
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()
lines = []

# Calculate the start time
start_time = time.perf_counter_ns()

#Read all the lines in the file into a list
try:
    with open(args.input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("The file path entered may be incorrect or the file does not exist.")
    print("Please enter the correct file path or create the input file before running the program.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)


"""
    Starting from the end of the list containing the file's lines,
    write out each line to the output file specified.
    While writing, reverse the contents of the line.
"""
with open(args.output_file, "w") as out_file:
    start = 0
    end = len(lines)

    for i in range(end-1, -1, -1):
        line = lines[i].rstrip()[::-1]

        if i != 0:
            out_file.write(f"{i+1}. {line}\n")
        else:
            out_file.write(f"{i+1}. {line}")

# Calculate the end time and time taken
end_time = time.perf_counter_ns()
t_length = (end_time - start_time)/(10**6)

# Show the result
print(f"It took {t_length} ms! for {end} lines")
