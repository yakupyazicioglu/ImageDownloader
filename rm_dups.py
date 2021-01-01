# this script can remove duplicate lines in a text file
lines = open('covers.txt', 'r').readlines()

lines_set = set(lines)

out  = open('workfile.txt', 'w')

for line in lines_set:
    out.write(line)