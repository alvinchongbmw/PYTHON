largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        inum = int(num)
    except:
        inum = None
    if inum is None :
        print("Invalid input")
        continue

    if largest is None :
        largest = inum
    if smallest is None :
        smallest = inum

    if inum > largest :
        largest = inum
    if inum < smallest :
        smallest = inum
    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
