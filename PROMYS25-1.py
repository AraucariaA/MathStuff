import ast
import time

start_time = time.time()

def rowToCol(arr):
    '''
    Turns rows into columns and vice versa. Was initially used in place of colGatherer.
    The array must be rectangular. 
    '''
    newArr=[]

    for i in range(0, len(arr[0])):
        newArr.append([])
        for j in range(0, len(arr)):
            newArr[i].append(arr[j][i])
    
    return newArr


def tablePrinter(table):
    '''
    Given an array, will put this into a new .txt file called "DataOut"
    '''
    with open("DataOut.txt", "w") as f:
        for i in range(len(table)-1, -1, -1):
            f.writelines(str(table[i]) + "\n")


def colGatherer(arr, xpos):
    '''
    Given an x-value in the arrary, this function will return all the known numbers in that
        column. In practice, this means all the numbers below your current y-position.
    '''
    newArr=[]
    # print("lenarr", len(arr))
    for i in range(0, len(arr)-1):
        # print("newArr", newArr)
        # print("arr[i]", arr[i])
        # print("i", i)
        # print("xpos", xpos)
        # ValI stands for Value-Integer, ValL stands for Value-List
        valI = arr[i][xpos]
        # valL = [valI]
        newArr += [valI]
    return newArr


def numberFinder(arr, xpos, ypos):
    '''
    Gives you the minimum number that can be placed knowing the column below it and the 
        row behind it.
    Will not work if the numbers above/ahead are in the array.
    '''
    # print("call")
    cols = colGatherer(arr, xpos)
    rows = arr[ypos]
    nums = cols + rows
    # print("nums", nums)
    done = False
    for i in range(0, max(nums)+2):
        if i in nums:
            pass
        else:
            return i


def efficientNumberFinder(arr, xpos, ypos):
    '''
    Works the same as numberFinder() in theory. Differences:
    - When comparing, instead of comparing against the left-of-diagonal it uses the 
        equivilent column as the table is symmetric
    - Casts the list into a set to make searching easier. This lowers the time complexity 
        by orders of magnitude (without this, it takes >10 hours)
    '''
    # TODO: Finish. This is just copied from the other
    # print("call")
    # print("x")
    cols = colGatherer(arr, xpos)
    # print("y")
    rowLeft = colGatherer(arr, ypos)
    rowRight = arr[ypos]
    nums = set(cols + rowLeft+rowRight)
    # print("nums", nums)
    done = False
    for i in range(0, max(nums)+2):
        if i in nums:
            pass
        else:
            return i


def tableBuilder(length):
    '''
    Will build a square table, where the left side of the diagonal is filled with 8's for easier viewing and indexing
    '''
    try:
        #each array is a row
        table = []

        for ypos in range(0, length):
            table.append([])
            for xpos in range(0, length):
                if ypos==0:
                    table[ypos].append(xpos)
                elif xpos<ypos:
                    table[ypos].append(8)
                else:
                    # table[ypos].append(numberFinder(table,xpos,ypos))
                    table[ypos].append(efficientNumberFinder(table,xpos,ypos))
        
        return table
    except KeyboardInterrupt:
        print("stopped")
        return table

# function call to build the table
# tablePrinter(tableBuilder(2000))
# print("time taken", (time.time() - start_time))


def posFinder(filepath, xpos, ypos):
    '''
    Parses a .txt file and then returns the value at the specified index.
    '''
    with open(filepath, "r") as f:
        fileS = f.read()
    arr = fileS.splitlines()
    for i in range(0, len(arr)):
        arr[i]=ast.literal_eval(arr[i])
    return(arr[ypos][xpos])

# function call to find the answer
# print(posFinder(r"C:\Users\Makore\.vscode\MyProjects\DataOut2000.txt", 1607, 1989))