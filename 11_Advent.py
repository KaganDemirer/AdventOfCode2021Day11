with open("11_Advent.txt") as input_file:
    read_lines = input_file.readlines()

matrix = []
flashed = []
flashes = 0
sumflashes = 0

for y in read_lines:
    tp = []
    for x in y[:-1]:
        tp.append(x)
    matrix.append(tp)

def add(y,x):
    matrix[y][x] = str(int(matrix[y][x])+1)


def step():
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] = str(int(matrix[y][x])+1)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            check(y,x)
    

def check(y, x):
    global flashes
    global flashed
    if int(matrix[y][x]) > 9:
        flashes+=1
        flashed.append([y,x])
        matrix[y][x] = str(0)
        if x-1!=-1:
            if int(matrix[y][x-1])!=0 and [y,x-1] not in flashed:
                add(y,x-1)
                check(y,x-1)
            if y-1!=-1:
                if int(matrix[y-1][x-1])!=0 and [y-1,x-1] not in flashed:
                    add(y-1,x-1)
                    check(y-1,x-1)
            if y+1!=len(matrix):
                if int(matrix[y+1][x-1])!=0 and [y+1,x-1] not in flashed:
                    add(y+1,x-1)
                    check(y+1,x-1)
        if x+1!=len(matrix[y]):
            if int(matrix[y][x+1])!=0 and [y,x+1] not in flashed:
                add(y,x+1)
                check(y,x+1)
            if y-1!=-1:
                if int(matrix[y-1][x+1])!=0 and [y-1,x+1] not in flashed:
                    add(y-1,x+1)
                    check(y-1,x+1)
            if y+1!=len(matrix):
                if int(matrix[y+1][x+1])!=0 and [y+1,x+1] not in flashed:
                    add(y+1,x+1)
                    check(y+1,x+1)
        if y-1!=-1:
            if int(matrix[y-1][x])!=0 and [y-1,x] not in flashed:
                add(y-1,x)
                check(y-1,x)
        if y+1!=len(matrix):
            if int(matrix[y+1][x])!=0 and [y+1,x] not in flashed:
                add(y+1,x)
                check(y+1,x)

times = 0

while True:
    sumflashes = 0
    times+=1
    print("Step:", times)
    step()
    flashed.clear()
    for x in matrix:
        intx = [int(y) for y in x]
        sumflashes = sumflashes+sum(intx)
        print(x)
    print(sumflashes)
    print()
    if(sumflashes==0):
        break

print(flashes)