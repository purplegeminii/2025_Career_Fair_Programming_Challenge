# Read file from cmd arguments
# Store the lines in the file on first read
"""
[
Have a book
Play some games
Go to sleep
]
"""
import argparse


parser = argparse.ArgumentParser(prog='main',
                                 description='Reverse the lines of a file, the sentences in a line, and the words in a sentence',
                                 epilog='Make sure you enter the file name correctly')

parser.add_argument('input_file') 
parser.add_argument('output_file') 
args = parser.parse_args()


lines = []
with open(args.input_file, "r") as file:
    lines = file.readlines()

with open(args.output_file, "w") as out_file:
    # for i in range(len(lines)):
    #     if lines[i] in ["\n", "\r\n"]:
    #         print(i+1)
    start = 0
    end = len(lines)

    for i in range(end-1, -1, -1):
        line = lines[i].rstrip()[::-1]

        if i != 0:
            out_file.write(f"{i+1}. {line}\n")
        else:
            out_file.write(f"{i+1}. {line}")    
    
    




