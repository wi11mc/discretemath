def BottlesOfBeer(n):
    if n > 0:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer")
        print(f"take one down pass it around, {n - 1} bottles of beer on the wall")
        BottlesOfBeer(n - 1) # using recursion to decrement the number of bottles by 1
    else:
        print("no bottles of beer on the wall no bottles of beer")
        print("go to the store, buy some more")
        
BottlesOfBeer(8)

#linear search algorithm

def LinearSearch(x, lst):
    for index in range(len(lst)):
        if lst[index] == x:
            return index
    return -1

testList = [7, 7, 3, 6, 4, 1, 9, 2]
target = 9
location = LinearSearch(target, testList)
if location != -1:
    print(f"target {target} found at index {location}")
else:
    print(f"target {target} not found in list")