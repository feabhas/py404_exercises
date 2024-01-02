#!/usr/bin/env python3

"""Simple implementation of a quicksort"""

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop(len(array) // 2)
    print("Chose pivot {}".format(pivot))
    les = []
    greater = []
    for value in array:
        if value <= pivot:
            les.append(value)
        else:
            greater.append(value)
    return quicksort(les) + [pivot] + quicksort(greater)

def main():
    data = [1, 7, 4, 5, 9, 14, 2, 2, 3]
    print(quicksort(data))

if __name__ == '__main__':
    main()