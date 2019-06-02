import sys
f1 = sys.argv[1]
f2 = sys.argv[2]
f1 = open(f1)
f2 = open(f2, 'w')
for line in f1:
    line = line.strip("\n")
    f2.write(str(len(line)) + "\n")

f1.close()
f2.close()