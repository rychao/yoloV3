import os
from sys import argv

run, filename = argv

fin = open(filename)
fout = open(filename + '.tmp', 'w')
lines = fin.readlines()
for line in lines:
    fout.write(line[17:])
fout.close()
fin.close()
os.rename(filename + '.tmp', filename)