# Python Program to Print 1-12-123-1234 Pattern up to n lines

n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# ********************************************************
# Python Program To Print A-BB-CCC-DDDD Pattern Up To n Lines   

n = int(input("Enter number of rows: "))
a = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%c"%(a),end="")
    a+=1
    print()

# ********************************************************
# Python Program to Print (Generate) Right Angle Triangle Star Pattern

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()
