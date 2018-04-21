fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be open:', fname)
    exit()

for line in fhand:
    print(line.upper().rstrip())
