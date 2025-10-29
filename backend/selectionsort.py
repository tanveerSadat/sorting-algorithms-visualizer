def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

def selectionSortWithSteps(arr):
    steps = []
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            steps.append([arr.copy(), i, j, minIndex, False])
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            steps.append([arr.copy(), i, j, minIndex, True])
        else:
            steps.append([arr.copy(), i, j, minIndex, False])

    return steps

# def printStep(step):
#     arr, i, j, minIndex, swapped = step
#     arrStr = " ".join(map(str, arr))
#     print(arrStr)

#     iArrow = [" "] * len(arr)
#     jArrow = [" "] * len(arr)
#     mArrow = [" "] * len(arr)

#     iArrow[i] = "i"
#     jArrow[j] = "j"
#     mArrow[minIndex] = "m"

#     print(" ".join(iArrow))
#     print(" ".join(jArrow))
#     print(" ".join(mArrow))

#     if swapped:
#         print("Swap occurred!\n")
#     else:
#         print()

# if __name__ == "__main__":

#     arr = [1, 3, 2, 4, 5, 7, 6]
#     steps = selectionSortWithSteps(arr.copy())
#     for step in steps:
#         printStep(step)
            
    