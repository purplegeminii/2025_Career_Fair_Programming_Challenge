# Read file path from cmd arguments
# Store the lines in the file on first read
# Write the lines read to the output file in reverse order (start from the bottom of the list)
# While writing, reverse the words in the sentence

import argparse
import time

parser = argparse.ArgumentParser(
    prog='main',
    description='Reverse the lines of a file, the sentences in a line, and the words in a sentence',
    epilog='Make sure you enter the file name correctly'
)

parser.add_argument('input_file') 
parser.add_argument('output_file') 
args = parser.parse_args()

# Calculate the start time
start = time.perf_counter_ns()

# [100, 200, 400, 800, 1000, 2000, 4000, 6000, 8000, 10000]
no_of_lines = 100

""" Read all the lines in the file into a list """
lines = []
with open(args.input_file, "r", encoding="utf-8") as file:
    lines = file.readlines(no_of_lines)


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
end = time.perf_counter_ns()
t_length = end - start

# Show the result
print(f"It took {t_length} seconds! for {no_of_lines} lines")




