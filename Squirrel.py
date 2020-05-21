'''
Author: wagnerb@udel.edu
Updated: 2/13/2020
Description:  Summate a sequence of numbers while skipping certain ones.
              The total, or corresponding message is then output.
'''

# Get the filename from stdin
filename = input()

# Reads individual lines from file into a list
with open(filename) as i:
    lines = i.readlines()

# Determine number of lines to read
repeat = int(lines[0])

# Initialize total
total = 0

# Loops through lines in file and adds positive numbers to total
for x in range(repeat):
    if int(lines[x+1]) == -999:# x + 1 to account for first line having total number of lines.
        break
    elif int(lines[x+1]) >= 0:
        total += int(lines[x+1])
    else:
        continue

# Output total or corresponding message
if total > 0:
    print (total)
else:
    print ("EMPTY")
