def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubbleSortWithSteps(arr):

    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append([arr.copy(), i, j, False])
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append([arr.copy(), i, j, True])

    return steps

def printStep(step):
    arr, i, j, swapped = step
    arrStr = " ".join(map(str, arr))
    print(arrStr)

    iArrow = [" "] * len(arr)
    jArrow = [" "] * len(arr)

    iArrow[i] = "i"
    jArrow[j] = "j"
    jArrow[j+1] = "J"

    print(" ".join(iArrow))
    print(" ".join(jArrow))

    if swapped:
        print("Swap happened!\n")
    else:
        print()

if __name__ == "__main__":

    arr = [1, 3, 2, 4, 5, 7, 6]
    steps = bubbleSortWithSteps(arr.copy())
    for step in steps:
        printStep(step)
